"""Sihti2 genealogy pass."""

import unittest
from pathlib import Path

from scripts.validate_data import load_atlas

ROOT = Path(__file__).resolve().parents[1]


class Sihti2PassTests(unittest.TestCase):
    def test_sihti2_is_on_wall_with_narrow_lineage(self):
        atlas = load_atlas(ROOT)
        ids = {node["id"] for node in atlas["nodes"]}
        self.assertIn("Sihti2", ids)

        edges = {(edge["source"], edge["target"], edge["type"]): edge for edge in atlas["edges"]}
        edge = edges[("Sihti", "Sihti2", "inherits")]
        self.assertEqual(edge["confidence"], "high")

        node = next(node for node in atlas["nodes"] if node["id"] == "Sihti2")
        self.assertIn("spectral", node["survived"].lower())
        self.assertIn("fractal", node["killed"].lower())

    def test_sihti2_joins_operator_defined_persistence_not_object_claim(self):
        atlas = load_atlas(ROOT)
        motifs = {m["id"]: m for m in atlas["motifs"]}
        self.assertIn("Sihti2", motifs["operator-defines-persistence"]["nodes"])

        repos = {r["name"]: r for r in atlas["repos"]}
        self.assertIn("Sihti2", repos)
        self.assertEqual(repos["Sihti2"]["inventory_status"], "reviewed")

        pass_ids = {p["id"] for p in atlas["passes"]}
        self.assertIn("sihti2-spectral-geometry", pass_ids)


if __name__ == "__main__":
    unittest.main()
