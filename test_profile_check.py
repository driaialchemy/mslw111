import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from profile_check import validate_profile_readme


class ProfileCheckTests(unittest.TestCase):
    def test_valid_profile_readme_passes(self):
        with TemporaryDirectory() as tmp:
            readme = Path(tmp) / "README.md"
            readme.write_text("AI prompt engineering and data analysis", encoding="utf-8")

            self.assertEqual(validate_profile_readme(readme), [])

    def test_missing_required_terms_fails(self):
        with TemporaryDirectory() as tmp:
            readme = Path(tmp) / "README.md"
            readme.write_text("hello", encoding="utf-8")

            problems = validate_profile_readme(readme)

        self.assertTrue(problems)
        self.assertIn("README is missing profile terms", problems[0])


if __name__ == "__main__":
    unittest.main()
