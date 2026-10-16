from pathlib import Path
import unittest

from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]
PASS_ID = "october-16-sihti-image-and-growth-microscope"
REPOS = ("SihtiImageModel", "Growth-Microscope")
EVIDENCE = ['oct16-sihti-representation-classification','oct16-sihti-whole-memory-generator','oct16-sihti-patch-translation','oct16-sihti-natural-photo-and-defect-limits','oct16-growth-gate1-explanation-controls','oct16-growth-gate2-prospective-selection','oct16-growth-gate3-discovered-groups-null']

class OctoberSixteenPassTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.atlas = load_atlas(ROOT)

    def test_atlas_invariants(self):
        self.assertEqual(validate_atlas(self.atlas), [])

    def test_both_repos_are_reviewed_and_unique(self):
        nodes = self.atlas["nodes"]
        repos = {r["name"]: r for r in self.atlas["repos"]}
        for name in REPOS:
            cards = [n for n in nodes if n["id"] == name]
            self.assertEqual(len(cards), 1)
            self.assertEqual(cards[0]["pass_id"], PASS_ID)
            self.assertEqual(repos[name]["inventory_status"], "reviewed")

    def test_evidence_has_controls_and_limits(self):
        evidence = {e["id"]: e for e in self.atlas["evidence"]}
        for evidence_id in EVIDENCE:
            self.assertIn(evidence_id, evidence)
            self.assertTrue(evidence[evidence_id]["controls"])
            self.assertTrue(evidence[evidence_id]["limitations"])

    def test_negative_results_remain_visible(self):
        cards = {n["id"]: n for n in self.atlas["nodes"]}
        self.assertIn("0.53 dB", cards["SihtiImageModel"]["killed"])
        self.assertIn("never the best", cards["Growth-Microscope"]["killed"])
        questions = {q["id"]: q for q in self.atlas["questions"]}
        self.assertEqual(questions["oct16-online-temporal-residue-restoration"]["state"], "open")
        self.assertEqual(questions["oct16-causal-groups-transfer-versus-physics"]["state"], "open")

if __name__ == "__main__":
    unittest.main()
