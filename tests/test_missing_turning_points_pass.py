from pathlib import Path
import unittest

from scripts.validate_data import load_atlas

ROOT = Path(__file__).resolve().parents[1]


class MissingTurningPointTests(unittest.TestCase):
    def test_missing_turning_points_are_curated(self):
        atlas = load_atlas(ROOT)
        nodes = {node["id"]: node for node in atlas["nodes"]}

        for node_id in ("ResonantCortex2", "-mp-ri", "InformationFlow", "SplatPack"):
            with self.subTest(node=node_id):
                self.assertIn(node_id, nodes)

        self.assertEqual(nodes["ResonantCortex2"]["status"], "ledger")
        self.assertIn("compilation", nodes["ResonantCortex2"]["killed"].lower())
        self.assertEqual(nodes["SplatPack"]["usefulness"], "practical")
        self.assertIn("residual", nodes["SplatPack"]["tags"])

    def test_documented_correction_and_extraction_edges_are_present(self):
        atlas = load_atlas(ROOT)
        edges = {(edge["source"], edge["target"], edge["type"]): edge for edge in atlas["edges"]}

        self.assertIn(("-mp-ri", "InformationFlow", "corrects"), edges)
        self.assertIn(("SplatWorld4", "SplatPack", "extracts"), edges)

    def test_field_computing_is_a_first_class_pass(self):
        atlas = load_atlas(ROOT)
        pass_ids = {item["id"] for item in atlas["passes"]}
        self.assertIn("field-computing", pass_ids)


if __name__ == "__main__":
    unittest.main()
