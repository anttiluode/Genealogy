"""BrahSol/BrahClaude: two reviewed cards, a live chapter, and conservative evidence."""
import unittest
from pathlib import Path
from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]
PASS = "november-3-brah-ping-and-route-memory"
NAMES = {"BrahSol", "BrahClaude"}
MOTIF = "nov3-ping-read-backaction"


class BrahPairTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.atlas = load_atlas(ROOT)

    def test_inventoried_once_and_pass_enabled(self):
        self.assertEqual(validate_atlas(self.atlas), [])
        self.assertGreaterEqual(len(self.atlas["repos"]), 580)
        self.assertEqual(
            {x["id"] for x in self.atlas["nodes"] if x.get("pass_id") == PASS},
            NAMES)
        for name in NAMES:
            self.assertEqual(sum(x["name"] == name for x in self.atlas["repos"]), 1)
            self.assertEqual(sum(x["id"] == name for x in self.atlas["nodes"]), 1)
            self.assertEqual(next(x for x in self.atlas["repos"] if x["name"] == name)["inventory_status"],"reviewed")

    def test_different_experiments_and_negative_controls(self):
        nodes = {x["id"]: x for x in self.atlas["nodes"]}
        self.assertIn("forgetting", nodes["BrahSol"]["survived"])
        self.assertIn("Hebbian", nodes["BrahSol"]["killed"])
        self.assertIn("0.02571", nodes["BrahSol"]["survived"])
        self.assertIn("0.1008", nodes["BrahSol"]["survived"])
        self.assertIn("99.6%", nodes["BrahClaude"]["survived"])
        self.assertIn("invertible", nodes["BrahClaude"]["killed"])
        self.assertIn("G1", nodes["BrahClaude"]["killed"])
        self.assertIn("G4", nodes["BrahClaude"]["killed"])

    def test_lineage_and_motif(self):
        edges = [x for x in self.atlas["edges"] if x.get("pass_id") == PASS]
        self.assertTrue(any(x["source"]=="PerceptionLab" and x["target"]=="BrahSol" and x["type"]=="inherits" for x in edges))
        self.assertTrue(any(x["source"]=="Sihti" and x["target"]=="BrahClaude" and x["type"]=="converges" for x in edges))
        self.assertTrue(any(x["source"]=="BrahSol" and x["target"]=="BrahClaude" and x["type"]=="converges" for x in edges))
        motifs = {x["id"]: x for x in self.atlas["motifs"]}
        self.assertTrue(NAMES <= set(motifs[MOTIF]["nodes"]))

    def test_evidence_and_unresolved_question(self):
        ev = {x["id"]: x for x in self.atlas["evidence"]}
        ids = {"nov3-brahsol-active-probing-and-forgetting",
               "nov3-brahclaude-temporal-route-gates"}
        self.assertTrue(ids <= ev.keys())
        for key in ids:
            self.assertEqual(ev[key]["result"],"mixed")
        q = next(x for x in self.atlas["questions"] if x["id"]=="nov3-route-addressability-and-destructive-reading")
        self.assertEqual(q["state"],"open")
        self.assertEqual(set(q["evidence"]),ids)

    def test_wall_and_review(self):
        wall=(ROOT/"index.html").read_text(encoding="utf-8")
        readme=(ROOT/"README.md").read_text(encoding="utf-8")
        self.assertIn('id="nov3-brah-pingers"',wall)
        for name in NAMES:
            self.assertIn('data-mad-node="'+name+'"',wall)
            self.assertIn("https://github.com/anttiluode/"+name,readme)
        review=ROOT/"docs/reviews/2026-11-03-brahsol-brahclaude-route-interrogation.md"
        self.assertTrue(review.is_file())
        self.assertIn("8.8404",review.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
