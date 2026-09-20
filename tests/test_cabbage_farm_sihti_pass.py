"""CabbageFarmSihti genealogy pass."""

import unittest
from pathlib import Path

from scripts.validate_data import load_atlas

ROOT = Path(__file__).resolve().parents[1]


class CabbageFarmSihtiPassTests(unittest.TestCase):
    def test_procedural_law_branch_is_on_wall(self):
        atlas = load_atlas(ROOT)
        ids = {node["id"] for node in atlas["nodes"]}
        self.assertIn("CabbageFarm", ids)
        self.assertIn("CabbageFarmSihti", ids)

        edges = {(e["source"], e["target"], e["type"]): e for e in atlas["edges"]}
        self.assertIn(("CabbageFarm", "CabbageFarmSihti", "inherits"), edges)
        self.assertIn(("Sihti2", "CabbageFarmSihti", "converges"), edges)

        node = next(n for n in atlas["nodes"] if n["id"] == "CabbageFarmSihti")
        self.assertIn("coordinate", node["survived"].lower())
        self.assertIn("power spectrum", node["killed"].lower())

    def test_generative_law_motif_and_census(self):
        atlas = load_atlas(ROOT)
        motifs = {m["id"]: m for m in atlas["motifs"]}
        self.assertEqual(
            set(motifs["generative-law-not-instance"]["nodes"]),
            {"CabbageFarm", "Sihti2", "CabbageFarmSihti"},
        )

        repos = {r["name"]: r for r in atlas["repos"]}
        self.assertEqual(repos["CabbageFarm"]["inventory_status"], "reviewed")
        self.assertEqual(repos["CabbageFarmSihti"]["inventory_status"], "reviewed")

        pass_ids = {p["id"] for p in atlas["passes"]}
        self.assertIn("cabbage-farm-sihti", pass_ids)


if __name__ == "__main__":
    unittest.main()
