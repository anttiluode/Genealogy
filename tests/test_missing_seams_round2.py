from pathlib import Path
import unittest

from scripts.validate_data import load_atlas

ROOT = Path(__file__).resolve().parents[1]


class MissingSeamsRound2Tests(unittest.TestCase):
    def test_missing_repositories_are_first_class_nodes(self):
        atlas = load_atlas(ROOT)
        nodes = {node["id"]: node for node in atlas["nodes"]}

        expected = {
            "NeuralAlgorithmDecoding",
            "MorphoGeneticneuronClaude50Opus",
            "MorphogeneticNeuronChatGPTSol",
            "WidePresent",
            "PresentMoment",
            "PredictiveHKT",
            "Island-Memory-Field",
            "AgainstTheGrain",
        }
        self.assertTrue(expected.issubset(nodes), expected - set(nodes))

    def test_missing_seam_passes_are_registered(self):
        atlas = load_atlas(ROOT)
        pass_ids = {item["id"] for item in atlas["passes"]}

        expected = {
            "algorithm-decoding",
            "developmental-order-memory",
            "temporal-epistemic-lineage",
            "geometric-reversal",
        }
        self.assertTrue(expected.issubset(pass_ids), expected - pass_ids)

    def test_documentary_edges_capture_the_missing_lineages(self):
        atlas = load_atlas(ROOT)
        edges = {(edge["source"], edge["target"], edge["type"]) for edge in atlas["edges"]}

        self.assertIn(("GeometricNeuronV5", "MorphoGeneticneuronClaude50Opus", "extracts"), edges)
        self.assertIn(("PhaseStigmergy", "MorphogeneticNeuronChatGPTSol", "converges"), edges)
        self.assertIn(("WidePresent", "PresentMoment", "forks"), edges)
        self.assertIn(("WidePresent", "AuditedEpistemicCache", "extracts"), edges)
        self.assertIn(("PredictiveHKT", "AuditedEpistemicCache", "extracts"), edges)
        self.assertIn(("Island-Memory-Field", "AuditedEpistemicCache", "extracts"), edges)
        self.assertIn(("GeometricNeuronV9", "AgainstTheGrain", "inherits"), edges)

    def test_extraction_reuse_is_visible_as_a_cross_repo_motif(self):
        atlas = load_atlas(ROOT)
        motifs = {motif["id"]: motif for motif in atlas["motifs"]}

        self.assertIn("extraction-reuse-spine", motifs)
        motif_nodes = set(motifs["extraction-reuse-spine"]["nodes"])
        expected = {
            "NeuralAlgorithmDecoding",
            "ResonantCortex2",
            "AnotherOddThing",
            "EvoX",
            "Operaattori",
            "OperaattoriJako",
            "SplatPack",
            "WidePresent",
            "AuditedEpistemicCache",
            "Island-Memory-Field",
            "MorphogeneticNeuronChatGPTSol",
            "AgainstTheGrain",
        }
        self.assertTrue(expected.issubset(motif_nodes), expected - motif_nodes)

    def test_algorithm_decoding_preserves_identifiability_boundary(self):
        atlas = load_atlas(ROOT)
        node = {node["id"]: node for node in atlas["nodes"]}["NeuralAlgorithmDecoding"]
        self.assertIn("2-state", node["survived"])
        self.assertIn("NOT_IDENTIFIABLE", node["survived"])
        self.assertIn("arbitrary", node["killed"].lower())


if __name__ == "__main__":
    unittest.main()
