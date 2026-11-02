# Android development delivery

This procedure uses fictional data only. It does not establish real-data readiness. The
application ID is `com.zendooh.app`, minimum API 24, target API 36. The current launcher
displays Zendooh; no ledger or SMS acquisition exists yet.

## Build and signing custody

Run `mise install`, configure the SDK as described in [CONTRIBUTING](../CONTRIBUTING.md),
then run `mise run build`. The debug artifact is
`androidApp/build/outputs/apk/debug/androidApp-debug.apk`.

Android's debug signing key normally lives in the developer's `.android` directory. Keep
that directory outside Git and preserve the same key for development updates. A fresh
environment can create a different key: do not assume two debug APKs share a signer. Do
not send keys, passwords or private financial records to an agent. The debug key is
suitable for fictional-data development only; establish a separately custodied release
identity before distributing a beta.

Before handing over an APK, use the SDK build-tools `apksigner verify --print-certs`
command on it and record its SHA-256 certificate fingerprint privately alongside the
artifact checksum (`sha256sum`). Verify the signature and compare the certificate with the
previous accepted build before an update. Back up the signing key through a private,
access-controlled channel independent of this checkout. Losing the key prevents an
in-place update of the same application ID. Never uninstall to resolve a signature
mismatch when data must be preserved; stop and recover the original signer instead.

## Install and update

Enable developer options and USB debugging on the test phone, connect by USB, and approve
the host on the phone. Use a dedicated emulator or a phone containing fictional test data.
Run the [development setup](../CONTRIBUTING.md#development-environment) to install
platform-tools. Select the exact device serial from `mise exec -- adb devices`, then run:

```sh
mise exec -- adb -s SERIAL install -r androidApp/build/outputs/apk/debug/androidApp-debug.apk
mise run launch:android SERIAL
```

The launch task opens the installed app and waits for activity launch completion. It does
not build or install an APK.

Replace `SERIAL` with the intended device. `-r` preserves app data for a compatible signed
update. A failed install must be investigated; uninstalling clears application data. Do
not collect device-wide logs, inboxes, screenshots or account details for agent review.
Report only synthetic reproductions and non-sensitive pass/fail results.

## Android execution and phone checklist

No emulator is needed for `mise run test`, which currently runs only the desktop Compose
smoke test. Android assembly and lint do not execute the application. To verify Android
execution, provision an API 24+ emulator using Android Studio Device Manager, boot it, and
perform the install/launch steps above. An API 36 emulator is useful for the target SDK;
also check a minimum-supported API before claiming broad compatibility. Record OS/API,
build revision, installation result and visible title without private device identifiers.
Instrumentation tests will be added with the platform behavior they verify; there is no
instrumented test suite at this stage.

Reference phone: Redmi 15C, HyperOS 3.0, Android 16, dual SIM. When available:

- Install the fictional-data build and confirm the Zendooh title appears without a crash.
- Close/reopen and rotate; check large system text, light/dark appearance and TalkBack.
- Install the next build over the existing one using the same signer; confirm launch.
- Record failures using fictional examples and sanitized descriptions only.

H01 remains pending until phase 02 supplies a useful manual-ledger journey. Its checklist
must then include account creation, exact amounts, editing, restart persistence and
visible history. SMS/SIM mapping, permission revocation, background restrictions and
portable recovery require their owning phases' tests; the title smoke test proves none of
these. Defer all real-data trials until H02 approval.
