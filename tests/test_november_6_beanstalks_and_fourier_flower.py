"""Regression checks for the November 5–6 Beanstalk and Fourier pass."""
import unittest
from pathlib import Path
from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]
PASS = "november-6-beanstalk-games-and-fourier-flower"
NAMES = {"SolAndTheBeanStalk", "SolAndTheBeanstalk2", "FourierFlower"}

class NewGameAndFlowerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.atlas = load_atlas(ROOT)

    def test_nodes_census_and_schema(self):
        self.assertEqual(validate_atlas(self.atlas), [])
        self.assertGreaterEqual(len(self.atlas["repos"]), 590)
        self.assertEqual({n["id"] for n in self.atlas["nodes"] if n.get("pass_id") == PASS}, NAMES)
        for name in NAMES:
            self.assertEqual(sum(r["name"] == name for r in self.atlas["repos"]), 1)
            self.assertEqual(sum(n["id"] == name for n in self.atlas["nodes"]), 1)
            self.assertEqual(next(r for r in self.atlas["repos"] if r["name"] == name)["inventory_status"], "reviewed")

    def test_provenance_and_wall(self):
        edges = {(e["source"], e["target"], e["type"]) for e in self.atlas["edges"] if e.get("pass_id") == PASS}
        self.assertIn(("Koynnos", "SolAndTheBeanStalk", "extracts"), edges)
        self.assertIn(("PsychedelicGarden", "SolAndTheBeanstalk2", "inherits"), edges)
        self.assertIn(("SolAndTheBeanStalk", "SolAndTheBeanstalk2", "corrects"), edges)
        self.assertFalse(any(e[0] == "SolAndTheBeanStalk" and e[1] == "SolAndTheBeanstalk2" and e[2] == "inherits" for e in edges))
        self.assertFalse(any("FourierFlower" in e[:2] for e in edges))
        wall = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn('id="nov6-beanstalk-fourier"', wall)
        for name in NAMES:
            self.assertIn('data-mad-node="' + name + '"', wall)
        self.assertTrue((ROOT / "docs/reviews/2026-11-06-beanstalk-games-and-fourier-flower.md").is_file())

if __name__ == "__main__":
    unittest.main()
