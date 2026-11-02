"""Isolated setup regressions. Run with python3 -B scripts/test_setup.py."""

from contextlib import redirect_stdout
import hashlib
import io
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import setup_support as support


class HelpersTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="zendooh setup test ")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.properties = self.root / "local.properties"
        self.sdk = self.root / "SDK with spaces"

    def repair(self, automatic=True):
        with redirect_stdout(io.StringIO()):
            support.sdk_config(str(self.sdk), automatic, self.properties)

    def test_supported_hosts(self):
        for host, arch, expected in (
            ("Linux", "x86_64", "linux-x64"),
            ("Darwin", "x86_64", "macos-x64"),
            ("Darwin", "arm64", "macos-arm64"),
        ):
            with (
                patch.object(support.platform, "system", return_value=host),
                patch.object(support.platform, "machine", return_value=arch),
            ):
                self.assertEqual(support.host_platform(), expected)

    def test_unsupported_host(self):
        with patch.object(support.platform, "system", return_value="Windows"):
            with self.assertRaisesRegex(RuntimeError, "Unsupported host"):
                support.preflight()

    def test_missing_native_library(self):
        with (
            patch.object(support.platform, "system", return_value="Linux"),
            patch.object(support.platform, "machine", return_value="x86_64"),
            patch.object(support.ctypes, "CDLL", side_effect=OSError),
        ):
            with self.assertRaisesRegex(RuntimeError, "Missing native libraries"):
                support.preflight()

    def test_unwritable_directory(self):
        with (
            patch.object(support.os, "access", return_value=False),
            patch.object(support.ctypes, "CDLL"),
        ):
            with self.assertRaisesRegex(RuntimeError, "not writable"):
                support.preflight()

    def test_versions(self):
        for installed in (
            "2026.10.18 linux-x64",
            "2026.10.25 linux-x64",
            "2027.1.0 macos-arm64",
        ):
            support.version("2026.10.18", installed)
        for installed in (
            "2026.10.9 linux-x64",
            "2025.12.99 linux-x64",
            "garbage",
            "2026.10.18-beta",
        ):
            with self.assertRaisesRegex(RuntimeError, "Upgrade mise"):
                support.version("2026.10.18", installed)

    def test_checksum(self):
        binary = self.root / "mise"
        binary.write_bytes(b"fixture binary")
        manifest = self.root / "checksums"
        manifest.write_text(
            hashlib.sha256(binary.read_bytes()).hexdigest() + "  ./asset\n"
        )
        support.checksum(binary, "asset", manifest)
        binary.write_bytes(b"corrupt")
        with self.assertRaisesRegex(RuntimeError, "checksum verification failed"):
            support.checksum(binary, "asset", manifest)

    def test_environment_conflict(self):
        support.sdk_environment(str(self.sdk), "", str(self.sdk / ".." / self.sdk.name))
        with self.assertRaisesRegex(RuntimeError, "ANDROID_HOME conflicts"):
            support.sdk_environment(str(self.sdk), "/some/other/sdk", "")

    def test_missing_property_file_is_not_created(self):
        self.repair()
        self.assertFalse(self.properties.exists())

    def test_absent_or_matching_sdk_is_unchanged(self):
        for content in (
            b"# comment\nother=value\n",
            ("sdk.dir=" + support.escape_path(str(self.sdk)) + "\n").encode(),
        ):
            self.properties.write_bytes(content)
            self.repair()
            self.assertEqual(self.properties.read_bytes(), content)
            self.assertEqual(list(self.root.glob("local.properties.backup-*")), [])

    def test_unattended_conflict(self):
        self.properties.write_text("sdk.dir=/old/sdk\n")
        with patch.object(support.sys, "stdin", io.StringIO()):
            with self.assertRaisesRegex(RuntimeError, "--repair-sdk-config"):
                self.repair(False)
        self.assertEqual(self.properties.read_text(), "sdk.dir=/old/sdk\n")

    def test_prompt_accept_and_backup(self):
        original = b"# keep\r\nother = literal\\value\r\nsdk\\.dir : /old/\\\r\n sdk\r\n! keep too\r\nsdk.dir=/duplicate\r\n"
        self.properties.write_bytes(original)
        with (
            patch.object(support.sys.stdin, "isatty", return_value=True),
            patch("builtins.input", return_value="yes"),
        ):
            self.repair(False)
        backups = list(self.root.glob("local.properties.backup-*"))
        self.assertEqual(len(backups), 1)
        self.assertEqual(backups[0].read_bytes(), original)
        result = self.properties.read_bytes()
        self.assertIn(b"other = literal\\value\r\n", result)
        self.assertIn(b"! keep too\r\n", result)
        values = [
            v for _, k, v in support.property_records(result.decode()) if k == "sdk.dir"
        ]
        self.assertEqual(values, [str(self.sdk)])
        self.repair()
        self.assertEqual(len(list(self.root.glob("local.properties.backup-*"))), 1)

    def test_prompt_decline(self):
        self.properties.write_text("sdk.dir=/old/sdk\n")
        for answer in ("", "n", "no"):
            with (
                patch.object(support.sys.stdin, "isatty", return_value=True),
                patch("builtins.input", return_value=answer),
            ):
                with self.assertRaisesRegex(RuntimeError, "declined"):
                    self.repair(False)
        self.assertEqual(self.properties.read_text(), "sdk.dir=/old/sdk\n")

    def test_backup_failure_preserves_original(self):
        self.properties.write_text("sdk.dir=/old/sdk\n")
        with patch.object(support.tempfile, "mkstemp", side_effect=PermissionError):
            with self.assertRaises(PermissionError):
                self.repair()
        self.assertEqual(self.properties.read_text(), "sdk.dir=/old/sdk\n")

    def test_unicode_property_path(self):
        value = str(self.sdk / "fictional-\U0001f600")
        encoded = support.escape_path(value)
        self.assertTrue(encoded.isascii())
        self.assertEqual(support.unescape(encoded), value)

    def test_comment_backslash_is_not_continuation(self):
        self.properties.write_text(
            "# keep trailing backslash " + "\\" + "\nsdk.dir=/old/sdk\n"
        )
        self.repair()
        self.assertIn(
            "sdk.dir=" + support.escape_path(str(self.sdk)), self.properties.read_text()
        )

    def test_unique_backups(self):
        for _ in range(2):
            self.properties.write_text("sdk.dir=/old/sdk\n")
            self.repair()
        self.assertEqual(len(list(self.root.glob("local.properties.backup-*"))), 2)


