"""November 7 CrystalMoon genealogical regression checks."""
import unittest
from pathlib import Path
from scripts.validate_data import load_atlas, validate_atlas
ROOT = Path(__file__).resolve().parents[1]
PASS = "november-7-crystalmoon-descendants"
NAMES = {"CrystalMoonV2", "NotKansas"}

class DescendantTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.atlas = load_atlas(ROOT)

    def test_census_and_nodes(self):
        self.assertEqual(validate_atlas(self.atlas), [])
        self.assertEqual(len(self.atlas["repos"]), 599)
        self.assertEqual({n["id"] for n in self.atlas["nodes"] if n.get("pass_id") == PASS}, NAMES)
        for name in NAMES:
            self.assertEqual(sum(r["name"] == name for r in self.atlas["repos"]), 1)
            self.assertEqual(sum(n["id"] == name for n in self.atlas["nodes"]), 1)

    def test_edges_and_existing_nodes(self):
        edges = {(e["source"],e["target"],e["type"]) for e in self.atlas["edges"] if e.get("pass_id") == PASS}
        self.assertEqual(edges, {("CrystalMoon","CrystalMoonV2","inherits"),("CrystalMoonV2","NotKansas","inherits")})
        for name in ("Story2","ZetaDreamer3D","ZetaDreamer3DV2"):
            self.assertEqual(sum(n["id"] == name for n in self.atlas["nodes"]), 1)

    def test_wall(self):
        wall = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn('id="nov7-crystal-descendants"', wall)
        for name in NAMES:
            self.assertIn('data-mad-node="' + name + '"',wall)
        self.assertTrue((ROOT / "docs/reviews/2026-11-07-crystalmoon-descendants.md").is_file())

if __name__ == "__main__":
    unittest.main()
