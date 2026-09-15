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

    def test_first_slice_has_meaningful_curated_content(self):
        atlas = load_atlas(ROOT)
        self.assertGreaterEqual(len(atlas["nodes"]), 25)
        self.assertGreaterEqual(len(atlas["edges"]), 20)
        self.assertGreaterEqual(len(atlas["motifs"]), 5)
        self.assertGreaterEqual(sum(node["usefulness"] == "practical" for node in atlas["nodes"]), 2)

    def test_modular_passes_are_merged_and_auditable(self):
        atlas = load_atlas(ROOT)
        pass_ids = {item["id"] for item in atlas["passes"]}
        self.assertIn("foundation", pass_ids)
        self.assertIn("geometric-ladder", pass_ids)
        node = next(node for node in atlas["nodes"] if node["id"] == "GeometricNeuronV21")
        self.assertEqual(node["pass_id"], "geometric-ladder")
        self.assertEqual(node["era"], "Autopsy & external reset")

    def test_geometric_ladder_keeps_real_corrections_without_fake_version_edges(self):
        atlas = load_atlas(ROOT)
        edges = {(edge["source"], edge["target"], edge["type"]) for edge in atlas["edges"]}
        self.assertIn(("GeometricNeuronV8", "GeometricNeuronV9", "corrects"), edges)
        self.assertIn(("GeometricNeuronV21", "GeometricNeuronV24", "corrects"), edges)
        self.assertNotIn(("GeometricNeuronV2", "GeometricNeuronV4", "inherits"), edges)
        self.assertNotIn(("GeometricNeuronV2", "GeometricNeuronV4", "forks"), edges)

    def test_splat_pass_replaces_speculative_worldmodel_edge_with_explicit_lineage(self):
        atlas = load_atlas(ROOT)
        pass_ids = {item["id"] for item in atlas["passes"]}
        self.assertIn("splat-world", pass_ids)
        edges = {(edge["source"], edge["target"], edge["type"]): edge for edge in atlas["edges"]}
        self.assertNotIn(("Splatworld2", "WorldModel", "inherits"), edges)
        for source in ("SplatWorld", "SplatField", "TheSplat5", "SplatNeuron", "SplatNeuronPlusField"):
            self.assertIn((source, "WorldModel", "inherits"), edges)
            self.assertEqual(edges[(source, "WorldModel", "inherits")]["confidence"], "high")
        self.assertIn(("Splatworld2", "Splatworld3", "inherits"), edges)
        self.assertIn(("ObjektiYksi", "Splatworld3", "converges"), edges)
        self.assertIn(("SlapstackBet8", "SlapStack9", "forks"), edges)

if __name__ == "__main__":
    unittest.main()
