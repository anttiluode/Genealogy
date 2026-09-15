from pathlib import Path
import unittest

from scripts.validate_data import load_atlas

ROOT = Path(__file__).resolve().parents[1]


class DynamicalResetPassTests(unittest.TestCase):
    def test_dynamical_reset_keeps_persistent_material_and_learning_audits(self):
        atlas = load_atlas(ROOT)
        pass_ids = {item["id"] for item in atlas["passes"]}
        self.assertIn("dynamical-neuron-reset", pass_ids)

        ids = {node["id"] for node in atlas["nodes"]}
        for node_id in ("Sunday", "GeoNeuronX", "RecurrentGeometricNet"):
            self.assertIn(node_id, ids)

        edges = {
            (edge["source"], edge["target"], edge["type"]): edge
            for edge in atlas["edges"]
        }
        self.assertEqual(
            edges[("GeometricNeuronV5", "RecurrentGeometricNet", "inherits")]["confidence"],
            "high",
        )
        self.assertEqual(
            edges[("RecurrentGeometricNet", "MovingProblem", "corrects")]["confidence"],
            "high",
        )
        self.assertEqual(
            edges[("GeoNeuronX", "T-800NNP", "inherits")]["confidence"],
            "high",
        )
        for source in ("Sunday", "Monday", "Tuesday"):
            self.assertEqual(
                edges[(source, "GeoNeuronX", "converges")]["confidence"],
                "high",
            )

        sunday = next(node for node in atlas["nodes"] if node["id"] == "Sunday")
        self.assertIn("reservoir", sunday["killed"].lower())
        self.assertIn("persistent", sunday["survived"].lower())

        geox = next(node for node in atlas["nodes"] if node["id"] == "GeoNeuronX")
        self.assertIn("0.8440", geox["survived"])
        self.assertIn("whitening", geox["killed"].lower())

        recurrent = next(node for node in atlas["nodes"] if node["id"] == "RecurrentGeometricNet")
        self.assertIn("1.000", recurrent["survived"])
        self.assertIn("backprop", recurrent["killed"].lower())

    def test_audit_learning_rule_motif_connects_the_three_stages(self):
        atlas = load_atlas(ROOT)
        motifs = {motif["id"]: motif for motif in atlas["motifs"]}
        motif = motifs["audit-the-learning-rule"]
        self.assertTrue(
            {"RecurrentGeometricNet", "GeoNeuronX", "MovingProblem"}.issubset(
                set(motif["nodes"])
            )
        )


if __name__ == "__main__":
    unittest.main()
