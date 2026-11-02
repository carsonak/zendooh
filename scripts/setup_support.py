"""Standard-library helpers for setup.sh; no third-party Python packages required."""

import ctypes
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import shutil
import stat
import sys
import tempfile
import xml.etree.ElementTree as ET


def fail(message):
    raise RuntimeError(message)


def host_platform():
    host = (platform.system(), platform.machine())
    supported = {
        ("Linux", "x86_64"): "linux-x64",
        ("Darwin", "x86_64"): "macos-x64",
        ("Darwin", "arm64"): "macos-arm64",
    }
    if host not in supported:
        fail(
            "Unsupported host: %s %s. Use Linux/WSL x86-64 or macOS x86-64/arm64."
            % host
        )
    return supported[host]


def preflight():
    host_platform()
    if sys.version_info < (3, 9):
        fail(
            "Python 3.9 or newer is required. Install host prerequisites from CONTRIBUTING.md."
        )
    if platform.system() == "Linux":
        missing = []
        for library in (
            "libc.so.6",
            "libstdc++.so.6",
            "libz.so.1",
            "libX11.so.6",
            "libXext.so.6",
            "libXi.so.6",
            "libXrender.so.1",
            "libXtst.so.6",
            "libfontconfig.so.1",
            "libfreetype.so.6",
            "libGL.so.1",
        ):
            try:
                ctypes.CDLL(library)
            except OSError:
                missing.append(library)
        if missing:
            fail(
                "Missing native libraries: "
                + ", ".join(missing)
                + ". Install host prerequisites from CONTRIBUTING.md and rerun; setup never uses sudo."
            )
    # Check the closest existing ancestor before installing anything.
    data_home = Path(os.environ.get("XDG_DATA_HOME", str(Path.home() / ".local/share")))
    cache_home = Path(
        os.environ.get(
            "XDG_CACHE_HOME",
            str(
                Path.home()
                / ("Library/Caches" if platform.system() == "Darwin" else ".cache")
            ),
        )
    )
    for value in (
        os.environ.get("MISE_DATA_DIR", str(data_home / "mise")),
        os.environ.get("MISE_CACHE_DIR", str(cache_home / "mise")),
        os.environ.get("GRADLE_USER_HOME", str(Path.home() / ".gradle")),
    ):
        target = Path(value).expanduser().absolute()
        while not target.exists():
            target = target.parent
        if not target.is_dir() or not os.access(target, os.W_OK | os.X_OK):
            fail("Installation directory is not writable: " + str(target))


def version(minimum, installed):
    match = re.match(r"(\d+)\.(\d+)\.(\d+)(?:\s|$)", installed)
    if not match or tuple(map(int, match.groups())) < tuple(
        map(int, minimum.split("."))
    ):
        fail(
            "Installed mise is unsupported. Upgrade mise to at least "
            + minimum
            + " and rerun; setup leaves it unchanged."
        )


def checksum(binary, asset, manifest):
    matches = []
    for line in Path(manifest).read_text().splitlines():
        fields = line.split()
        if len(fields) == 2 and fields[1].removeprefix("./") == asset:
            matches.append(fields[0])
    if (
        len(matches) != 1
        or hashlib.sha256(Path(binary).read_bytes()).hexdigest() != matches[0]
    ):
        fail("Mise release checksum verification failed; the binary was not installed.")


def equivalent(left, right):
    return Path(left).resolve() == Path(right).resolve()


def sdk_environment(sdk, android_home, android_root):
    for name, value in (
        ("ANDROID_HOME", android_home),
        ("ANDROID_SDK_ROOT", android_root),
    ):
        if value and not equivalent(value, sdk):
            fail(
                name
                + " conflicts with the mise SDK. Unset it before running setup; use mise activation or mise exec afterward."
            )


def unescape(value):
    def replace(match):
        value = match.group(1)
        if value.startswith("u"):
            if not re.fullmatch(r"u[\da-fA-F]{4}", value):
                fail(
                    "Malformed Unicode escape in local.properties; correct it before setup."
                )
            return chr(int(value[1:], 16))
        return {"t": "\t", "n": "\n", "r": "\r", "f": "\f"}.get(value, value)

    decoded = re.sub(r"\\(u.{0,4}|.)", replace, value)
    return decoded.encode("utf-16", "surrogatepass").decode("utf-16")


def property_records(content):
    """Yield original records plus decoded keys/values, including continuations."""
    lines = iter(re.findall(r"[^\r\n]*(?:\r\n|\r|\n|$)", content))
    for line in lines:
        raw = line
        if line.lstrip(" \t\f").startswith(("#", "!")):
            yield raw, None, None
            continue
        logical = line.rstrip("\r\n")
        while (len(logical) - len(logical.rstrip("\\"))) % 2:
            following = next(lines, "")
            raw += following
            logical = logical[:-1] + following.lstrip(" \t\f").rstrip("\r\n")
            if not following:
                break
        text = logical.lstrip(" \t\f")
        if not text or text.startswith(("#", "!")):
            yield raw, None, None
            continue
        end = 0
        while end < len(text):
            if text[end] == "\\":
                end += 2
            elif text[end] in "=: \t\f":
                break
            else:
                end += 1
        key = unescape(text[:end])
        value = text[end:].lstrip(" \t\f")
        if value.startswith(("=", ":")):
            value = value[1:].lstrip(" \t\f")
        yield raw, key, unescape(value)


