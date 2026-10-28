"""Exercise non-destructive installs and standalone prompt generation."""

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from build import render
from install import install, package_files


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.target = self.base / "skills" / "im-poetry"

    def test_install_is_complete_and_does_not_copy_development_files(self):
        install(ROOT, self.target)
        self.assertEqual(package_files(ROOT), package_files(self.target))
        self.assertFalse((self.target / "scripts").exists())
        self.assertFalse((self.target / "README.md").exists())

    def test_second_install_is_idempotent(self):
        install(ROOT, self.target)
        self.assertIn("Already current", install(ROOT, self.target))

    def test_different_existing_skill_is_untouched(self):
        self.target.mkdir(parents=True)
        file = self.target / "SKILL.md"
        file.write_text("my existing skill", encoding="utf-8")
        with self.assertRaises(FileExistsError):
            install(ROOT, self.target)
        self.assertEqual(file.read_text(), "my existing skill")

    def test_extra_user_file_prevents_overwrite(self):
        install(ROOT, self.target)
        (self.target / "notes.txt").write_text("keep me")
        with self.assertRaises(FileExistsError):
            install(ROOT, self.target)
        self.assertEqual((self.target / "notes.txt").read_text(), "keep me")

    def test_dry_run_creates_nothing(self):
        install(ROOT, self.target, dry_run=True)
        self.assertEqual(list(self.base.iterdir()), [])

    def test_target_symlink_is_not_followed(self):
        other = self.base / "other"
        other.mkdir()
        self.target.parent.mkdir()
        self.target.symlink_to(other, target_is_directory=True)
        with self.assertRaises(FileExistsError):
            install(ROOT, self.target)
        self.assertEqual(list(other.iterdir()), [])

    def test_cli_project_locations(self):
        for target, directory in (
            ("claude", ".claude"), ("gemini", ".gemini"), ("codex", ".agents")
        ):
            completed = subprocess.run(
                [sys.executable, str(ROOT / "scripts/install.py"), "--target", target,
                 "--project", str(self.base)], text=True, capture_output=True
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertTrue((self.base / directory / "skills/im-poetry/SKILL.md").is_file())

    def test_conflicting_cli_options_fail(self):
        completed = subprocess.run(
            [sys.executable, str(ROOT / "scripts/install.py"), "--destination",
             str(self.target), "--project", str(self.base)], capture_output=True
        )
        self.assertNotEqual(completed.returncode, 0)
        self.assertFalse(self.target.exists())


class PromptTests(unittest.TestCase):
    def test_removes_only_frontmatter_and_native_reference_block(self):
        text = "---\nname: example\n---\n\nKeep me.\n<!-- portable:omit:start -->\nNative only\n<!-- portable:omit:end -->\nKeep this too.\n"
        self.assertEqual(render(text), "Keep me.\nKeep this too.\n")

    def test_malformed_omission_is_rejected(self):
        for tail in ("<!-- portable:omit:start -->", "<!-- portable:omit:end -->"):
            with self.assertRaises(ValueError):
                render("---\nname: example\n---\n" + tail)

    def test_native_and_standalone_share_protected_examples(self):
        prompt = render((ROOT / "SKILL.md").read_text(encoding="utf-8"))
        for phrase in ("원인을 찾으려 했다", "실패할 수도 있다", "지금 검토하고 있다"):
            self.assertIn(phrase, prompt)
        self.assertNotIn("references/", prompt)
        self.assertLessEqual(len(prompt), 8000)


if __name__ == "__main__":
    unittest.main()
