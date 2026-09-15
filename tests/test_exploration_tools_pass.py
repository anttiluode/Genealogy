from pathlib import Path
import unittest

from scripts.validate_data import load_atlas

ROOT = Path(__file__).resolve().parents[1]


class ExplorationToolsPassTests(unittest.TestCase):
    def test_exploration_tools_preserve_useful_views_and_boundaries(self):
        atlas = load_atlas(ROOT)
        pass_ids = {item["id"] for item in atlas["passes"]}
        self.assertIn("exploration-tools", pass_ids)

        nodes = {node["id"]: node for node in atlas["nodes"]}
        for node_id in (
            "PhaseSpaceVisualizer",
            "WignerEEG",
            "CircularEEGMoirePatternVisualizer",
            "WaveNeuronMusicVisualizer",
            "LLM-Studio",
        ):
            self.assertIn(node_id, nodes)
            self.assertEqual(nodes[node_id]["usefulness"], "practical")

        wigner = nodes["WignerEEG"]
        self.assertIn("explor", wigner["survived"].lower())
        self.assertIn("non-classical", wigner["killed"].lower())

        moire = nodes["CircularEEGMoirePatternVisualizer"]
        self.assertIn("synthetic", moire["killed"].lower())
        self.assertIn("shader", moire["survived"].lower())

        studio = nodes["LLM-Studio"]
        self.assertIn("train", studio["survived"].lower())
        self.assertIn("heatmap", studio["survived"].lower())

    def test_old_python_phase_visualizer_does_not_get_name_based_vst_edge(self):
        atlas = load_atlas(ROOT)
        edges = {(edge["source"], edge["target"]) for edge in atlas["edges"]}
        self.assertNotIn(("PhaseSpaceVisualizer", "PhaseSpaceVisualizerVST"), edges)
        self.assertNotIn(("PhaseSpaceVisualizer", "TakensPhaseSpaceVisualizerVST"), edges)

    def test_seeing_structure_is_not_explaining_structure_motif(self):
        atlas = load_atlas(ROOT)
        motifs = {motif["id"]: motif for motif in atlas["motifs"]}
        motif = motifs["seeing-structure-is-not-explaining-structure"]
        self.assertTrue(
            {
                "PhaseSpaceVisualizer",
                "WignerEEG",
                "CircularEEGMoirePatternVisualizer",
                "DynamicalMRIlol",
                "EEGTools",
            }.issubset(set(motif["nodes"]))
        )


if __name__ == "__main__":
    unittest.main()
