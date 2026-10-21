# Mobile Hacked or Not Checker

A Python-based **Android security inspection tool** that uses Android Debug Bridge (ADB) to collect device information and look for selected indicators that may warrant further investigation.

> **Important:** This project is experimental. Its findings are indicators—not proof—that a device is compromised. It may produce false positives or miss threats. Do not use it as a replacement for a trusted mobile-security product or a professional incident-response review.

## Features

- Connects to an Android device through ADB.
- Collects selected device and Android configuration information.
- Checks selected indicators that may be relevant to a security review.
- Intended for defensive inspection of devices you own or are explicitly authorized to assess.

## Requirements

- Python 3 installed on your computer.
- Android Debug Bridge (ADB) installed and available on your PATH.
- An Android device and a USB data cable.
- USB debugging enabled in Android Developer options.
- A Linux environment such as Kali Linux may be used, but is not a security requirement of ADB itself.

## Setup

1. Install Python 3 and ADB using the instructions for your operating system.
2. On your Android device, enable **Developer options** and then **USB debugging**.
3. Connect the device by USB and approve the debugging authorization prompt on the device.
4. Verify that ADB can see the device:

   ```bash
   adb devices
   ```

   Confirm that your device appears with the status `device`. If it shows `unauthorized`, unlock the phone and approve the prompt.

## Run

From the folder containing the project file:

```bash
python mobile-hacked-checker.python
```

If the script has a different filename in your local copy, substitute that filename. Review the script before running it, and follow any additional dependencies or prompts it documents.

## Interpreting results

- Treat every warning as a lead to investigate, not a definitive malware verdict.
- Package names, network activity, debugging settings, and system logs can be normal on legitimate devices.
- Confirm suspicious findings using reliable sources and multiple independent checks.
- A clean result does **not** guarantee that a device is malware-free.

## Safety and privacy

- Run checks only on devices you own or have explicit permission to inspect.
- Review the code before use and understand what information it collects.
- Avoid publishing logs that contain personal information, device identifiers, network details, or other sensitive data.
- This project is provided for educational and defensive security purposes.

## Current status

This is a learning project and should be considered a work in progress. Test it on supported Android versions and document verified behavior before relying on it for security decisions.

## Author

**Kamlesh Suthar**

---

*Learn. Build. Test responsibly.*

## Project documentation

- [Security policy](SECURITY.md) — safe use, privacy, and reporting guidance.
- [Contributing guide](CONTRIBUTING.md) — how to propose and test changes.
- [Changelog](CHANGELOG.md) — notable project updates.
- [Python checks workflow](.github/workflows/python-checks.yml) — checks that the scanner source parses on pushes and pull requests.

## Development status

Automated CI checks Python syntax only. They do not verify detection accuracy or replace testing with a real Android device. No real-device compatibility claim is made without testing evidence.
