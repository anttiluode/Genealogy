"""BrainRailRoad's separate, evidence-backed November 8 genealogy addition."""
import unittest
from pathlib import Path
from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]
PASS = "november-8-brainrailroad-hard-event-learning"
MOTIF = "nov8-hard-event-learning-is-not-guaranteed"

class BrainRailRoadGenealogyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.atlas = load_atlas(ROOT)

    def test_unique_census_and_curated_entry(self):
        self.assertEqual(validate_atlas(self.atlas), [])
        self.assertGreaterEqual(len(self.atlas["repos"]), 605)
        self.assertEqual(sum(r["name"] == "BrainRailRoad" for r in self.atlas["repos"]), 1)
        nodes = [n for n in self.atlas["nodes"] if n["id"] == "BrainRailRoad"]
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0]["pass_id"], PASS)
        self.assertIn("NOT learned", nodes[0]["killed"])

    def test_lineage_is_not_falsely_inherited_growth(self):
        edges = {(e["source"], e["target"], e["type"]) for e in self.atlas["edges"]}
        self.assertIn(("TurntableNeuron", "BrainRailRoad", "extracts"), edges)
        self.assertIn(("TurntableAISol", "BrainRailRoad", "extracts"), edges)
        for name in ("KasvavatKiskotSol", "KasvavatKiskotClaude"):
            self.assertIn((name, "BrainRailRoad", "converges"), edges)
            self.assertNotIn((name, "BrainRailRoad", "inherits"), edges)

    def test_control_and_negative_result_have_traceable_evidence(self):
        evs = [e for e in self.atlas["evidence"] if e["node"] == "BrainRailRoad"]
        self.assertEqual(len(evs), 2)
        for e in evs:
            self.assertIn(MOTIF, e["motifs"])
        gru = next(e for e in evs if e["id"] == "nov8-brainrailroad-gru-and-silence")
        self.assertEqual(gru["result"], "mixed")
        self.assertIn("railway", " ".join(gru["limitations"]).lower())
        self.assertEqual(gru["sample"]["count"], 5)

    def test_rescue_is_recorded_as_negative_learning_evidence(self):
        ev = next(e for e in self.atlas["evidence"] if e["id"] == "nov8-brainrailroad-rescue-clock-and-dead-credit")
        self.assertEqual(ev["result"], "mixed")
        self.assertEqual(ev["sample"]["count"], 512)
        self.assertIn("one seed", " ".join(ev["limitations"]).lower())
        self.assertIn("600", (ROOT / "docs/reviews/2026-11-08-brainrailroad.md").read_text(encoding="utf8"))

    def test_visible_chapter_and_written_audit(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn('data-mad-node="BrainRailRoad"', html)
        self.assertIn("605", html)
        self.assertTrue((ROOT / "docs/reviews/2026-11-08-brainrailroad.md").is_file())

if __name__ == "__main__":
    unittest.main()
