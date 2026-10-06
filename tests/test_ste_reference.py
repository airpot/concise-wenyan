import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "ste_reference.py"


class ReferenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location("ste_reference", SCRIPT)
        cls.ref = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.ref)

    def test_unavailable_source_is_not_a_pass(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(FileNotFoundError):
                self.ref.ensure_pdf(Path(directory), download=False)

    def test_corrupt_cached_source_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / self.ref.PDF_NAME
            path.write_bytes(b"%PDF-1.7\nwrong source")
            with self.assertRaises(ValueError):
                self.ref.ensure_pdf(Path(directory), download=False)

    def test_exact_headword_not_substring_or_alternative(self):
        rows = [
            {"word": "TEST", "pos": "n", "approved": True},
            {"word": "test", "pos": "v", "approved": False},
            {"word": "CONTEST", "pos": "n", "approved": False},
        ]
        result = self.ref.match_entries(rows, "test")
        self.assertEqual(len(result), 2)
        self.assertEqual([r["approved"] for r in result], [True, False])
        self.assertEqual(self.ref.match_entries(rows, "tes"), [])

    def test_all_sections_and_dictionary_introduction_have_ranges(self):
        self.assertEqual(set(self.ref.SECTIONS), {str(i) for i in range(1, 10)} | {"dictionary-intro"})
        for first, last in self.ref.SECTIONS.values():
            self.assertLessEqual(first, last)
            self.assertGreater(first, 0)

    def test_lookup_live_official_rows(self):
        # Integration with the verified private cache, never a network test.
        cache = Path.home() / ".cache" / "concise-wenyan"
        if not (cache / self.ref.PDF_NAME).exists():
            self.skipTest("No official PDF in the private cache")
        pdf = self.ref.ensure_pdf(cache, download=False)
        rows = self.ref.dictionary_entries(pdf)
        test = self.ref.match_entries(rows, "test")
        self.assertTrue(any(r["approved"] and r["pos"] == "n" for r in test))
        self.assertTrue(any(not r["approved"] and r["pos"] == "v" for r in test))
        acceptable = self.ref.match_entries(rows, "acceptable")
        self.assertTrue(any(not r["approved"] and r["pos"] == "adj" for r in acceptable))
        # Some PDF lines merge the headword and meaning into one text span.
        mandatory = self.ref.match_entries(rows, "mandatory")
        self.assertTrue(any(r["approved"] and r["pos"] == "adj" for r in mandatory))
        provided = self.ref.match_entries(rows, "provided (that)")
        self.assertTrue(any(not r["approved"] and r["pos"] == "conj" for r in provided))
        prefix = self.ref.match_entries(rows, "re-")
        self.assertTrue(any(r["pos"] == "prefix" for r in prefix))
        wear = self.ref.match_entries(rows, "wear")
        self.assertTrue(any(r["approved"] and "friction" in r["text"].lower() for r in wear))
        self.assertEqual(self.ref.match_entries(rows, "qzx_nonexistent_word"), [])
        with self.ref.open_pdf(pdf) as document:
            first, last = self.ref.SECTIONS["9"]
            text = "\n".join(document[n - 1].get_text() for n in range(first, last + 1))
            for number in range(1, 9):
                self.assertIn(f"GR-{number}", text)


if __name__ == "__main__":
    unittest.main()
