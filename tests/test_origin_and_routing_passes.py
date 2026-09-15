from pathlib import Path
import unittest

from scripts.validate_data import load_atlas

ROOT = Path(__file__).resolve().parents[1]


class OriginAndRoutingPassTests(unittest.TestCase):
    def test_deerskin_origin_pass_keeps_audits_and_handoffs_explicit(self):
        atlas = load_atlas(ROOT)
        pass_ids = {item["id"] for item in atlas["passes"]}
        self.assertIn("deerskin-origins", pass_ids)

        ids = {node["id"] for node in atlas["nodes"]}
        for node_id in (
            "deerskin-hypothesis",
            "PkasPCL3satSolver",
            "PkasDeerskin",
            "Deerskin-Cortex",
            "Takens-Gated-Deerskin",
        ):
            self.assertIn(node_id, ids)

        edges = {
            (edge["source"], edge["target"], edge["type"]): edge
            for edge in atlas["edges"]
        }
        for target in ("PkasDeerskin", "Deerskin-Cortex"):
            edge = edges[("deerskin-hypothesis", target, "inherits")]
            self.assertEqual(edge["confidence"], "high")
        self.assertIn(
            ("Takens-Gated-Deerskin", "Geometric-Neuron", "extracts"),
            edges,
        )
        self.assertIn(
            ("deerskin-hypothesis", "GeometricNeuronV21", "corrects"),
            edges,
        )

        origin = next(node for node in atlas["nodes"] if node["id"] == "deerskin-hypothesis")
        killed = origin["killed"].lower()
        self.assertIn("restart", killed)
        self.assertIn("must oscillate", killed)
        survived = origin["survived"].lower()
        self.assertIn("eeg", survived)
        self.assertIn("p = 0.007", survived)

    def test_spectral_routing_pass_uses_explicit_fusion_not_fake_ancestry(self):
        atlas = load_atlas(ROOT)
        pass_ids = {item["id"] for item in atlas["passes"]}
        self.assertIn("spectral-routing", pass_ids)

        edges = {
            (edge["source"], edge["target"], edge["type"]): edge
            for edge in atlas["edges"]
        }
        ga_edge = edges[("GAx", "ThirdWay", "converges")]
        self.assertEqual(ga_edge["confidence"], "high")
        for source in (
            "GeometricNeuronV25GeneticAlgoAndFanningNeuron",
            "Kompressori",
            "CausalHorizon",
        ):
            edge = edges[(source, "ThirdWay", "converges")]
            self.assertEqual(edge["confidence"], "high")

        self.assertNotIn(("GAx", "ThirdWay", "inherits"), edges)
        self.assertNotIn(
            ("GeometricNeuronV25GeneticAlgoAndFanningNeuron", "ThirdWay", "inherits"),
            edges,
        )

        motifs = {motif["id"]: motif for motif in atlas["motifs"]}
        self.assertIn("same-answer-different-computation", motifs)
        self.assertTrue(
            {"GAx", "ThirdWay", "TransformerStudy"}.issubset(
                set(motifs["same-answer-different-computation"]["nodes"])
            )
        )


if __name__ == "__main__":
    unittest.main()
