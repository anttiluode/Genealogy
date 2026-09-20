from pathlib import Path
import unittest

from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]

class AInsteinPassTests(unittest.TestCase):
    def test_ainstein_is_on_the_wall_with_operator_time_lineage(self):
        atlas = load_atlas(ROOT)
        self.assertEqual(validate_atlas(atlas), [])
        self.assertIn("ainstein", {p["id"] for p in atlas["passes"]})
        ids = {n["id"] for n in atlas["nodes"]}
        self.assertIn("AInstein", ids)
        edges = {(e["source"], e["target"], e["type"]) for e in atlas["edges"]}
        self.assertIn(("OperatorTime", "AInstein", "inherits"), edges)
        self.assertIn(("GAx", "AInstein", "converges"), edges)
        self.assertIn(("Sihti", "AInstein", "converges"), edges)
        self.assertIn(("AnotherOddThing", "AInstein", "converges"), edges)
        self.assertIn(("WhatToLookAt", "AInstein", "converges"), edges)

    def test_ainstein_keeps_transformer_control_as_a_correction(self):
        atlas = load_atlas(ROOT)
        node = next(n for n in atlas["nodes"] if n["id"] == "AInstein")
        self.assertIn("attention convexity", node["killed"].lower())
        self.assertIn("0.9467", node["survived"])
        motif = next(m for m in atlas["motifs"] if m["id"] == "constructive-residue-synthesis")
        self.assertIn("AInstein", motif["nodes"])
        self.assertIn("OperatorTime", motif["nodes"])


    def test_gate2_records_active_collision_budget_and_misbinding_boundary(self):
        atlas = load_atlas(ROOT)
        node = next(n for n in atlas["nodes"] if n["id"] == "AInstein")
        self.assertIn("0.9531", node["survived"])
        self.assertIn("4.6875%", node["survived"])
        self.assertIn("0.4762", node["killed"])
        self.assertIn("confidence alone", node["killed"].lower())
        self.assertIn("active-collision-selection", node["tags"])
        self.assertIn("address-misbinding", node["tags"])


    def test_gate3_records_matched_budget_topology_and_wiring_attackers(self):
        atlas = load_atlas(ROOT)
        node = next(n for n in atlas["nodes"] if n["id"] == "AInstein")
        self.assertIn("0.9986", node["survived"])
        self.assertIn("0.3091", node["survived"])
        self.assertIn("-0.0118", node["survived"])
        self.assertIn("unit count alone", node["killed"].lower())
        self.assertIn("coincidence", node["killed"].lower())
        self.assertIn("topology-grown-synthesis", node["tags"])
        edges = {(e["source"], e["target"], e["type"]) for e in atlas["edges"]}
        self.assertIn(("DendriteAsIteratedFeedbackOperator", "AInstein", "converges"), edges)
        self.assertIn(("AnttisNeuron", "AInstein", "converges"), edges)

if __name__ == "__main__":
    unittest.main()
