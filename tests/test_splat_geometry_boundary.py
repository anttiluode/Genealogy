from pathlib import Path
import unittest

from scripts.validate_data import load_atlas

ROOT = Path(__file__).resolve().parents[1]


class SplatGeometryBoundaryTests(unittest.TestCase):
    def test_worldrank_and_worldplus_are_first_class_negative_results(self):
        atlas = load_atlas(ROOT)
        nodes = {node["id"]: node for node in atlas["nodes"]}

        self.assertIn("WorldRank", nodes)
        self.assertIn("WorldPlus", nodes)

        self.assertEqual(nodes["WorldRank"]["status"], "negative")
        self.assertIn("rank 2", nodes["WorldRank"]["killed"].lower())
        self.assertIn("rank 3", nodes["WorldRank"]["survived"].lower())

        self.assertEqual(nodes["WorldPlus"]["status"], "negative")
        self.assertIn("counterfactual", nodes["WorldPlus"]["killed"].lower())
        self.assertIn("alias", nodes["WorldPlus"]["survived"].lower())

    def test_documented_geometry_audit_lineage_is_present(self):
        atlas = load_atlas(ROOT)
        edges = {(edge["source"], edge["target"], edge["type"]) for edge in atlas["edges"]}

        self.assertIn(("TinyAvatar", "WorldRank", "extracts"), edges)
        self.assertIn(("WorldRank", "WorldPlus", "inherits"), edges)

    def test_splat_vs_3dgs_boundary_is_visible_as_a_motif(self):
        atlas = load_atlas(ROOT)
        motifs = {motif["id"]: motif for motif in atlas["motifs"]}

        self.assertIn("generative-splats-are-not-3dgs", motifs)
        motif = motifs["generative-splats-are-not-3dgs"]
        for node_id in ("SplatWorld", "TinyAvatar", "WorldRank", "WorldPlus", "WorldModel"):
            self.assertIn(node_id, motif["nodes"])
        self.assertIn("scene-specific", motif["description"].lower())
        self.assertIn("generative", motif["description"].lower())

    def test_rank_two_shortcut_is_preserved_as_a_boundary(self):
        atlas = load_atlas(ROOT)
        motifs = {motif["id"]: motif for motif in atlas["motifs"]}

        self.assertIn("rank-two-is-not-depth", motifs)
        motif = motifs["rank-two-is-not-depth"]
        self.assertIn("rank-3", motif["description"].lower())
        self.assertIn("rank-2", motif["description"].lower())


if __name__ == "__main__":
    unittest.main()