def escape_path(value):
    # ASCII-only Java Properties representation also handles Unicode user paths.
    result = []
    for char in value:
        if char in "\\ :=#!":
            result.append("\\" + char)
        elif ord(char) < 32 or ord(char) > 126:
            units = char.encode("utf-16-be")
            result.extend(
                "\\u%04x" % int.from_bytes(units[i : i + 2], "big")
                for i in range(0, len(units), 2)
            )
        else:
            result.append(char)
    return "".join(result)


def sdk_config(sdk, repair, path=Path("local.properties")):
    if not path.exists():
        return
    original = path.read_bytes()
    records = list(property_records(original.decode("latin-1")))
    values = [value for _, key, value in records if key == "sdk.dir"]
    if not values or all(equivalent(value, sdk) for value in values):
        return
    if not repair:
        if not sys.stdin.isatty():
            fail(
                "local.properties sdk.dir conflicts with the mise SDK. Rerun interactively or pass --repair-sdk-config to back up and replace sdk.dir."
            )
        answer = input(
            "local.properties sdk.dir conflicts. Back up the file and replace sdk.dir with the mise SDK? [y/N] "
        )
        if answer.strip().lower() not in ("y", "yes"):
            fail("SDK configuration repair declined; local.properties is unchanged.")
    if path.is_symlink():
        fail("Cannot repair a symlinked local.properties. Update its target manually.")
    newline = "\r\n" if b"\r\n" in original else "\n"
    updated = []
    replaced = False
    for raw, key, _ in records:
        if key == "sdk.dir":
            if not replaced:
                updated.append(
                    "sdk.dir=" + escape_path(str(Path(sdk).resolve())) + newline
                )
                replaced = True
        else:
            updated.append(raw)
    # Both files stay alongside the original; backups never overwrite a prior backup.
    backup_fd, backup_name = tempfile.mkstemp(
        prefix=path.name + ".backup-", dir=path.parent
    )
    with os.fdopen(backup_fd, "wb") as backup:
        backup.write(original)
        backup.flush()
        os.fsync(backup.fileno())
    temp_fd, temp_name = tempfile.mkstemp(prefix=".setup-properties-", dir=path.parent)
    try:
        with os.fdopen(temp_fd, "wb") as output:
            output.write("".join(updated).encode("latin-1"))
            output.flush()
            os.fsync(output.fileno())
        os.chmod(temp_name, stat.S_IMODE(path.stat().st_mode))
        if path.read_bytes() != original:
            fail("local.properties changed during setup; refusing to overwrite it.")
        os.replace(temp_name, path)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)
    print("Updated sdk.dir; original saved as " + str(backup_name))


def verify_sdk():
    sdk = Path(os.environ["ANDROID_HOME"]).resolve()
    for command in ("sdkmanager", "adb", "apksigner"):
        executable = shutil.which(command)
        if executable is None or sdk not in Path(executable).resolve().parents:
            fail(command + " does not resolve inside the selected SDK.")
        print(command + ": " + executable)
    for package in os.environ["ZENDOOH_ANDROID_PACKAGES"].split():
        directory = sdk.joinpath(*package.split(";"))
        manifest = directory / "package.xml"
        if not manifest.is_file():
            fail("SDK package is missing or incomplete: " + package)
        tree = ET.parse(manifest)
        if not any(
            node.tag.split("}")[-1] == "localPackage" and node.get("path") == package
            for node in tree.iter()
        ):
            fail("SDK package metadata does not match: " + package)


def main():
    command, *args = sys.argv[1:]
    if command == "platform":
        print(host_platform())
    elif command == "preflight":
        preflight()
    elif command == "version":
        version(*args)
    elif command == "release":
        release = json.loads(Path(args[0]).read_text())
        tag = release.get("tag_name", "")
        if (
            release.get("draft")
            or release.get("prerelease")
            or not re.fullmatch(r"v\d+\.\d+\.\d+", tag)
        ):
            fail("Could not resolve a stable mise release.")
        print(tag)
    elif command == "checksum":
        checksum(*args)
    elif command == "sdk-environment":
        sdk_environment(*args)
    elif command == "sdk-config":
        sdk_config(args[0], args[1] == "true")
    elif command == "verify-sdk":
        verify_sdk()
    else:
        fail("Unknown setup helper command: " + command)


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, OSError, ValueError, ET.ParseError) as error:
        print("Setup: " + str(error), file=sys.stderr)
        sys.exit(1)
