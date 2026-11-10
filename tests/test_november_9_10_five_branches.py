"""November 9–10: five curated arrivals, not five new inventory records."""
import unittest
from pathlib import Path
from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]
PASS = "november-9-10-active-eyes-private-memory-fable-worlds"
REVIEW = ROOT / "docs/reviews/2026-11-10-five-branches-active-eyes-fable-worlds.md"
NAMES = ("OneTinyTransformer", "SihtiSilma", "Muru", "CrystalMoonV3", "NotKansas2")


class NovemberNineTenGenealogyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.atlas = load_atlas(ROOT)

    def test_inventory_is_not_duplicated(self):
        self.assertEqual(validate_atlas(self.atlas), [])
        self.assertGreaterEqual(len(self.atlas["repos"]), 610)
        for name in NAMES:
            inventory = [r for r in self.atlas["repos"] if r["name"] == name]
            self.assertEqual(len(inventory), 1, name)
            self.assertEqual(inventory[0]["inventory_status"], "reviewed")
            nodes = [n for n in self.atlas["nodes"] if n["id"] == name]
            self.assertEqual(len(nodes), 1, name)
            self.assertEqual(nodes[0]["pass_id"], PASS)

    def test_direct_code_inheritance_versus_conceptual_extracts(self):
        edges = {(e["source"], e["target"], e["type"]) for e in self.atlas["edges"]}
        self.assertIn(("SihtiImageModel", "SihtiSilma", "inherits"), edges)
        self.assertIn(("SihtiSilma", "Muru", "extracts"), edges)
        self.assertIn(("OneTinyTransformer", "Muru", "extracts"), edges)
        self.assertNotIn(("OneTinyTransformer", "Muru", "inherits"), edges)
        self.assertIn(("CrystalMoonV2", "CrystalMoonV3", "inherits"), edges)
        self.assertIn(("NotKansas", "NotKansas2", "inherits"), edges)
        self.assertNotIn(("CrystalMoonV3", "NotKansas2", "inherits"), edges)

    def test_all_five_have_evidence_and_explicit_limitations(self):
        for name in NAMES:
            node = next(n for n in self.atlas["nodes"] if n["id"] == name)
            self.assertTrue(node["killed"])
            evs = [e for e in self.atlas["evidence"] if e["node"] == name]
            self.assertGreaterEqual(len(evs), 1, name)
            self.assertTrue(any(e["limitations"] for e in evs), name)
        p3 = next(e for e in self.atlas["evidence"] if e["id"] == "nov9-sihtisilma-200-image-active-selection")
        self.assertEqual(p3["sample"]["count"], 200)
        self.assertTrue(p3["held_out"])
        pet = next(e for e in self.atlas["evidence"] if e["id"] == "nov9-muru-pillars-matched-observation")
        self.assertEqual(pet["sample"]["count"], 5)

    def test_landing_chapter_and_review_exist(self):
        html = (ROOT / "index.html").read_text(encoding="utf8")
        self.assertIn('id="nov9-10-new-branches"', html)
        for name in NAMES:
            self.assertIn(f'data-mad-node="{name}"', html)
        self.assertTrue(REVIEW.is_file())
        self.assertIn("flat 64", REVIEW.read_text(encoding="utf8"))


if __name__ == "__main__":
    unittest.main()
