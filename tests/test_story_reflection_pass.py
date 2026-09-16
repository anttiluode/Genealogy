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
        self.assertIn("meta-reflection", node["tags"])
        self.assertIn("not scientific evidence", node["killed"].lower())
        self.assertIn("same seed", node["claim"].lower())

    def test_story_records_the_ai_brain_theme_without_inventing_ancestry(self):
        atlas = load_atlas(ROOT)
        nodes = {node["id"]: node for node in atlas["nodes"]}
        node = nodes["Story"]
        self.assertIn("brain", node["claim"].lower())
        self.assertIn("ai", node["claim"].lower())

        story_edges = [
            edge for edge in atlas["edges"]
            if edge["source"] == "Story" or edge["target"] == "Story"
        ]
        self.assertEqual(story_edges, [])


if __name__ == "__main__":
    unittest.main()
