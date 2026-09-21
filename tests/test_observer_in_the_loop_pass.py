import json
from pathlib import Path
import unittest

from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


class ObserverInTheLoopPassTests(unittest.TestCase):
    def test_pass_is_enabled_and_valid(self):
        index = json.loads((DATA / "passes" / "index.json").read_text(encoding="utf-8"))
        self.assertTrue(any(
            row["path"] == "observer-in-the-loop.json" and row.get("enabled", True)
            for row in index
        ))
        atlas = load_atlas(ROOT)
        self.assertEqual(validate_atlas(atlas), [])
        self.assertIn("observer-in-the-loop", {p["id"] for p in atlas["passes"]})

    def test_survivor_motif_spans_old_and_current_observer_lines(self):
        atlas = load_atlas(ROOT)
        motif = next(
            m for m in atlas["motifs"]
            if m["id"] == "observer-participates-in-dynamics"
        )
        ids = set(motif["nodes"])
        for node_id in (
            "MoireBrain",
            "GeometricNeuronV24",
            "ReadWrite",
            "SighImageSuper",
            "PredictiveHKT",
            "SplatWorld4",
            "WhatToLookAt",
            "AuditedEpistemicCache",
            "OperatorTime",
            "AInstein",
            "AinsteinInsideTransformerResidualStream",
        ):
            self.assertIn(node_id, ids)

    def test_wall_gets_cross_cutting_observer_edges(self):
        atlas = load_atlas(ROOT)
        edges = {(e["source"], e["target"], e["type"]) for e in atlas["edges"]}
        self.assertIn(("MoireBrain", "GeometricNeuronV24", "rediscovery"), edges)
        self.assertIn(("SplatWorld4", "WhatToLookAt", "converges"), edges)
        self.assertIn(
            ("PredictiveHKT", "AinsteinInsideTransformerResidualStream", "rediscovery"),
            edges,
        )
        self.assertIn(
            ("AuditedEpistemicCache", "AinsteinInsideTransformerResidualStream", "converges"),
            edges,
        )

    def test_gate07d_is_recorded_as_instrument_validity_not_cognition(self):
        atlas = load_atlas(ROOT)
        node = next(
            n for n in atlas["nodes"]
            if n["id"] == "AinsteinInsideTransformerResidualStream"
        )
        self.assertIn("0.01645", node["survived"])
        self.assertIn("0.02843", node["survived"])
        self.assertIn("fine-grained first-action", node["killed"])
        self.assertIn("instrument-validity", node["tags"])

        evidence = next(
            e for e in atlas["evidence"]
            if e["id"] == "ainstein-transformer-gate07d-instrument-invariance"
        )
        self.assertEqual(evidence["result"], "mixed")
        self.assertIn("observer-participates-in-dynamics", evidence["motifs"])
        self.assertIn("measurement-receipt-validity", evidence["motifs"])


if __name__ == "__main__":
    unittest.main()
