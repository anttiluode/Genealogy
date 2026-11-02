"""November 2 Computing Beach convergence: two existing census rows, distinct mechanisms, and a fair next gate."""
from pathlib import Path
import unittest

from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]
PASS = "november-2-computing-beach-convergence"
BEACHES = {"ComputingBeachSol", "ComputingBeachClaude"}


class ComputingBeachGenealogyTests(unittest.TestCase):
    def setUp(self):
        self.atlas = load_atlas(ROOT)

    def test_two_existing_repos_promoted_without_duplication(self):
        self.assertEqual(validate_atlas(self.atlas), [])
        self.assertGreaterEqual(len(self.atlas["repos"]), 577)
        self.assertEqual(
            {n["id"] for n in self.atlas["nodes"] if n.get("pass_id") == PASS},
            BEACHES,
        )
        for name in BEACHES:
            self.assertEqual(sum(r["name"] == name for r in self.atlas["repos"]), 1)
            self.assertEqual(sum(n["id"] == name for n in self.atlas["nodes"]), 1)
            row = next(r for r in self.atlas["repos"] if r["name"] == name)
            self.assertEqual(row["inventory_status"], "reviewed")

    def test_source_reported_success_and_failure_are_distinct(self):
        n = {n["id"]: n for n in self.atlas["nodes"]}
        self.assertIn("62/64", n["ComputingBeachSol"]["survived"])
        self.assertIn("7/8", n["ComputingBeachSol"]["killed"])
        self.assertIn("0.70–0.75", n["ComputingBeachClaude"]["survived"])
        self.assertIn("global evaluation", n["ComputingBeachClaude"]["killed"])
        relevant = [e for e in self.atlas["edges"] if e.get("pass_id") == PASS]
        self.assertTrue(any(e["source"] == "WallMemoryLaw" and e["target"] == "ComputingBeachSol" and e["type"] == "inherits" for e in relevant))
        self.assertTrue(any(e["source"] == "WallMemoryLaw" and e["target"] == "ComputingBeachClaude" and e["type"] == "inherits" for e in relevant))
        self.assertTrue(any(e["source"] == "ComputingBeachSol" and e["target"] == "ComputingBeachClaude" and e["type"] == "converges" for e in relevant))

    def test_evidence_question_and_treatise(self):
        ev = [e for e in self.atlas["evidence"] if e["id"].startswith("nov2-")]
        self.assertEqual(len(ev), 6)
        question = next(q for q in self.atlas["questions"] if q["id"] == "nov2-written-operator-vs-ordinary-weights")
        self.assertEqual(question["state"], "open")
        self.assertEqual(len(question["candidate_experiment"]["outcomes"]), 2)
        self.assertIn("RNN", question["candidate_experiment"]["design"])
        treatise = ROOT / "docs/reviews/2026-11-02-the-beach-that-remembered.md"
        self.assertTrue(treatise.is_file())
        essay = treatise.read_text(encoding="utf-8")
        self.assertIn("The durable object was never the sand", essay)
        self.assertIn("what we have not", essay.lower())

    def test_landing_wall_navigation(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn('id="nov2-computing-beach"', html)
        for name in BEACHES:
            self.assertIn('data-mad-node="' + name + '"', html)
            self.assertIn("https://github.com/anttiluode/" + name, readme)
        self.assertIn("2026-11-02-the-beach-that-remembered.md", html)


if __name__ == "__main__":
    unittest.main()
