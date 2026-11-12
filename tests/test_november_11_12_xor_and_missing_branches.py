"""November 11–12: native-ring follow-up, missing Tunnistus, and XOR reductions."""
from pathlib import Path
import unittest
from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]
NOV11 = {"GeometricNeuronV28", "Tunnistus", "SihtiSR"}
NOV12 = {
    "MuistoVaihde", "GN-XOR", "KultaaVaiKatinkultaa",
    "KultaaVaiKatinkultaaOpus", "GoldOpus", "GoldSol",
    "GoldGemini", "PhaseLockedPredictiveCoding"
}

class NewNovemberResearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.atlas = load_atlas(ROOT)

    def test_valid_references_and_one_node_per_repo(self):
        self.assertEqual(validate_atlas(self.atlas), [])
        nodes = self.atlas["nodes"]
        inv = self.atlas["repos"]
        self.assertEqual(len({r["name"] for r in inv}), len(inv))
        for repo in NOV11 | NOV12 | {"GeometricNeuronV27", "Moon"}:
            self.assertEqual(sum(n["id"] == repo for n in nodes), 1, repo)
            self.assertEqual(
                [r["inventory_status"] for r in inv if r["name"] == repo],
                ["reviewed"], repo
            )

    def test_historical_v27_correction(self):
        v27 = next(n for n in self.atlas["nodes"] if n["id"] == "GeometricNeuronV27")
        self.assertEqual(v27["status"], "experiment")
        self.assertIn("40/40", v27["survived"])
        self.assertIn("proposal", v27["claim"])

    def test_new_evidence_and_walled_chapters(self):
        ev = self.atlas["evidence"]
        for name in ["Tunnistus", "GeometricNeuronV28", "SihtiSR",
                     "KultaaVaiKatinkultaaOpus", "GoldOpus",
                     "GoldSol", "PhaseLockedPredictiveCoding"]:
            self.assertTrue(any(e["node"] == name for e in ev), name)
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn('id="nov12-xor-madness"', html)
        self.assertIn('id="nov11-v27-v28"', html)
        for name in NOV11 | NOV12:
            self.assertIn('data-mad-node="' + name + '"', html)
        review = (ROOT / "docs/reviews/2026-11-12-native-rings-xor-and-controls.md").read_text(encoding="utf-8")
        for value in ("Tunnistus", "RAISR", "checkerboard-free", "55/71", "phase-masquerade"):
            self.assertIn(value, review)

if __name__ == "__main__":
    unittest.main()
