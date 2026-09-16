from pathlib import Path
import unittest

from scripts.validate_data import load_atlas

ROOT = Path(__file__).resolve().parents[1]


class SyntheticUniverseEpistemologyTests(unittest.TestCase):
    def test_matrix_in_matrix_preserves_map_vs_mechanism_boundary(self):
        atlas = load_atlas(ROOT)
        nodes = {node["id"]: node for node in atlas["nodes"]}

        self.assertIn("MatrixInMatrix", nodes)
        node = nodes["MatrixInMatrix"]
        self.assertEqual(node["status"], "experiment")
        self.assertIn("compression", node["survived"].lower())
        self.assertIn("source mechanism", node["killed"].lower())

    def test_phi_world_theory_is_curated_as_an_idea_mine_not_evidence(self):
        atlas = load_atlas(ROOT)
        nodes = {node["id"]: node for node in atlas["nodes"]}

        self.assertIn("phi-world-theory", nodes)
        node = nodes["phi-world-theory"]
        self.assertEqual(node["status"], "idea-mine")
        self.assertIn("ai slop", node["killed"].lower())
        self.assertIn("workflow", node["survived"].lower())

    def test_model_is_not_mechanism_motif_connects_the_two_repos(self):
        atlas = load_atlas(ROOT)
        motifs = {motif["id"]: motif for motif in atlas["motifs"]}

        self.assertIn("model-is-not-source-mechanism", motifs)
        motif = motifs["model-is-not-source-mechanism"]
        self.assertIn("MatrixInMatrix", motif["nodes"])
        self.assertIn("phi-world-theory", motif["nodes"])
        self.assertIn("mechanism", motif["description"].lower())
        self.assertIn("prediction", motif["description"].lower())


if __name__ == "__main__":
    unittest.main()
