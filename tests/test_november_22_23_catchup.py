"""Regression guard: missing November 22 projects + Nov 23 Pisara/VirtualTuft."""
import json
import unittest
from pathlib import Path
from scripts.validate_data import load_atlas, validate_atlas

ROOT=Path(__file__).resolve().parents[1]
EXPECTED_22={"ShadowValley","HeadAsResonator3","Theorem","CabbageSuper","JanusBoxCabbageSihtiX","SighImageX","BlackBoxSpotlight","SighImageInverse"}
EXPECTED_23={"Pisara","VirtualTuft"}

class LateNovemberTests(unittest.TestCase):
    def test_inventory_and_curated_nodes_are_unique(self):
        atlas=load_atlas(ROOT)
        self.assertEqual([],validate_atlas(atlas))
        self.assertEqual(684,len(atlas["repos"]))
        for name in EXPECTED_22|EXPECTED_23:
            self.assertEqual(1,sum(r["name"]==name for r in atlas["repos"]),name)
            self.assertEqual(1,sum(n["id"]==name for n in atlas["nodes"]),name)
    def test_live_wall_and_provenance(self):
        html=(ROOT/"index.html").read_text(encoding="utf-8")
        for section in ("nov22-shadow-theorem-resonator","nov23-delay-memory"):
            self.assertIn('id="'+section+'"',html)
        for name in EXPECTED_22|EXPECTED_23:
            self.assertIn('data-mad-node="'+name+'"',html)
        paths=[p["path"] for p in json.loads((ROOT/"data/passes/index.json").read_text(encoding="utf-8"))]
        self.assertIn("november-22-identifiability-head-shadow-and-audio.json",paths)
        self.assertIn("november-23-pisara-virtualtuft-delayed-memories.json",paths)

if __name__=="__main__":
    unittest.main()
