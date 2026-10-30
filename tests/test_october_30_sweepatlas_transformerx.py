"""October 30: distinct spatial tool and causal state-read transformer, with controls."""
from pathlib import Path
import unittest

from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]
PASS = "october-30-sweepatlas-transformerx"
NAMES = {"SweepAtlas", "TransformerX"}


class October30AtlasAndTransformerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.atlas = load_atlas(ROOT)
        cls.nodes = {n["id"]: n for n in cls.atlas["nodes"]}
        cls.evidence = {e["id"]: e for e in cls.atlas["evidence"]}

    def test_census_cards_and_validation(self):
        self.assertEqual(validate_atlas(self.atlas), [])
        self.assertGreaterEqual(len(self.atlas["repos"]), 565)
        self.assertEqual({n["id"] for n in self.atlas["nodes"] if n.get("pass_id") == PASS}, NAMES)
        for name in NAMES:
            self.assertEqual(sum(r["name"] == name for r in self.atlas["repos"]), 1)
            self.assertEqual(sum(n["id"] == name for n in self.atlas["nodes"]), 1)
            self.assertEqual(self.nodes[name]["pass_id"], PASS)
            self.assertEqual(next(r for r in self.atlas["repos"] if r["name"] == name)["inventory_status"], "reviewed")

    def test_causal_read_and_negative_limits(self):
        self.assertEqual(self.nodes["SweepAtlas"]["status"], "tool")
        self.assertEqual(self.nodes["TransformerX"]["status"], "experiment")
        self.assertIn("0.038", self.nodes["TransformerX"]["killed"])
        self.assertIn("23.96%", self.nodes["TransformerX"]["killed"])
        self.assertIn("SLAM", self.nodes["SweepAtlas"]["killed"])
        self.assertIn("not backfill", self.nodes["SweepAtlas"]["killed"])
        self.assertEqual(self.evidence["oct30-transformerx-history-read-disconnection"]["result"], "supports")
        self.assertEqual(self.evidence["oct30-transformerx-extra-router-no-clear-benefit"]["result"], "contradicts")
        self.assertEqual(self.evidence["oct30-sweepatlas-2d-video-mosaic-and-image-adjustments"]["node"], "SweepAtlas")

    def test_convergence_only_no_false_code_inheritance(self):
        edges = {(e["source"], e["target"], e["type"]) for e in self.atlas["edges"]}
        for expected in (("LoopAImemory", "TransformerX", "converges"),
                         ("RoundAndRound", "TransformerX", "converges"),
                         ("Loopcraft", "SweepAtlas", "converges")):
            self.assertIn(expected, edges)
        for forbidden in (("LoopAImemory", "TransformerX", "inherits"),
                          ("RoundAndRound", "TransformerX", "inherits"),
                          ("WorldModel", "SweepAtlas", "inherits"),
                          ("TransformerX", "SweepAtlas", "inherits")):
            self.assertNotIn(forbidden, edges)

    def test_wall_and_research_linkage(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn('id="oct30-atlas-transformerx"', html)
        self.assertLess(html.index('id="oct30-atlas-transformerx"'),
                        html.index('id="oct29-roundandround"'))
        for name in NAMES:
            self.assertIn(f'data-mad-node="{name}"', html)
            self.assertIn(f"https://github.com/anttiluode/{name}", readme)
        self.assertTrue((ROOT / "docs/reviews/2026-10-30-sweepatlas-transformerx.md").is_file())
        self.assertIn("data/passes/october-30-sweepatlas-transformerx.json", readme)
        questions = {q["id"] for q in self.atlas["questions"]}
        self.assertIn("oct30-history-helps-beyond-fair-recurrent-or-window-baselines", questions)
        self.assertIn("oct30-observed-atlas-vs-spatial-world-model", questions)


if __name__ == "__main__":
    unittest.main()
