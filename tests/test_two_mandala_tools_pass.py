from pathlib import Path
import unittest
from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]

class TwoMandalaToolsPassTest(unittest.TestCase):
    def test_atlas_pass_and_reviewed_census(self):
        atlas = load_atlas(ROOT)
        self.assertEqual([], validate_atlas(atlas))
        self.assertEqual(1, sum(n["id"] == "2MandalaTools" for n in atlas["nodes"]))
        self.assertEqual("reviewed", next(r["inventory_status"] for r in atlas["repos"] if r["name"] == "2MandalaTools"))
        self.assertIn("two-mandala-tools-frequency-lens", [p["id"] for p in atlas["passes"]])

    def test_scientific_boundaries_and_conceptual_edges(self):
        atlas = load_atlas(ROOT)
        node = next(n for n in atlas["nodes"] if n["id"] == "2MandalaTools")
        self.assertIn("FFT", node["claim"])
        self.assertIn("cancel algebraically", node["killed"])
        self.assertIn("TikTok", node["killed"])
        edges = {(x["source"], x["target"]): x for x in atlas["edges"]}
        for target in ("SighImageSuper", "Sihti"):
            e = edges[("2MandalaTools", target)]
            self.assertEqual("converges", e["type"])
            self.assertNotEqual("inherits", e["type"])
        motif = next(x for x in atlas["motifs"] if x["id"] == "radial-frequency-lens-versus-operator-created-structure")
        self.assertEqual({"2MandalaTools", "SighImageSuper", "Sihti"}, set(motif["nodes"]))
        self.assertFalse(any(e["node"] == "2MandalaTools" for e in atlas["evidence"]))

if __name__ == "__main__":
    unittest.main()
