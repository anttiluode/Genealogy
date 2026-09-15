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

    def test_clockfield_pass_prunes_grand_claims_without_name_based_birth_edge(self):
        atlas = load_atlas(ROOT)
        pass_ids = {item["id"] for item in atlas["passes"]}
        self.assertIn("clockfield-pruning", pass_ids)
        edges = {(edge["source"], edge["target"], edge["type"]): edge for edge in atlas["edges"]}
        for source in ("ClockfieldBornRule", "ClockfieldCollapse", "ClockfieldBigBang", "Geometric-Neuron"):
            self.assertIn((source, "ClockfieldAsUniversalOperator", "converges"), edges)
            self.assertEqual(edges[(source, "ClockfieldAsUniversalOperator", "converges")]["confidence"], "high")
        self.assertIn(("Clockfield", "ClockfieldUnified", "converges"), edges)
        self.assertIn(("SimpsonsUniverse", "ClockfieldUnified", "corrects"), edges)
        self.assertNotIn(("BirthOfClockfield", "Clockfield", "inherits"), edges)
        self.assertNotIn(("BirthOfClockfield", "Clockfield", "forks"), edges)
        unified = next(node for node in atlas["nodes"] if node["id"] == "ClockfieldUnified")
        self.assertEqual(unified["status"], "survivor")
        killed = unified["killed"].lower()
        self.assertIn("1/137", killed)
        self.assertIn("gauge", killed)

    def test_machine_spine_uses_explicit_repository_lineage(self):
        atlas = load_atlas(ROOT)
        pass_ids = {item["id"] for item in atlas["passes"]}
        self.assertIn("machine-spine", pass_ids)
        ids = {node["id"] for node in atlas["nodes"]}
        self.assertIn("AnttisBrain2", ids)
        edges = {(edge["source"], edge["target"], edge["type"]): edge for edge in atlas["edges"]}
        self.assertIn(("AnttisBrain2", "HorizonNet", "inherits"), edges)
        for source in ("AnttisNeuron", "GrowingAnttisNeuron", "ActiveVectorNN"):
            self.assertIn((source, "NewMachine", "inherits"), edges)
            self.assertEqual(edges[(source, "NewMachine", "inherits")]["confidence"], "high")
        self.assertNotIn(("NewMachine", "FusionMachine", "inherits"), edges)

    def test_causal_memory_pass_keeps_motivation_separate_from_inheritance(self):
        atlas = load_atlas(ROOT)
        pass_ids = {item["id"] for item in atlas["passes"]}
        self.assertIn("causal-memory", pass_ids)
        ids = {node["id"] for node in atlas["nodes"]}
        for node_id in ("GelatinIsland", "JelloBrain", "SighImageSuper", "GeometricNeuronOriginReview", "OperaattoriAktiivinenDendriitti", "IttnasNoruen", "CausalHorizon"):
            self.assertIn(node_id, ids)
        edges = {(edge["source"], edge["target"], edge["type"]): edge for edge in atlas["edges"]}
        self.assertIn(("GelatinIsland", "JelloBrain", "inherits"), edges)
        for source in ("SighImageSuper", "Operaattori", "GeometricNeuronOriginReview"):
            self.assertIn((source, "OperaattoriAktiivinenDendriitti", "converges"), edges)
        for source in ("SighImageSuper", "Kompressori", "GeometricNeuronOriginReview", "OperaattoriAktiivinenDendriitti", "Operaattori"):
            self.assertIn((source, "IttnasNoruen", "converges"), edges)
        for source in ("AnttisBrain2", "SighImageSuper", "GeometricNeuronV24", "Operaattori", "OperaattoriJako", "Kompressori", "JelloBrain", "IttnasNoruen"):
            edge = edges[(source, "CausalHorizon", "converges")]
            self.assertEqual(edge["confidence"], "medium")

    def test_retention_economy_prices_memory_and_reuse(self):
        atlas = load_atlas(ROOT)
        pass_ids = {item["id"] for item in atlas["passes"]}
        self.assertIn("retention-economy", pass_ids)
        ids = {node["id"] for node in atlas["nodes"]}
        for node_id in ("Paper", "368", "ThinkingJello"):
            self.assertIn(node_id, ids)
        edges = {(edge["source"], edge["target"], edge["type"]): edge for edge in atlas["edges"]}
        self.assertIn(("JelloBrain", "Paper", "extracts"), edges)
        self.assertIn(("Paper", "368", "inherits"), edges)
        self.assertIn(("JelloBrain", "ThinkingJello", "inherits"), edges)
        self.assertIn(("GelatinIsland", "ThinkingJello", "inherits"), edges)
        memory = next(node for node in atlas["nodes"] if node["id"] == "368")
        self.assertIn("storage itself does nothing", memory["survived"].lower())
        self.assertIn("no recurrence", memory["killed"].lower())

if __name__ == "__main__":
    unittest.main()
