from pathlib import Path
import unittest

from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]


class CrystalHuntPassTests(unittest.TestCase):
    def test_curated_once_and_census_reviewed(self):
        atlas = load_atlas(ROOT)
        self.assertEqual([], validate_atlas(atlas))
        self.assertEqual(1, sum(n["id"] == "CrystalHunt" for n in atlas["nodes"]))
        self.assertEqual("reviewed", next(r["inventory_status"] for r in atlas["repos"] if r["name"] == "CrystalHunt"))
        self.assertIn("crystal-hunt-world-mind", [p["id"] for p in atlas["passes"]])

    def test_feedback_cautions_and_conceptual_not_inherited_edges(self):
        atlas = load_atlas(ROOT)
        node = next(n for n in atlas["nodes"] if n["id"] == "CrystalHunt")
        self.assertIn("64x64", node["claim"])
        self.assertIn("no comparative game", node["killed"].lower())
        self.assertIn("keyboard", node["killed"].lower())
        edges = {(e["source"],e["target"]):e["type"] for e in atlas["edges"]}
        self.assertEqual("converges",edges[("CrystalHunt","CrystalMoon")])
        self.assertEqual("converges",edges[("CrystalHunt","FieldComputer")])
        motif = next(m for m in atlas["motifs"] if m["id"] == "procedural-world-observer-feedback-boundary")
        self.assertIn("CrystalHunt", motif["nodes"])
        self.assertFalse(any(e["node"]=="CrystalHunt" for e in atlas["evidence"]))


if __name__ == "__main__":
    unittest.main()
