from pathlib import Path
import json
import unittest
from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]
PASS = "november-15-perceptionlab-fossil-bed.json"


class PerceptionLabFossilBedTests(unittest.TestCase):
    def test_pass_is_curated_once_and_atlas_valid(self):
        atlas = load_atlas(ROOT)
        self.assertEqual([], validate_atlas(atlas))
        self.assertEqual(1, sum(r["name"] == "PerceptionLabNodes" for r in atlas["repos"]))
        self.assertEqual("reviewed", next(r["inventory_status"] for r in atlas["repos"] if r["name"] == "PerceptionLabNodes"))
        self.assertEqual(1, sum(n["id"] == "PerceptionLabNodes" for n in atlas["nodes"]))
        p = json.loads((ROOT / "data/passes" / PASS).read_text(encoding="utf-8"))
        node = p["nodes"][0]
        self.assertIn("22.17", node["survived"])
        self.assertIn("59-step", node["survived"])
        self.assertIn("bit-identical", node["killed"])
        self.assertIn("interpretive", node["killed"])
        types = {(e["source"], e["target"]): e["type"] for e in p["edges"]}
        self.assertEqual("corrects", types[("PerceptionLab", "PerceptionLabNodes")])
        self.assertEqual("converges", types[("PerceptionLab", "SighImageSuper")])
        self.assertIn("no code inheritance", next(e["why"] for e in p["edges"] if e["target"] == "SighImageSuper"))

    def test_evidence_records_are_reruns_with_controls(self):
        ev = {e["id"]: e for e in json.loads((ROOT / "data/evidence.json").read_text(encoding="utf-8"))}
        for key, result in (("nov15-pl-wavefield-headless-calibration", "supports"),
                            ("nov15-pl-ecg-moebius-feedback-inert", "contradicts"),
                            ("nov15-pl-jewishstar-avalanche-suppressed", "contradicts")):
            self.assertEqual(result, ev[key]["result"])
            self.assertTrue(ev[key]["controls"])
            self.assertIn("rerun", ev[key]["replication"])

    def test_wall_readme_and_log_link_back(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        log = (ROOT / "RESEARCH_LOG.md").read_text(encoding="utf-8")
        self.assertIn('id="nov15-perceptionlab-nodes"', html)
        self.assertIn('data-mad-node="PerceptionLabNodes"', html)
        self.assertIn("data/passes/" + PASS, html)
        self.assertIn("anttiluode.github.io/PerceptionLabNodes", html)
        self.assertIn("anttiluode/PerceptionLabNodes", readme)
        self.assertIn("PerceptionLabNodes", log)
        self.assertNotIn("KNOBLINE", html + readme + log)


if __name__ == "__main__":
    unittest.main()
