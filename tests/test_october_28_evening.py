"""October 28 Evening source-audited scout writer → blind ping reader and heredity gate."""
import unittest
from pathlib import Path
from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]
PASS = "october-28-evening-scout-wave-read-write-heredity"
EVIDENCE = {"oct28-evening-order-ping-reader-beats-mean", "oct28-evening-recency-ping-fails-scalar", "oct28-evening-inheritance-converges-to-seek"}

class EveningPassTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a = load_atlas(ROOT)
        cls.nodes = {n["id"]: n for n in cls.a["nodes"]}
        cls.edges = {(e["source"], e["target"], e["type"]) for e in cls.a["edges"]}
        cls.receipts = {e["id"]: e for e in cls.a["evidence"]}

    def test_census_and_pass_are_unique(self):
        self.assertEqual(validate_atlas(self.a), [])
        self.assertEqual([r["name"] for r in self.a["repos"]].count("Evening"), 1)
        self.assertEqual(len(self.a["repos"]), 550)
        self.assertEqual(self.nodes["Evening"]["pass_id"], PASS)
        self.assertEqual(len([n for n in self.a["nodes"] if n["id"] == "Evening"]), 1)

    def test_distinct_contributions_and_corrected_claims(self):
        self.assertIn(("BlackBoxLab", "Evening", "inherits"), self.edges)
        self.assertIn(("WallMemoryLaw", "Evening", "converges"), self.edges)
        self.assertNotIn(("WallMemoryLaw", "Evening", "inherits"), self.edges)
        self.assertIn("0/8", self.nodes["Evening"]["killed"])
        self.assertIn("pixel-shuffling", self.nodes["Evening"]["survived"])

    def test_results_not_overclaimed(self):
        self.assertTrue(EVIDENCE.issubset(self.receipts))
        self.assertEqual(self.receipts["oct28-evening-order-ping-reader-beats-mean"]["sample"]["count"], 48)
        self.assertEqual(self.receipts["oct28-evening-recency-ping-fails-scalar"]["result"], "contradicts")
        self.assertEqual(self.receipts["oct28-evening-inheritance-converges-to-seek"]["result"], "contradicts")
        self.assertIn("oct28-can-scout-ping-code-hold-two-lineages", {q["id"] for q in self.a["questions"]})

    def test_visible_page_and_review(self):
        html = (ROOT/"index.html").read_text(encoding="utf-8")
        readme = (ROOT/"README.md").read_text(encoding="utf-8")
        self.assertIn('id="oct28-evening"', html)
        self.assertIn('data-mad-node="Evening"', html)
        self.assertIn("550", readme)
        self.assertTrue((ROOT/"docs/reviews/2026-10-28-evening-read-write-heredity.md").is_file())

if __name__ == "__main__":
    unittest.main()
