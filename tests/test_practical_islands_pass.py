from pathlib import Path
import unittest

from scripts.validate_data import load_atlas

ROOT = Path(__file__).resolve().parents[1]


class PracticalIslandsPassTests(unittest.TestCase):
    def test_practical_islands_exist_without_forced_ancestry(self):
        atlas = load_atlas(ROOT)
        pass_ids = {item["id"] for item in atlas["passes"]}
        self.assertIn("practical-islands", pass_ids)

        ids = {node["id"] for node in atlas["nodes"]}
        for node_id in (
            "PhaseSpaceVisualizerVST",
            "TinyAvatar",
            "Arborverb",
            "AnttisImageSynthVST",
            "PrimeCrystalVST",
        ):
            self.assertIn(node_id, ids)

        tiny = next(node for node in atlas["nodes"] if node["id"] == "TinyAvatar")
        self.assertEqual(tiny["usefulness"], "practical")
        self.assertIn("0.998", tiny["survived"])
        self.assertIn("0.81", tiny["survived"])

        arbor = next(node for node in atlas["nodes"] if node["id"] == "Arborverb")
        self.assertEqual(arbor["usefulness"], "practical")
        self.assertIn("0.999999998", arbor["survived"])
        self.assertIn("convolution", arbor["killed"].lower())

        prime = next(node for node in atlas["nodes"] if node["id"] == "PrimeCrystalVST")
        self.assertEqual(prime["usefulness"], "practical")
        self.assertIn("delay", prime["survived"].lower())
        self.assertIn("riemann", prime["killed"].lower())

    def test_useful_without_grand_theory_motif_spans_old_and_new_tools(self):
        atlas = load_atlas(ROOT)
        motifs = {motif["id"]: motif for motif in atlas["motifs"]}
        motif = motifs["useful-without-grand-theory"]
        self.assertTrue(
            {
                "PhaseSpaceVisualizerVST",
                "TakensPhaseSpaceVisualizerVST",
                "TinyAvatar",
                "Arborverb",
                "AnttisImageSynthVST",
                "LentoOrava",
                "TransientWaveCompiler",
            }.issubset(set(motif["nodes"]))
        )

    def test_tools_are_not_given_fake_lineage_edges(self):
        atlas = load_atlas(ROOT)
        edges = {(edge["source"], edge["target"]) for edge in atlas["edges"]}
        self.assertNotIn(("PhaseSpaceVisualizerVST", "TakensPhaseSpaceVisualizerVST"), edges)
        self.assertNotIn(("FunctionalArbors", "Arborverb"), edges)
        self.assertNotIn(("SplatWorld", "TinyAvatar"), edges)


if __name__ == "__main__":
    unittest.main()
