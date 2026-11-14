from pathlib import Path
import json
import unittest
from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]
PASS = "november-14-slimebody-physical-pumping.json"

class SlimeBodyGenealogyTests(unittest.TestCase):
    def test_slimebody_is_curated_once_and_atlas_valid(self):
        atlas = load_atlas(ROOT)
        self.assertEqual([], validate_atlas(atlas))
        self.assertEqual(1, sum(r["name"] == "SlimeBody" for r in atlas["repos"]))
        self.assertEqual(1, sum(n["id"] == "SlimeBody" for n in atlas["nodes"]))
        self.assertEqual("reviewed", next(r["inventory_status"] for r in atlas["repos"] if r["name"] == "SlimeBody"))
        p = json.loads((ROOT / "data/passes" / PASS).read_text(encoding="utf-8"))
        self.assertEqual(["SlimeBody"], [n["id"] for n in p["nodes"]])
        self.assertIn("12.7%", p["nodes"][0]["survived"])
        self.assertIn("not pump work", p["nodes"][0]["killed"])
        self.assertIn("Taylor dispersion", p["nodes"][0]["killed"])
        self.assertEqual({"Limasieni", "ElavaMatriisiClaude", "GelatinIsland"}, {e["source"] for e in p["edges"]})
        self.assertTrue(all(e["type"] == "converges" for e in p["edges"]))

    def test_wall_and_readme_explain_the_gate(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn('id="nov14-slimebody"', html)
        self.assertIn('data-mad-node="SlimeBody"', html)
        self.assertIn("data/passes/" + PASS, html)
        self.assertIn("anttiluode/SlimeBody", readme)
        self.assertIn("unequal", readme.lower())

if __name__ == "__main__":
    unittest.main()
