from pathlib import Path
import unittest
from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]
PASS_ID = "october-17-two-babies-state-and-navigation"

class TwoBabiesPassTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.atlas = load_atlas(ROOT)

    def test_atlas_valid(self):
        self.assertEqual(validate_atlas(self.atlas), [])

    def test_two_distinct_reviewed_nodes_and_no_duplicate_sihti2(self):
        nodes = self.atlas["nodes"]
        inventory = {r["name"]: r for r in self.atlas["repos"]}
        for name in ("SolsBaby", "ClaudesBaby"):
            matching = [n for n in nodes if n["id"] == name]
            self.assertEqual(len(matching), 1)
            self.assertEqual(matching[0]["pass_id"], PASS_ID)
            self.assertEqual(inventory[name]["inventory_status"], "reviewed")
            self.assertTrue(matching[0]["killed"])
        self.assertEqual(sum(n["id"] == "SihtiImageModel2" for n in nodes), 1)

    def test_failures_and_controls_remain_visible(self):
        nodes = {n["id"]: n for n in self.atlas["nodes"]}
        self.assertIn("168 bytes", nodes["SolsBaby"]["killed"])
        self.assertIn("G3", nodes["ClaudesBaby"]["killed"])
        self.assertIn("G4b", nodes["ClaudesBaby"]["killed"])
        ev = {r["id"]:r for r in self.atlas["evidence"]}
        for eid in ("oct17-solsbaby-frozen-writer", "oct17-claudesbaby-map-grid",
                    "oct17-claudesbaby-gate-failures"):
            self.assertTrue(ev[eid]["controls"])
            self.assertTrue(ev[eid]["limitations"])
        self.assertEqual(ev["oct17-claudesbaby-gate-failures"]["result"], "contradicts")

if __name__ == "__main__":
    unittest.main()
