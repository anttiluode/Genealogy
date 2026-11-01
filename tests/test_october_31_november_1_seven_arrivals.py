"""Seven newly indexed late-October/early-November repository arrivals."""
import unittest
from pathlib import Path
from scripts.validate_data import load_atlas, validate_atlas
ROOT=Path(__file__).resolve().parents[1]
NAMES={"2729","TheCombRedux","VHSImageStitch","CortexWaveguideLens","Sihtiimagemodel6","JanusMultiscalePhaseLensSol","Sihtiimagemodel7"}
class TestSevenArrivals(unittest.TestCase):
    def test_census_and_nodes(self):
        a=load_atlas(ROOT)
        self.assertEqual(validate_atlas(a),[])
        self.assertEqual(len(a["repos"]),572)
        self.assertEqual({n["id"] for n in a["nodes"] if n.get("pass_id")=="october-31-november-1-seven-arrivals"},NAMES)
        for name in NAMES:
            self.assertEqual(sum(r["name"]==name for r in a["repos"]),1)
            self.assertEqual(sum(n["id"]==name for n in a["nodes"]),1)
    def test_wall(self):
        html=(ROOT/"index.html").read_text(encoding="utf-8")
        readme=(ROOT/"README.md").read_text(encoding="utf-8")
        self.assertLess(html.index('id="oct31-nov1-seven-arrivals"'),html.index('id="oct30-atlas-transformerx"'))
        for n in NAMES:
            self.assertIn('data-mad-node="'+n+'"',html)
            self.assertIn("https://github.com/anttiluode/"+n,readme)
        self.assertTrue((ROOT/"docs/reviews/2026-11-01-seven-arrivals.md").is_file())
if __name__=="__main__": unittest.main()
