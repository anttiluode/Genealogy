import json
import unittest
from pathlib import Path
from scripts.validate_data import load_atlas, validate_atlas

ROOT=Path(__file__).resolve().parents[1]
NAMES=("SaturdayAfterRHproof","HEAD","SihtiAI","PredictiveSihtiV2","LazyRetrospectiveCreditAssignment")
PASS="november-21-sihti-head-and-retrospective-residue.json"

class November21SihtiTests(unittest.TestCase):
    def test_new_projects_once(self):
        atlas=load_atlas(ROOT)
        self.assertEqual([], validate_atlas(atlas))
        self.assertGreaterEqual(len(atlas["repos"]),672)
        self.assertEqual(1,sum(x["path"]==PASS for x in atlas["passes"]))
        for name in NAMES:
            self.assertEqual(1,sum(x["name"]==name for x in atlas["repos"]),name)
            self.assertEqual(1,sum(x["id"]==name for x in atlas["nodes"]),name)
    def test_special_top_lineage(self):
        payload=json.loads((ROOT/"data/passes"/PASS).read_text(encoding="utf-8"))
        edges={(e["source"],e["target"]) for e in payload["edges"]}
        self.assertTrue({("Sihti","SihtiAI"),("SihtiAI","PredictiveSihtiV2"),("PredictiveSihtiV2","LazyRetrospectiveCreditAssignment"),("SaturdayAfterRHproof","HEAD"),("HEAD","LazyRetrospectiveCreditAssignment")}<=edges)
        html=(ROOT/"index.html").read_text(encoding="utf-8")
        self.assertLess(html.index('id="nov21-sihti-lineage"'),html.index('id="nov20-clockfield-wificam"'))
        for name in NAMES:self.assertIn('data-mad-node="'+name+'"',html)
        self.assertIn('docs/sihti-lineage.md',html)
if __name__=="__main__":unittest.main()
