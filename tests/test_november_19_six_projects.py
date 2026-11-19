import json
import unittest
from pathlib import Path
from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]
NAMES = {"LightScan", "FunWithOpticalLoops", "3", "PhaseLabyrinth", "SplatYou", "FireIntoSilence"}
PASS_FILE = "november-19-optical-loops-residue-and-silent-rhythms.json"

class November19SixProjectsTests(unittest.TestCase):
    def test_census_and_reviewed_nodes(self):
        atlas = load_atlas(ROOT)
        self.assertEqual([], validate_atlas(atlas))
        self.assertGreaterEqual(len(atlas["repos"]), 665)
        for name in NAMES:
            self.assertEqual(1, sum(x["name"] == name for x in atlas["repos"]), name)
            self.assertEqual(1, sum(x["id"] == name for x in atlas["nodes"]), name)
        self.assertEqual(1, sum(x["path"] == PASS_FILE for x in atlas["passes"]))

    def test_documented_connections_and_visible_wall(self):
        p = json.loads((ROOT / "data/passes" / PASS_FILE).read_text(encoding="utf-8"))
        edges = {(x["source"], x["target"]) for x in p["edges"]}
        self.assertTrue({("PerceptionLabAI", "FireIntoSilence"), ("FireIntoSilence", "PhaseLabyrinth"),
                         ("SplatWorld", "SplatYou"), ("LightScan", "SplatYou")} <= edges)
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn('id="nov19-optics-silence"', html)
        for name in NAMES:
            self.assertIn('data-mad-node="' + name + '"', html)
        self.assertIn("Physical diffuser reconstruction remains to be demonstrated", html)

if __name__ == "__main__":
    unittest.main()
