import json
import unittest
from pathlib import Path
from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]
PASS_FILE = "november-20-complex-clockfield-and-wificam.json"


class November20ClockfieldCameraTests(unittest.TestCase):
    def test_census_and_reviewed_nodes(self):
        atlas = load_atlas(ROOT)
        self.assertEqual([], validate_atlas(atlas))
        self.assertGreaterEqual(len(atlas["repos"]), 667)
        for name in ("ComplexClockfield", "WIFIcam"):
            self.assertEqual(1, sum(x["name"] == name for x in atlas["repos"]), name)
            self.assertEqual(1, sum(x["id"] == name for x in atlas["nodes"]), name)
        self.assertEqual(1, sum(x["path"] == PASS_FILE for x in atlas["passes"]))

    def test_two_branches_visible_and_scientific_limits_recorded(self):
        p = json.loads((ROOT / "data/passes" / PASS_FILE).read_text(encoding="utf-8"))
        edges = {(edge["source"], edge["target"]) for edge in p["edges"]}
        self.assertTrue({
            ("Clockfield", "ComplexClockfield"),
            ("phi-world-theory", "ComplexClockfield"),
            ("LightScan", "WIFIcam")
        } <= edges)
        clock = next(n for n in p["nodes"] if n["id"] == "ComplexClockfield")
        camera = next(n for n in p["nodes"] if n["id"] == "WIFIcam")
        self.assertIn("nonlinear vacuum", clock["killed"].lower())
        self.assertIn("independent", camera["survived"].lower())
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn('id="nov20-clockfield-wificam"', html)
        self.assertIn('data-mad-node="ComplexClockfield"', html)
        self.assertIn('data-mad-node="WIFIcam"', html)


if __name__ == "__main__":
    unittest.main()
