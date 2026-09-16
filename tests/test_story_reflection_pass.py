from pathlib import Path
import unittest

from scripts.validate_data import load_atlas

ROOT = Path(__file__).resolve().parents[1]


class StoryReflectionPassTests(unittest.TestCase):
    def test_story_is_cataloged_as_narrative_reflection(self):
        atlas = load_atlas(ROOT)
        pass_ids = {item["id"] for item in atlas["passes"]}
        self.assertIn("story-reflection", pass_ids)

        nodes = {node["id"]: node for node in atlas["nodes"]}
        self.assertIn("Story", nodes)
        node = nodes["Story"]
        self.assertEqual(node["family"], "meta-narrative")
        self.assertEqual(node["usefulness"], "conceptual")
        self.assertIn("fiction", node["tags"])
        self.assertIn("not scientific evidence", node["killed"].lower())
        self.assertIn("same seed", node["claim"].lower())

    def test_story_has_documented_brain_ai_lineage_without_claiming_science(self):
        atlas = load_atlas(ROOT)
        edges = {(edge["source"], edge["target"], edge["type"]): edge for edge in atlas["edges"]}
        self.assertIn(("AnttisNeuron", "Story", "converges"), edges)
        self.assertIn(("TransformerStudy", "Story", "converges"), edges)

        nodes = {node["id"]: node for node in atlas["nodes"]}
        node = nodes["Story"]
        self.assertIn("brain", node["claim"].lower())
        self.assertIn("ai", node["claim"].lower())


if __name__ == "__main__":
    unittest.main()
