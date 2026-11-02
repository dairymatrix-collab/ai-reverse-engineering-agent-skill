import json
import pathlib
import subprocess
import sys
import tempfile
import unittest


SCRIPT = pathlib.Path(__file__).resolve().parents[1] / "scripts" / "create_manifest.py"


class CreateManifestTests(unittest.TestCase):
    def test_directory_manifest_excludes_external_symlinks(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            base = pathlib.Path(temporary_directory)
            target = base / "target"
            target.mkdir()
            inside = target / "inside.txt"
            inside.write_text("inside", encoding="utf-8")
            outside = base / "outside.txt"
            outside.write_text("outside", encoding="utf-8")

            try:
                (target / "inside-link.txt").symlink_to(inside)
                (target / "outside-link.txt").symlink_to(outside)
            except (NotImplementedError, OSError) as error:
                self.skipTest(f"file symlinks are unavailable: {error}")

            output = base / "manifest.json"
            subprocess.run(
                [sys.executable, str(SCRIPT), str(target), "-o", str(output)],
                check=True,
                capture_output=True,
                text=True,
            )
            paths = {item["path"] for item in json.loads(output.read_text(encoding="utf-8"))["files"]}

            self.assertIn("inside.txt", paths)
            self.assertIn("inside-link.txt", paths)
            self.assertNotIn("outside-link.txt", paths)


if __name__ == "__main__":
    unittest.main()
