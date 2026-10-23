"""October 22: mixed positive/negative visual learning entries are preserved."""
import unittest
from pathlib import Path
from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]
PID = "october-22-living-paper-conjunctions-and-visual-transfer"

class VisualLearningOct22Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.atlas = load_atlas(ROOT)

    def test_pass_and_inventory(self):
        self.assertEqual(validate_atlas(self.atlas), [])
        self.assertIn(PID, {p["id"] for p in self.atlas["passes"]})
        wanted = {"SihtiImageModel5", "ClaudeRepo1", "ModelImage"}
        self.assertEqual({n["id"] for n in self.atlas["nodes"] if n.get("pass_id") == PID}, wanted)
        self.assertEqual({r["name"] for r in self.atlas["repos"] if r["name"] in wanted}, wanted)
        for r in self.atlas["repos"]:
            if r["name"] in wanted:
                self.assertEqual(r["inventory_status"], "reviewed")

    def test_survivals_and_kills_are_separate(self):
        nodes = {n["id"]:n for n in self.atlas["nodes"]}
        self.assertIn("0.980", nodes["SihtiImageModel5"]["killed"])
        self.assertIn("chelsea", nodes["ClaudeRepo1"]["killed"])
        self.assertIn("20/20", nodes["ClaudeRepo1"]["survived"])
        self.assertIn("0.00916", nodes["ModelImage"]["killed"])
        evidence = {e["id"]:e for e in self.atlas["evidence"]}
        self.assertEqual(evidence["oct22-modelimage-v3-natural-transfer-negative"]["result"], "contradicts")
        self.assertEqual(evidence["oct22-claude-selfpredictive-branch-discovery"]["result"], "supports")
        self.assertEqual(evidence["oct22-model5-full-h3-and-h1b-fail"]["result"], "contradicts")
        self.assertGreaterEqual(len([e for e in evidence.values() if e["id"].startswith("oct22-")]), 8)

if __name__ == "__main__":
    unittest.main()