FAKE_MISE = r"""#!/usr/bin/env python3
import os, sys
from pathlib import Path
args = sys.argv[1:]
if args == ["--version"]:
    print(os.environ.get("FIXTURE_MISE_VERSION", "2026.10.25 linux-x64"))
elif args[0] in ("trust", "install"):
    if args[0] == "install" and os.environ.get("FIXTURE_INSTALL_FAIL"):
        sys.exit(9)
elif args[0] == "where":
    assert args == ["where", "vfox:android-sdk"], "Use the configured backend, not the registry alias"
    print(os.environ["FIXTURE_SDK"])
elif args[0] == "exec":
    sdk = os.environ["FIXTURE_SDK"]
    os.environ.update(ANDROID_HOME=sdk, ANDROID_SDK_ROOT=sdk,
        ZENDOOH_ANDROID_PACKAGES="platform-tools platforms;android-36 build-tools;35.0.0 build-tools;36.0.0")
    os.environ["PATH"] = sdk + "/cmdline-tools/19.0/bin:" + sdk + "/platform-tools:" + sdk + "/build-tools/36.0.0:" + os.environ["PATH"]
    os.execvpe(args[2], args[2:], os.environ)
else:
    sys.exit(3)
"""

FAKE_SDKMANAGER = r"""#!/usr/bin/env python3
import os, sys
from pathlib import Path
sdk = Path(os.environ["ANDROID_HOME"])
accepted = sdk / "accepted"
if "--licenses" in sys.argv:
    if accepted.exists() or sys.stdin.readline().strip() == "y":
        accepted.touch()
        print("All SDK package licenses accepted.")
    else:
        print("1 of 1 SDK package licenses not accepted.")
elif "--install" in sys.argv:
    if os.environ.get("FIXTURE_SDK_INSTALL_FAIL"):
        sys.exit(7)
    if not accepted.exists():
        sys.exit(8)
    for package in sys.argv[3:]:
        directory = sdk.joinpath(*package.split(";"))
        directory.mkdir(parents=True, exist_ok=True)
        (directory / "package.xml").write_text('<root><localPackage path="' + package + '"/></root>')
"""


class ScriptTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="zendooh setup scripts ")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        (self.root / "scripts").mkdir()
        for source in ("setup.sh", "setup-android.sh", "setup_support.py"):
            shutil.copy(Path(__file__).parent / source, self.root / "scripts" / source)
        (self.root / "mise.toml").write_text('min_version = "2026.10.18"\n')
        self.bin = self.root / "bin"
        self.bin.mkdir()
        self.sdk = self.root / "SDK with spaces"
        self.executable(self.bin / "mise", FAKE_MISE)
        self.executable(self.sdk / "cmdline-tools/19.0/bin/sdkmanager", FAKE_SDKMANAGER)
        for command in ("platform-tools/adb", "build-tools/36.0.0/apksigner"):
            self.executable(self.sdk / command, "#!/bin/sh\nexit 0\n")
        self.executable(self.bin / "java", "#!/bin/sh\nexit 0\n")
        self.executable(self.root / "gradlew", "#!/bin/sh\nexit 0\n")
        self.env = dict(
            os.environ,
            PATH=str(self.bin) + ":" + os.environ["PATH"],
            FIXTURE_SDK=str(self.sdk),
            HOME=str(self.root),
        )
        for name in ("ANDROID_HOME", "ANDROID_SDK_ROOT"):
            self.env.pop(name, None)

    @staticmethod
    def executable(path, content):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
        path.chmod(0o755)

    def run_setup(self, *args):
        return subprocess.run(
            ["bash", "scripts/setup.sh", *args],
            cwd=self.root,
            env=self.env,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            timeout=30,
        )

    def test_repeated_setup(self):
        for _ in range(2):
            result = self.run_setup("--accept-licenses")
            self.assertEqual(result.returncode, 0, result.stdout)
            self.assertIn("Setup complete", result.stdout)

    def test_missing_utility(self):
        # Isolate PATH rather than hiding a required command on the real host.
        self.executable(self.bin / "python3", "#!/bin/sh\nexit 0\n")
        self.env["PATH"] = str(self.bin)
        result = subprocess.run(
            [shutil.which("bash"), "scripts/setup.sh"],
            cwd=self.root,
            env=self.env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Missing curl", result.stdout)

    def test_license_refusal(self):
        result = self.run_setup()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("--accept-licenses", result.stdout)
        self.assertNotIn("Setup complete", result.stdout)

    def test_install_failure(self):
        self.env["FIXTURE_INSTALL_FAIL"] = "1"
        result = self.run_setup("--accept-licenses")
        self.assertEqual(result.returncode, 9)
        self.assertNotIn("Setup complete", result.stdout)

    def test_sdk_package_failure(self):
        self.env["FIXTURE_SDK_INSTALL_FAIL"] = "1"
        result = self.run_setup("--accept-licenses")
        self.assertEqual(result.returncode, 7, result.stdout)
        self.assertNotIn("Setup complete", result.stdout)

    def test_missing_adb_is_not_success(self):
        (self.sdk / "platform-tools/adb").unlink()
        result = self.run_setup("--accept-licenses")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("adb does not resolve", result.stdout)
        self.assertNotIn("Setup complete", result.stdout)

    def test_unsupported_version(self):
        self.env["FIXTURE_MISE_VERSION"] = "2026.1.0 linux-x64"
        result = self.run_setup()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Upgrade mise", result.stdout)

    def test_inherited_sdk_conflict(self):
        self.env["ANDROID_HOME"] = "/old/sdk"
        result = self.run_setup("--accept-licenses")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("ANDROID_HOME conflicts", result.stdout)

    def isolate_bootstrap(self, corrupt=False):
        # Provide only prerequisite commands; no mise executable on PATH.
        (self.bin / "mise").unlink()
        for command in (
            "python3",
            "bash",
            "dirname",
            "sed",
            "mkdir",
            "mktemp",
            "cp",
            "chmod",
            "mv",
            "rm",
            "yes",
            "grep",
            "cat",
            "git",
            "unzip",
            "tar",
        ):
            (self.bin / command).symlink_to(shutil.which(command))
        self.env["PATH"] = str(self.bin)
        payload = self.root / "release-binary"
        payload.write_text(FAKE_MISE)
        manifest = self.root / "release-checksums"
        digest = (
            "0" * 64 if corrupt else hashlib.sha256(payload.read_bytes()).hexdigest()
        )
        asset = "mise-v2026.11.0-" + support.host_platform()
        manifest.write_text(digest + "  ./" + asset + "\n")
        self.env.update(FIXTURE_RELEASE=str(payload), FIXTURE_CHECKSUMS=str(manifest))
        self.executable(
            self.bin / "curl",
            r"""#!/usr/bin/env python3
import json, os, shutil, sys
from pathlib import Path
args = sys.argv[1:]
output = Path(args[args.index("-o") + 1])
url = next(value for value in args if value.startswith("https://"))
if url.endswith("/latest"):
    output.write_text(json.dumps({"tag_name": "v2026.11.0", "draft": False, "prerelease": False}))
elif url.endswith("/SHASUMS256.txt"):
    shutil.copy(os.environ["FIXTURE_CHECKSUMS"], output)
else:
    shutil.copy(os.environ["FIXTURE_RELEASE"], output)
""",
        )

    def test_bootstrap_latest_and_rerun(self):
        self.isolate_bootstrap()
        for _ in range(2):
            result = self.run_setup("--accept-licenses")
            self.assertEqual(result.returncode, 0, result.stdout)
        self.assertEqual((self.root / ".local/bin/mise").read_text(), FAKE_MISE)
        self.assertEqual(list((self.root / ".local/bin").glob(".mise-*")), [])

    def test_bootstrap_checksum_failure(self):
        self.isolate_bootstrap(corrupt=True)
        result = self.run_setup("--accept-licenses")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("checksum verification failed", result.stdout)
        self.assertFalse((self.root / ".local/bin/mise").exists())
        self.assertNotIn("Setup complete", result.stdout)

    def test_property_repair_flag(self):
        properties = self.root / "local.properties"
        properties.write_text("sdk.dir=/old/sdk\nother=keep\n")
        result = self.run_setup("--accept-licenses")
        self.assertNotEqual(result.returncode, 0)
        result = self.run_setup("--accept-licenses", "--repair-sdk-config")
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("other=keep", properties.read_text())
        self.assertEqual(len(list(self.root.glob("local.properties.backup-*"))), 1)


if __name__ == "__main__":
    unittest.main()
