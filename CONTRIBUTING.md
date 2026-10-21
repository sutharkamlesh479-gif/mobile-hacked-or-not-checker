# Contributing

Thanks for helping improve Mobile Hacked or Not Checker.

## Before opening a change

1. Explain the problem and the expected behavior.
2. Keep changes focused and readable.
3. Avoid adding package names to detection lists without a credible, verifiable source.
4. Treat findings as indicators, not definitive malware verdicts.
5. Never include real device logs, serial numbers, personal data, credentials, or private network details.

## Local checks

- Use Python 3.
- Confirm the script parses: `python -m py_compile mobile-hacked-checker.python`
- If ADB and a test device are available, test device listing and scanning on a device you own or are authorized to assess.
- Do not run destructive commands as part of tests.

## Pull requests

Describe what changed, why it is needed, how it was tested, and any Android-version limitations. Clearly label checks that have not been tested on a real device.
