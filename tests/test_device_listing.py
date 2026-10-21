import contextlib
import importlib.machinery
import importlib.util
import io
from pathlib import Path
import subprocess
import unittest
from unittest.mock import patch


SOURCE = Path(__file__).resolve().parents[1] / "mobile-hacked-checker.python"
LOADER = importlib.machinery.SourceFileLoader("mobile_hacked_checker", str(SOURCE))
SPEC = importlib.util.spec_from_loader(LOADER.name, LOADER)
scanner_module = importlib.util.module_from_spec(SPEC)
LOADER.exec_module(scanner_module)


class ListDevicesTests(unittest.TestCase):
    @patch.object(scanner_module.subprocess, "run")
    def test_lists_only_authorized_devices(self, run_mock):
        run_mock.return_value = subprocess.CompletedProcess(
            ["adb", "devices"], 0,
            "List of devices attached\nABC123\tdevice\nXYZ999\tunauthorized\n", ""
        )
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            scanner_module.list_devices()
        self.assertIn("Authorized device: ABC123", output.getvalue())
        self.assertNotIn("Authorized device: XYZ999", output.getvalue())
        run_mock.assert_called_once_with(
            ["adb", "devices"], capture_output=True, text=True, timeout=15, check=False
        )

    @patch.object(scanner_module.subprocess, "run", side_effect=FileNotFoundError("adb missing"))
    def test_handles_missing_adb(self, run_mock):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            scanner_module.list_devices()
        self.assertIn("Could not run ADB", output.getvalue())


if __name__ == "__main__":
    unittest.main()
