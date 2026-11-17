import unittest, json
from pathlib import Path
from scripts.validate_data import load_atlas, validate_atlas
ROOT=Path(__file__).resolve().parents[1]
NAMES={"WaveComputer","WaveComputerAstra","ApicalRuleReversalMachine","WaveCortex","SyntheticQualia"}
PASS="november-17-synthetic-qualia-wave-cortex.json"

class November17QualiaTests(unittest.TestCase):
    def test_census_curated_and_valid(self):
        a=load_atlas(ROOT)
        self.assertEqual([],validate_atlas(a))
        self.assertEqual(656,len(a["repos"]))
        for name in NAMES|{"QualiaAstra","QualiaClaude","QualeX"}:
            self.assertEqual(1,sum(r["name"]==name for r in a["repos"]))
        for name in NAMES:
            self.assertEqual(1,sum(n["id"]==name for n in a["nodes"]))
        self.assertEqual(1,sum(p["path"]==PASS for p in a["passes"]))
    def test_edges_and_synthesis(self):
        p=json.loads((ROOT/"data/passes"/PASS).read_text(encoding="utf-8"))
        e={(x["source"],x["target"]):x["type"] for x in p["edges"]}
        self.assertEqual("inherits",e["QualiaClaude","WaveComputer"])
        self.assertEqual("inherits",e["WaveComputer","WaveCortex"])
        self.assertEqual("inherits",e["ApicalRuleReversalMachine","WaveCortex"])
        self.assertEqual("converges",e["WaveComputerAstra","WaveCortex"])
        self.assertEqual("extracts",e["WaveCortex","SyntheticQualia"])
        paper=next(x for x in p["nodes"] if x["id"]=="SyntheticQualia")
        self.assertEqual("ledger",paper["status"])
        self.assertIn("No assay establishes subjective experience",paper["killed"])
    def test_falsifiers_are_in_evidence_layer(self):
        ev={e["id"]:e for e in json.loads((ROOT/"data/evidence.json").read_text(encoding="utf-8"))}
        for name in ("nov17-astra-accuracy-negative","nov17-wavecortex-scalar-negative"):
            self.assertEqual("contradicts",ev[name]["result"])
            self.assertTrue(ev[name]["controls"])
        q=json.loads((ROOT/"data/questions.json").read_text(encoding="utf-8"))
        self.assertEqual("open",next(x["state"] for x in q if x["id"]=="nov17-persistent-inner-world"))
    def test_wall_and_review(self):
        html=(ROOT/"index.html").read_text(encoding="utf-8")
        self.assertIn('id="nov17-synthetic-qualia"',html)
        self.assertIn('id="nov16-qualia"',html)
        self.assertLess(html.index('id="nov17-synthetic-qualia"'),html.index('id="nov16-qualia"'))
        for name in NAMES:
            self.assertIn('data-mad-node="'+name+'"',html)
        for filename in ("README.md","RESEARCH_LOG.md","docs/reviews/2026-11-17-synthetic-qualia.md"):
            s=(ROOT/filename).read_text(encoding="utf-8")
            self.assertIn("SyntheticQualia",s)
            self.assertIn("WaveCortex",s)

if __name__=="__main__":
    unittest.main()
