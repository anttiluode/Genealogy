import unittest
from pathlib import Path
from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]

class WaveFormerNovember18Tests(unittest.TestCase):
    def test_inventory_pass_and_unique_nodes(self):
        atlas = load_atlas(ROOT)
        self.assertEqual([], validate_atlas(atlas))
        self.assertGreaterEqual(len(atlas["repos"]), 659)
        for name in ("WaveFormer", "Qwenimagination"):
            self.assertEqual(1, sum(r["name"] == name for r in atlas["repos"]))
            self.assertEqual(1, sum(n["id"] == name for n in atlas["nodes"]))
        self.assertIn("november-18-waveformer-hybrid", {p["id"] for p in atlas["passes"]})

    def test_wall_has_caveats(self):
        atlas = load_atlas(ROOT)
        e = {x["id"]: x for x in atlas["evidence"]}
        self.assertEqual("supports", e["nov17-qwen-jspace-pending"]["result"])
        self.assertEqual("inconclusive", e["nov18-qwen-v7-category-control"]["result"])
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn('id="nov18-waveformer"', html)
        self.assertIn('data-mad-node="WaveFormer"', html)
        self.assertIn("ablating the wave head changes almost nothing", html)

if __name__ == "__main__":
    unittest.main()
