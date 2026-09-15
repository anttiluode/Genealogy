from pathlib import Path
import unittest

from scripts.validate_data import load_atlas

ROOT = Path(__file__).resolve().parents[1]


class CreativeDSPPassTests(unittest.TestCase):
    def test_creative_dsp_pass_keeps_tools_and_rhetoric_separate(self):
        atlas = load_atlas(ROOT)
        pass_ids = {item["id"] for item in atlas["passes"]}
        self.assertIn("creative-dsp", pass_ids)

        nodes = {node["id"]: node for node in atlas["nodes"]}
        for node_id in ("AdelicPhaseFreezerVST", "ButSeriously", "DynamicalMRIlol"):
            self.assertIn(node_id, nodes)
            self.assertEqual(nodes[node_id]["usefulness"], "practical")

        adelic = nodes["AdelicPhaseFreezerVST"]
        self.assertIn("delay", adelic["survived"].lower())
        self.assertIn("bost", adelic["killed"].lower())

        seriously = nodes["ButSeriously"]
        self.assertIn("midi", seriously["survived"].lower())
        self.assertIn("preset", seriously["survived"].lower())

        mri = nodes["DynamicalMRIlol"]
        self.assertIn("heuristic", mri["killed"].lower())
        self.assertIn("recurrence", mri["survived"].lower())

    def test_adelic_to_but_seriously_is_explicit_implementation_descent(self):
        atlas = load_atlas(ROOT)
        edges = {
            (edge["source"], edge["target"], edge["type"]): edge
            for edge in atlas["edges"]
        }
        edge = edges[("AdelicPhaseFreezerVST", "ButSeriously", "inherits")]
        self.assertEqual(edge["confidence"], "high")
        self.assertIn("midi", edge["why"].lower())
        self.assertIn("preset", edge["why"].lower())

    def test_dynamical_mri_is_not_given_fake_takens_vst_ancestry(self):
        atlas = load_atlas(ROOT)
        edges = {(edge["source"], edge["target"]) for edge in atlas["edges"]}
        self.assertNotIn(("TakensPhaseSpaceVisualizerVST", "DynamicalMRIlol"), edges)
        self.assertNotIn(("PhaseSpaceVisualizerVST", "DynamicalMRIlol"), edges)


if __name__ == "__main__":
    unittest.main()
