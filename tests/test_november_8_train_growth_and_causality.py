"""November 8: six reviewed branches, five new census repositories, distinct lineage."""
import unittest
from pathlib import Path
from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]
PASS = "november-8-train-growth-and-causal-audits"
NAMES = {
    "TurntableNeuron", "TurntableAISol", "KasvavatKiskotSol",
    "KasvavatKiskotClaude", "TorsionFreeMirrorLock",
    "GeometricNeuronOriginReview",
}

class November8TrainGrowthTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.atlas = load_atlas(ROOT)

    def test_census_nodes_and_schema(self):
        self.assertEqual(validate_atlas(self.atlas), [])
        self.assertGreaterEqual(len(self.atlas["repos"]), 604)
        self.assertEqual(
            {n["id"] for n in self.atlas["nodes"] if n.get("pass_id") == PASS},
            NAMES,
        )
        for name in NAMES:
            self.assertEqual(sum(x["name"] == name for x in self.atlas["repos"]), 1)
            self.assertEqual(sum(x["id"] == name for x in self.atlas["nodes"]), 1)

    def test_two_independent_growing_rail_branches(self):
        edges = {(e["source"], e["target"], e["type"]) for e in self.atlas["edges"]}
        for expected in (
            ("TurntableNeuron", "TurntableAISol", "extracts"),
            ("TurntableNeuron", "KasvavatKiskotSol", "extracts"),
            ("TurntableNeuron", "KasvavatKiskotClaude", "extracts"),
            ("Friday", "TorsionFreeMirrorLock", "converges"),
            ("PerceptionLab", "GeometricNeuronOriginReview", "extracts"),
            ("KasvavatKiskotClaude", "KasvavatKiskotSol", "converges"),
        ):
            self.assertIn(expected, edges)
        self.assertNotIn(("KasvavatKiskotClaude", "KasvavatKiskotSol", "inherits"), edges)

    def test_corrections_survive(self):
        by_id = {n["id"]: n for n in self.atlas["nodes"]}
        self.assertIn("59", by_id["GeometricNeuronOriginReview"]["survived"])
        self.assertIn("52", by_id["GeometricNeuronOriginReview"]["killed"])
        self.assertIn("nonlocal", by_id["KasvavatKiskotClaude"]["killed"].lower())
        self.assertIn("not earned", by_id["TorsionFreeMirrorLock"]["killed"])
        self.assertIn("Private data jitter", by_id["TurntableNeuron"]["killed"])

    def test_visible_wall_and_review(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn('id="nov8-railway-causality"', html)
        for name in NAMES:
            self.assertIn('data-mad-node="' + name + '"', html)
        self.assertTrue(
            (ROOT / "docs/reviews/2026-11-08-train-growth-and-causality.md").is_file()
        )

if __name__ == "__main__":
    unittest.main()
