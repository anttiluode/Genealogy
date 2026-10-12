from pathlib import Path
import unittest

from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]


class FieldVineLineageTests(unittest.TestCase):
    def test_one_reviewed_node_for_each_repo(self):
        atlas = load_atlas(ROOT)
        self.assertEqual([], validate_atlas(atlas))
        self.assertIn("field-memory-and-growing-geometry", [x["id"] for x in atlas["passes"]])
        for name in ("FieldComputer", "VineComputer"):
            self.assertEqual(1, [x["id"] for x in atlas["nodes"]].count(name))
            repo = next(r for r in atlas["repos"] if r["name"] == name)
            self.assertEqual("reviewed", repo["inventory_status"])

    def test_controls_and_failures_survive_synthesis(self):
        atlas = load_atlas(ROOT)
        nodes = {x["id"]: x for x in atlas["nodes"]}
        self.assertIn("uncoupled nonlinear cells", nodes["FieldComputer"]["killed"].lower())
        self.assertIn("16-state", nodes["FieldComputer"]["killed"])
        self.assertIn("88.0%", nodes["FieldComputer"]["survived"])
        self.assertIn("not paired", nodes["VineComputer"]["killed"])
        self.assertIn("random search", nodes["VineComputer"]["killed"])
        evidence = {x["id"]: x for x in atlas["evidence"]}
        self.assertEqual("supports", evidence["fieldcomputer-nonlinear-pulse-and-probe-memory"]["result"])
        self.assertEqual("contradicts", evidence["fieldcomputer-no-spatial-or-scout-advantage"]["result"])
        self.assertEqual("mixed", evidence["vinecomputer-selection-versus-drift"]["result"])
        self.assertEqual(0, next(m["value"] for m in evidence["fieldcomputer-no-spatial-or-scout-advantage"]["metrics"] if m["name"].startswith("reciprocal quadratic advantage")))
        self.assertIn("grown-geometry-necessary-for-transport-computation", [q["id"] for q in atlas["questions"]])
        edges = {(e["source"],e["target"],e["type"]) for e in atlas["edges"]}
        self.assertIn(("GrowingAnttisNeuron","VineComputer","converges"),edges)
        self.assertIn(("FieldComputer","VineComputer","converges"),edges)

if __name__ == "__main__":
    unittest.main()
