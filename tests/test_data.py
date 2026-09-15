from pathlib import Path
import unittest
from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]

class AtlasDataTests(unittest.TestCase):
    def test_repository_data_is_valid(self):
        atlas = load_atlas(ROOT)
        self.assertEqual(validate_atlas(atlas), [])

    def test_curated_nodes_are_unique_and_have_known_statuses(self):
        atlas = load_atlas(ROOT)
        ids = [node["id"] for node in atlas["nodes"]]
        self.assertEqual(len(ids), len(set(ids)))
        allowed = {"idea-mine", "experiment", "negative", "ledger", "tool", "survivor", "active"}
        self.assertTrue(all(node["status"] in allowed for node in atlas["nodes"]))

    def test_edges_and_motifs_reference_existing_nodes(self):
        atlas = load_atlas(ROOT)
        ids = {node["id"] for node in atlas["nodes"]}
        for edge in atlas["edges"]:
            self.assertIn(edge["source"], ids)
            self.assertIn(edge["target"], ids)
        for motif in atlas["motifs"]:
            self.assertTrue(set(motif["nodes"]).issubset(ids))

if __name__ == "__main__":
    unittest.main()
