"""TarinaSR joins the curated visual-memory genealogy once, with measured boundaries."""
import unittest
from pathlib import Path
from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]

class TarinaSRGenealogyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.atlas = load_atlas(ROOT)

    def test_valid_and_unique_curated_entry(self):
        self.assertEqual(validate_atlas(self.atlas), [])
        nodes = [n for n in self.atlas["nodes"] if n["id"] == "TarinaSR"]
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0]["pass_id"], "november-12-tarinasr-shake-superresolution")
        inv = [r for r in self.atlas["repos"] if r["name"] == "TarinaSR"]
        self.assertEqual(len(inv), 1)
        self.assertEqual(inv[0]["inventory_status"], "reviewed")

    def test_actual_code_inheritance_not_phase_hub_copy(self):
        edges = {(e["source"],e["target"],e["type"]) for e in self.atlas["edges"]}
        self.assertIn(("SihtiSR","TarinaSR","inherits"),edges)
        self.assertIn(("GoldOpus","TarinaSR","extracts"),edges)
        self.assertIn(("PhaseLockedPredictiveCoding","TarinaSR","converges"),edges)
        self.assertNotIn(("PhaseLockedPredictiveCoding","TarinaSR","inherits"),edges)

    def test_results_controls_and_prior_art_recorded(self):
        ev = [e for e in self.atlas["evidence"] if e["node"] == "TarinaSR"]
        self.assertTrue(ev)
        self.assertTrue(any("Whole-low-resolution-pixel" in " ".join(e["controls"]) for e in ev))
        page = (ROOT/"index.html").read_text(encoding="utf-8")
        self.assertIn('id="nov12-tarinasr"',page)
        self.assertIn('data-mad-node="TarinaSR"',page)
        review=(ROOT/"docs/reviews/2026-11-12-tarinasr-subpixel-shake.md").read_text(encoding="utf-8")
        for phrase in ("Irani", "37.42", "31.86", "real phone", "SihtiSR"):
            self.assertIn(phrase,review)

if __name__=="__main__":
    unittest.main()
