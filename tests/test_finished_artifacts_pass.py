from pathlib import Path
import unittest

from scripts.validate_data import load_atlas

ROOT = Path(__file__).resolve().parents[1]


class FinishedArtifactsPassTests(unittest.TestCase):
    def test_finished_creative_artifacts_are_curated(self):
        atlas = load_atlas(ROOT)
        nodes = {node["id"]: node for node in atlas["nodes"]}

        for node_id in ("Arborverb", "ArborBody", "AnttisDeepfake", "AIvideoFX"):
            with self.subTest(node=node_id):
                self.assertIn(node_id, nodes)

        self.assertEqual(nodes["Arborverb"]["usefulness"], "practical")
        self.assertEqual(nodes["ArborBody"]["usefulness"], "practical")
        self.assertIn("phase", " ".join(nodes["AnttisDeepfake"]["tags"]).lower())
        self.assertIn("refresh", nodes["AIvideoFX"]["claim"].lower())

    def test_documented_lineage_edges_are_present(self):
        atlas = load_atlas(ROOT)
        edges = {(edge["source"], edge["target"], edge["type"]): edge for edge in atlas["edges"]}

        self.assertIn(("FunctionalArbors", "ArborBody", "extracts"), edges)
        self.assertIn(("AnttisDeepfake", "AIvideoFX", "inherits"), edges)

    def test_finished_artifacts_are_a_first_class_pass(self):
        atlas = load_atlas(ROOT)
        pass_ids = {item["id"] for item in atlas["passes"]}
        self.assertIn("finished-creative-artifacts", pass_ids)


if __name__ == "__main__":
    unittest.main()
