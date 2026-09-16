from copy import deepcopy
from pathlib import Path
import json
import unittest

from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]


class QuestionsLayerTests(unittest.TestCase):
    def test_questions_are_loaded_with_initial_cross_motif_coverage(self):
        questions_path = ROOT / "data/questions.json"
        self.assertTrue(questions_path.exists(), "questions ledger should exist")
        if not questions_path.exists():
            return
        questions = json.loads(questions_path.read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(questions), 5)
        ids = [item["id"] for item in questions]
        self.assertEqual(len(ids), len(set(ids)))
        motifs = {motif for item in questions for motif in item.get("motifs", [])}
        for motif in (
            "active-intervention",
            "late-relevance",
            "bounded-observation",
            "structure-as-computation",
            "persistent-state",
        ):
            self.assertIn(motif, motifs)

        atlas = load_atlas(ROOT)
        self.assertIn("questions", atlas)
        self.assertEqual(atlas["questions"], questions)

    def test_validator_rejects_unknown_question_references_and_false_resolution(self):
        atlas = load_atlas(ROOT)
        broken = deepcopy(atlas)
        broken["questions"] = [
            {
                "id": "broken-question",
                "title": "Broken question",
                "state": "resolved",
                "motifs": ["does-not-exist"],
                "evidence": ["also-does-not-exist"],
                "competing_explanations": ["A", "B"],
                "known": ["Something"],
                "missing_discriminator": "A decisive measurement",
                "candidate_experiment": {
                    "design": "Run a controlled A/B experiment",
                    "cost": "small",
                    "outcomes": [
                        {"if": "A", "then": "A is favored"},
                        {"if": "B", "then": "B is favored"},
                    ],
                },
            }
        ]
        errors = validate_atlas(broken)
        text = "\n".join(errors)
        self.assertIn("unknown motif", text)
        self.assertIn("unknown evidence", text)
        self.assertIn("resolved", text)

    def test_validator_rejects_scoring_and_resolution_evidence_on_open_questions(self):
        atlas = load_atlas(ROOT)
        evidence_id = atlas["evidence"][0]["id"]
        motif_id = atlas["evidence"][0]["motifs"][0]
        broken = deepcopy(atlas)
        broken["questions"] = [
            {
                "id": "scored-question",
                "title": "Scored question",
                "state": "open",
                "motifs": [motif_id],
                "evidence": [evidence_id],
                "resolution_evidence": [evidence_id],
                "score": 0.9,
                "competing_explanations": ["A", "B"],
                "known": ["Something"],
                "missing_discriminator": "A decisive measurement",
                "candidate_experiment": {
                    "design": "Run a controlled A/B experiment",
                    "cost": "small",
                    "outcomes": [
                        {"if": "A", "then": "A becomes more plausible"},
                        {"if": "B", "then": "B becomes more plausible"},
                    ],
                },
            }
        ]
        text = "\n".join(validate_atlas(broken))
        self.assertIn("forbidden field", text)
        self.assertIn("resolution evidence", text)

    def test_static_atlas_exposes_questions_view(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        js_path = ROOT / "assets/questions.js"
        self.assertIn('data-view="questions"', html)
        self.assertIn('id="questions-content"', html)
        self.assertIn('assets/questions.js', html)
        self.assertTrue(js_path.exists(), "questions JavaScript should exist")
        if not js_path.exists():
            return
        js = js_path.read_text(encoding="utf-8")
        self.assertIn("data/questions.json", js)
        self.assertIn("function renderQuestions", js)
        self.assertIn("atlas.questions", js)
        self.assertNotIn("questionScore", js)


if __name__ == "__main__":
    unittest.main()
