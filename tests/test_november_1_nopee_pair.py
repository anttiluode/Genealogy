"""November 1 Nopee experiments are distinct, source-linked entries."""
import unittest
from pathlib import Path
from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]
NAMES = {"Nopee", "NopeeClaude"}
PASS_ID = "november-1-nopee-dual-video-controls"


class NopeePairTests(unittest.TestCase):
    def test_two_curated_nodes_and_census(self):
        atlas = load_atlas(ROOT)
        self.assertEqual(validate_atlas(atlas), [])
        self.assertGreaterEqual(len(atlas["repos"]), 574)
        self.assertEqual(
            {node["id"] for node in atlas["nodes"] if node.get("pass_id") == PASS_ID},
            NAMES,
        )
        for name in NAMES:
            self.assertEqual(sum(repo["name"] == name for repo in atlas["repos"]), 1)
            self.assertEqual(sum(node["id"] == name for node in atlas["nodes"]), 1)
            self.assertEqual(
                next(repo for repo in atlas["repos"] if repo["name"] == name)["inventory_status"],
                "reviewed",
            )

    def test_controls_and_links_are_explicit(self):
        atlas = load_atlas(ROOT)
        nodes = {node["id"]: node for node in atlas["nodes"]}
        self.assertIn("0.03390", nodes["Nopee"]["survived"])
        self.assertIn("paused", nodes["NopeeClaude"]["killed"])
        self.assertIn("synthetic constants", nodes["Nopee"]["killed"])
        edges = [edge for edge in atlas["edges"] if edge["target"] in NAMES]
        self.assertTrue(any(e["source"] == "Sihti" and e["target"] == "Nopee" and e["type"] == "converges" for e in edges))
        self.assertTrue(any(e["source"] == "Nopee" and e["target"] == "NopeeClaude" and e["type"] == "converges" for e in edges))

    def test_wall_renders_both_navigation_targets(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn('id="nov1-nopee-pair"', html)
        for name in NAMES:
            self.assertIn('data-mad-node="' + name + '"', html)
            self.assertIn("https://github.com/anttiluode/" + name, readme)
        self.assertTrue((ROOT / "docs/reviews/2026-11-02-nopee-nopeeclaude.md").is_file())


if __name__ == "__main__":
    unittest.main()
