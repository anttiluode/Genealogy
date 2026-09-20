from pathlib import Path
import unittest

from scripts.validate_data import load_atlas

ROOT = Path(__file__).resolve().parents[1]


class EEGInstrumentsPassTests(unittest.TestCase):
    def test_eeg_instruments_keep_software_and_interpretation_separate(self):
        atlas = load_atlas(ROOT)
        pass_ids = {item["id"] for item in atlas["passes"]}
        self.assertIn("eeg-instruments", pass_ids)

        ids = {node["id"] for node in atlas["nodes"]}
        for node_id in (
            "PerceptionLab",
            "EEGTools",
            "EEGBrainSourceReconstructionTool",
            "EEGFlowchartPlus3DBrain",
            "KoopmanEEGExplorer",
            "EEG2AUDIO",
            "RealtimeEEG3Dsystem",
            "RegionalAttractorExplorer",
        ):
            self.assertIn(node_id, ids)

        # PerceptionLab is intentionally reused from the foundation atlas rather
        # than duplicated in this pass; the seven nodes below are the new records.
        pass_node_ids = {
            node["id"]
            for node in atlas["nodes"]
            if node.get("pass_id") == "eeg-instruments"
        }
        self.assertNotIn("PerceptionLab", pass_node_ids)
        self.assertEqual(len(pass_node_ids), 7)

        source = next(node for node in atlas["nodes"] if node["id"] == "EEGBrainSourceReconstructionTool")
        self.assertEqual(source["usefulness"], "practical")
        self.assertIn("template", source["killed"].lower())
        self.assertIn("medical", source["killed"].lower())

        koopman = next(node for node in atlas["nodes"] if node["id"] == "KoopmanEEGExplorer")
        self.assertIn("13", koopman["killed"])
        self.assertIn("replication", koopman["killed"].lower())

        realtime = next(node for node in atlas["nodes"] if node["id"] == "RealtimeEEG3Dsystem")
        self.assertIn("prove", realtime["killed"].lower())
        self.assertIn("visual", realtime["survived"].lower())

    def test_instrument_boundary_motif_spans_honest_and_hype_heavy_tools(self):
        atlas = load_atlas(ROOT)
        motifs = {motif["id"]: motif for motif in atlas["motifs"]}
        motif = motifs["instrument-survives-interpretation"]
        self.assertTrue(
            {
                "PerceptionLab",
                "EEGTools",
                "EEGBrainSourceReconstructionTool",
                "EEGFlowchartPlus3DBrain",
                "KoopmanEEGExplorer",
                "EEG2AUDIO",
                "RealtimeEEG3Dsystem",
                "RegionalAttractorExplorer",
            }.issubset(set(motif["nodes"]))
        )
        self.assertIn("22.0-frame", motif["description"])

    def test_thematic_similarity_does_not_create_fake_eeg_lineage(self):
        atlas = load_atlas(ROOT)
        edges = {(edge["source"], edge["target"]) for edge in atlas["edges"]}
        self.assertNotIn(("EEGTools", "RealtimeEEG3Dsystem"), edges)
        self.assertNotIn(("EEGBrainSourceReconstructionTool", "EEGFlowchartPlus3DBrain"), edges)
        self.assertNotIn(("PerceptionLab", "EEGTools"), edges)


if __name__ == "__main__":
    unittest.main()
