"""November 5 project genealogy: unique census rows, typed lineages, and evidence boundaries."""
import unittest
from pathlib import Path
from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]
PASS_ID = "november-5-vines-chains-and-garden-worlds"
NAMES = {"Emergence3DSol", "Koynnos", "PsychedelicGarden"}

class November5VinesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.atlas = load_atlas(ROOT)

    def test_census_and_reviewed_nodes(self):
        self.assertEqual(validate_atlas(self.atlas), [])
        self.assertGreaterEqual(len(self.atlas["repos"]), 587)
        self.assertEqual({n["id"] for n in self.atlas["nodes"] if n.get("pass_id") == PASS_ID}, NAMES)
        for name in NAMES:
            self.assertEqual(sum(r["name"] == name for r in self.atlas["repos"]), 1)
            self.assertEqual(sum(n["id"] == name for n in self.atlas["nodes"]), 1)
            self.assertEqual(next(r for r in self.atlas["repos"] if r["name"] == name)["inventory_status"], "reviewed")

    def test_edges_and_limits(self):
        edges = [e for e in self.atlas["edges"] if e.get("pass_id") == PASS_ID]
        self.assertTrue(any(e["source"] == "Emergence3D" and e["target"] == "Emergence3DSol" and e["type"] == "inherits" for e in edges))
        self.assertFalse(any(e["source"] == "Emergence3DSol" and e["target"] == "Koynnos" and e["type"] == "forks" for e in edges))
        nodes = {n["id"]: n for n in self.atlas["nodes"]}
        self.assertIn("No committed multi-seed", nodes["Emergence3DSol"]["killed"])
        self.assertIn("No measured real-GPU", nodes["PsychedelicGarden"]["killed"])
        wall = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn('id="nov5-vines-chains"', wall)
        for name in NAMES:
            self.assertIn('data-mad-node="' + name + '"', wall)
        self.assertTrue((ROOT / "docs/reviews/2026-11-05-vines-borrowed-support-and-game-worlds.md").is_file())

if __name__ == "__main__":
    unittest.main()
