from pathlib import Path
import unittest
from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]

class MobiusQwordPass(unittest.TestCase):
    def test_pass_is_valid_and_evidence_links_are_distinct(self):
        atlas = load_atlas(ROOT)
        self.assertEqual(validate_atlas(atlas), [])
        nodes = {n["id"]: n for n in atlas["nodes"]}
        self.assertEqual(nodes["Q-word"]["pass_id"], "mobius-qword-transfer")
        self.assertEqual(nodes["MovingTarget2"]["pass_id"], "moving-target-memory-worlds")
        self.assertIn(("MovingTarget2","Q-word","extracts"),
            {(e["source"],e["target"],e["type"]) for e in atlas["edges"]})
        records = {e["id"]: e for e in atlas["evidence"]}
        self.assertEqual(records["qword-mobius-out-of-family-transfer"]["result"], "contradicts")
        self.assertEqual(records["movingtarget2-mobius-odometer-and-shape"]["result"], "supports")
        self.assertEqual(records["qword-mobius-out-of-family-transfer"]["sample"]["count"], 3)
        self.assertEqual(records["movingtarget2-mobius-odometer-and-shape"]["sample"]["count"], 20)

if __name__ == "__main__":
    unittest.main()
