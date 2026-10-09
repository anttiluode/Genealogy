from pathlib import Path
import unittest
from scripts.validate_data import load_atlas

ROOT = Path(__file__).resolve().parents[1]

class PredictiveLoopTests(unittest.TestCase):
    def setUp(self):
        self.a = load_atlas(ROOT)

    def test_two_nodes_are_reviewed(self):
        nodes = {x["id"]: x for x in self.a["nodes"]}
        repos = {x["name"]: x for x in self.a["repos"]}
        self.assertIn("descending-predictive-loop", {x["id"] for x in self.a["passes"]})
        for name in ("CorticalLoop", "Alavirta"):
            self.assertIn(name, nodes)
            self.assertEqual(repos[name]["inventory_status"], "reviewed")

    def test_parent_and_representational_links(self):
        edges = {(x["source"], x["target"], x["type"]) for x in self.a["edges"]}
        self.assertIn(("CorticalLoop", "Alavirta", "inherits"), edges)
        self.assertIn(("GeometricNeuronV21", "Alavirta", "converges"), edges)
        self.assertIn(("GeometricNeuronV9", "CorticalLoop", "converges"), edges)

    def test_evidence_and_open_discriminator(self):
        records = {x["id"]: x for x in self.a["evidence"]}
        for name in ("cortical-loop-blackout-and-direction", "cortical-loop-linear-grid-discovery", "alavirta-shared-space-correction"):
            self.assertIn(name, records)
            self.assertFalse(records[name]["held_out"])
            self.assertIn("not", records[name]["replication"].lower())
        q = {x["id"]: x for x in self.a["questions"]}["learned-shared-space-predictive-loop"]
        self.assertEqual(q["state"], "open")
        self.assertEqual(len(q["evidence"]), 3)

if __name__ == "__main__":
    unittest.main()
