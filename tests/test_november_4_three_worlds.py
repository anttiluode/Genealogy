"""November 4 new worlds: three reviewed arrivals, distinct mechanisms, and honest controls."""
import unittest
from pathlib import Path
from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]
PASS = "november-4-environments-index-and-emergent-geometry"
NAMES = {"SelfIndexingBeach", "EmergenceNoSpace", "Emergence3D"}

class NewWorldsNovember4(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.atlas = load_atlas(ROOT)

    def test_inventory_and_pass(self):
        self.assertEqual(validate_atlas(self.atlas), [])
        self.assertGreaterEqual(len(self.atlas["repos"]), 584)
        self.assertEqual({x["id"] for x in self.atlas["nodes"] if x.get("pass_id") == PASS}, NAMES)
        for name in NAMES:
            self.assertEqual(sum(x["name"] == name for x in self.atlas["repos"]), 1)
            self.assertEqual(sum(x["id"] == name for x in self.atlas["nodes"]), 1)
            self.assertEqual(next(x for x in self.atlas["repos"] if x["name"] == name)["inventory_status"],"reviewed")

    def test_distinct_claims_and_controls(self):
        nodes = {x["id"]: x for x in self.atlas["nodes"]}
        self.assertIn("external", nodes["SelfIndexingBeach"]["killed"])
        self.assertIn("0.000476",nodes["SelfIndexingBeach"]["survived"])
        self.assertIn("degree-preserving",nodes["EmergenceNoSpace"]["killed"].lower())
        self.assertIn("not emergent",nodes["Emergence3D"]["killed"].lower())
        self.assertIn("a 3d",nodes["Emergence3D"]["claim"].lower())

    def test_ancestry_and_wall(self):
        edges=[x for x in self.atlas["edges"] if x.get("pass_id")==PASS]
        self.assertTrue(any(x["source"]=="Emergence" and x["target"]=="Emergence3D" and x["type"]=="inherits" for x in edges))
        self.assertFalse(any(x["source"]=="Emergence3D" and x["target"]=="EmergenceNoSpace" and x["type"]=="forks" for x in edges))
        wall=(ROOT/"index.html").read_text(encoding="utf-8")
        self.assertIn('id="nov4-three-worlds"',wall)
        for name in NAMES:self.assertIn('data-mad-node="'+name+'"',wall)
        self.assertTrue((ROOT/"docs/reviews/2026-11-04-three-worlds-prediction-and-geometry.md").is_file())

if __name__ == "__main__":
    unittest.main()
