"""October 28: four reviewed arrivals, one documented inheritance edge, no invented fork."""
import unittest
from pathlib import Path
from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]
PASS = "october-28-generative-life-and-loopcraft"
NAMES = {"Emergence", "Emergence2", "EmergenceAstra", "Loopcraft"}

class GenerativeLifeAndLoopcraftPassTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.atlas = load_atlas(ROOT)
        cls.nodes = {node["id"]: node for node in cls.atlas["nodes"]}
        cls.edges = {(edge["source"], edge["target"], edge["type"]) for edge in cls.atlas["edges"]}

    def test_unique_reviewed_census_and_pass(self):
        self.assertEqual(validate_atlas(self.atlas), [])
        self.assertGreaterEqual(len(self.atlas["repos"]), 554)
        for name in NAMES:
            self.assertEqual([r["name"] for r in self.atlas["repos"]].count(name), 1)
            self.assertEqual(len([n for n in self.atlas["nodes"] if n["id"] == name]), 1)
            self.assertEqual(self.nodes[name]["pass_id"], PASS)

    def test_direct_inheritance_only_and_control_boundaries(self):
        self.assertIn(("Emergence", "Emergence2", "inherits"), self.edges)
        self.assertNotIn(("Emergence", "EmergenceAstra", "inherits"), self.edges)
        self.assertNotIn(("Emergence", "EmergenceAstra", "forks"), self.edges)
        self.assertIn("straight", self.nodes["Emergence2"]["killed"])
        self.assertIn("1/3", self.nodes["EmergenceAstra"]["killed"])
        self.assertEqual(self.nodes["Loopcraft"]["status"], "tool")

    def test_visible_wall_and_docs(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn('id="oct28-generative-life"', html)
        for name in NAMES:
            self.assertIn(f'data-mad-node="{name}"', html)
            self.assertIn(f"https://github.com/anttiluode/{name}", readme)
        self.assertTrue((ROOT / "docs/reviews/2026-10-28-emergence-family-loopcraft.md").is_file())

if __name__ == "__main__":
    unittest.main()
