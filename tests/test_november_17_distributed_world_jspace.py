import json
import unittest
from pathlib import Path
from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]
PASS = "november-17-distributed-context-and-jspace.json"
NAMES = {"TuftSheet", "TuftSheetSol", "Qwenimagination"}

class DistributedWorldAndJspaceTests(unittest.TestCase):
    def test_inventory_schema_and_pass(self):
        atlas = load_atlas(ROOT)
        self.assertEqual([], validate_atlas(atlas))
        self.assertEqual(656, len(atlas["repos"]))
        for name in NAMES:
            self.assertEqual(1, sum(r["name"] == name and r["inventory_status"] == "reviewed" for r in atlas["repos"]))
            self.assertEqual(1, sum(n["id"] == name for n in atlas["nodes"]))
        self.assertEqual(1, sum(p["path"] == PASS for p in atlas["passes"]))

    def test_lineage_and_limits(self):
        p = json.loads((ROOT / "data/passes" / PASS).read_text(encoding="utf-8"))
        self.assertEqual(NAMES, {x["id"] for x in p["nodes"]})
        edges = {(x["source"], x["target"]):x["type"] for x in p["edges"]}
        self.assertEqual("inherits", edges["WaveCortex", "TuftSheet"])
        self.assertEqual("converges", edges["TuftSheet", "TuftSheetSol"])
        self.assertEqual("extracts", edges["TuftSheet", "Qwenimagination"])
        nodes = {x["id"]:x for x in p["nodes"]}
        self.assertIn("22/32", nodes["TuftSheet"]["killed"])
        self.assertIn("hand-coded", nodes["TuftSheetSol"]["killed"])
        self.assertIn("No real pretrained Qwen", nodes["Qwenimagination"]["killed"])

    def test_site_and_docs(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn('id="nov17-distributed-imagination"', html)
        self.assertLess(html.index('id="nov17-distributed-imagination"'), html.index('id="nov17-synthetic-qualia"'))
        for name in NAMES:
            self.assertIn('data-mad-node="' + name + '"', html)
        for path in ("README.md", "RESEARCH_LOG.md", "docs/reviews/2026-11-17-distributed-context-and-jspace.md"):
            self.assertIn("Qwenimagination", (ROOT / path).read_text(encoding="utf-8"))

if __name__ == "__main__":
    unittest.main()
