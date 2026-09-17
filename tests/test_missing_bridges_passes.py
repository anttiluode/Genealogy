from pathlib import Path
import unittest

from scripts.validate_data import load_atlas

ROOT = Path(__file__).resolve().parents[1]


class MissingBridgesPassTests(unittest.TestCase):
    def test_missing_bridge_repositories_are_first_class_nodes(self):
        atlas = load_atlas(ROOT)
        nodes = {node["id"]: node for node in atlas["nodes"]}

        expected = {
            "DendriteAsIteratedFeedbackOperator",
            "OutoSynapsi",
            "AlternativeNeuron",
            "RajoitustenHierarkia",
            "SelectCarryBindWriteAskSelect",
            "CausalHorizon",
            "GAlinearPredictionNetwork",
            "AuditedEpistemicCache",
        }
        self.assertTrue(expected.issubset(nodes), expected - set(nodes))

    def test_documentary_bridge_edges_are_preserved(self):
        atlas = load_atlas(ROOT)
        edges = {(edge["source"], edge["target"], edge["type"]) for edge in atlas["edges"]}

        self.assertIn(("SighImageSuper", "DendriteAsIteratedFeedbackOperator", "inherits"), edges)
        self.assertIn(("OutoSynapsi", "AlternativeNeuron", "converges"), edges)
        self.assertIn(("InformationFlow", "SelectCarryBindWriteAskSelect", "converges"), edges)
        self.assertIn(("GAlinearPredictionNetwork", "ThirdWay", "extracts"), edges)

    def test_new_passes_are_registered(self):
        atlas = load_atlas(ROOT)
        pass_ids = {item["id"] for item in atlas["passes"]}

        expected = {
            "operator-learning-bridge",
            "field-memory-continuation",
            "math-and-learning-boundaries",
            "epistemic-cache",
        }
        self.assertTrue(expected.issubset(pass_ids), expected - pass_ids)

    def test_statistics_is_a_cross_cutting_evidence_discipline_not_a_fake_repo(self):
        atlas = load_atlas(ROOT)
        nodes = {node["id"] for node in atlas["nodes"]}
        motifs = {motif["id"]: motif for motif in atlas["motifs"]}

        self.assertNotIn("Statistics", nodes)
        self.assertIn("statistical-evidence-is-a-separate-layer", motifs)
        motif = motifs["statistical-evidence-is-a-separate-layer"]
        self.assertIn("RajoitustenHierarkia", motif["nodes"])
        self.assertIn("AuditedEpistemicCache", motif["nodes"])


if __name__ == "__main__":
    unittest.main()
