"""October 19 SihtiBrain/AIBrain lineage: five cards and bounded receipts."""
from pathlib import Path
import unittest

from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]
PASS_ID = "october-19-sihtibrain-to-ai-query-memory"
PROJECTS = {"SihtiBrain", "SihtiBrainV2", "SihtibrainV3", "AIBrain", "AIbrainV2"}
RECEIPTS = {
    "oct19-sihtibrain-soma-hidden-modes",
    "oct19-sihtibrain-real-time-credit-baseline",
    "oct19-v2-echo-and-persistent-wire",
    "oct19-v2-preregistered-calcium-advantage-fail",
    "oct19-v3-complementary-probe-vs-static",
    "oct19-v3-phase-averaged-tracking-cancel",
    "oct19-aibrain-connection-memory-interference",
    "oct19-aibrainv2-matched-graph-retention",
    "oct19-aibrainv2-normalization-and-indexed-ceiling",
}


class October19BrainLineageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.atlas = load_atlas(ROOT)

    def test_all_data_links_and_schemas_remain_valid(self):
        self.assertEqual(validate_atlas(self.atlas), [])

    def test_five_distinct_cards_are_in_one_october19_pass(self):
        nodes = [n for n in self.atlas["nodes"] if n.get("pass_id") == PASS_ID]
        self.assertEqual({n["id"] for n in nodes}, PROJECTS)
        self.assertEqual(len(nodes), 5)
        self.assertEqual([n["era_order"] for n in nodes], list(range(136, 141)))
        inventory = {r["name"]: r for r in self.atlas["repos"]}
        for name in PROJECTS:
            self.assertIn(name, inventory)
            self.assertEqual(inventory[name]["inventory_status"], "reviewed")

    def test_all_nine_results_are_traceable_and_show_limitations(self):
        evidence = {e["id"]: e for e in self.atlas["evidence"]}
        for key in RECEIPTS:
            self.assertIn(key, evidence)
            self.assertIn(evidence[key]["node"], PROJECTS)
            self.assertTrue(evidence[key]["source"].startswith("https://github.com/anttiluode/"))
            self.assertTrue(evidence[key]["controls"])
            self.assertTrue(evidence[key]["limitations"])
        self.assertEqual(evidence["oct19-v2-preregistered-calcium-advantage-fail"]["result"], "contradicts")
        self.assertEqual(evidence["oct19-v3-phase-averaged-tracking-cancel"]["result"], "contradicts")
        self.assertEqual(evidence["oct19-aibrainv2-normalization-and-indexed-ceiling"]["result"], "mixed")

    def test_distinct_stopping_boundaries_remain_in_cards(self):
        by_id = {n["id"]: n for n in self.atlas["nodes"]}
        self.assertIn("three-factor", by_id["SihtiBrain"]["killed"])
        self.assertIn("62.13%", by_id["SihtiBrainV2"]["killed"])
        self.assertIn("0.781", by_id["SihtibrainV3"]["killed"])
        self.assertIn("42.5%", by_id["AIBrain"]["killed"])
        self.assertIn("53.4%", by_id["AIbrainV2"]["killed"])
        self.assertIn("73.9%", by_id["AIbrainV2"]["killed"])

    def test_questions_remain_open_and_demand_simpler_controls(self):
        questions = {q["id"]: q for q in self.atlas["questions"]}
        for qid in ("oct19-operator-read-beyond-normalization-and-index",
                    "oct19-phase-aware-probes-vs-velocity-tracking"):
            self.assertEqual(questions[qid]["state"], "open")
            self.assertTrue(questions[qid]["competing_explanations"])
            self.assertGreaterEqual(len(questions[qid]["candidate_experiment"]["outcomes"]), 2)

    def test_motifs_capture_both_successes_and_failures(self):
        motifs = {m["id"]: m for m in self.atlas["motifs"]}
        for mid in ("oct19-distributed-visibility-and-active-probing",
                    "oct19-local-credit-vs-simpler-event",
                    "oct19-queryable-operator-memory-interference"):
            self.assertIn(mid, motifs)
        e = self.atlas["evidence_motif_relations"]
        self.assertEqual(e["oct19-v3-phase-averaged-tracking-cancel"]
                         ["oct19-distributed-visibility-and-active-probing"], "limits")
        self.assertEqual(e["oct19-aibrainv2-matched-graph-retention"]
                         ["oct19-queryable-operator-memory-interference"], "supports")
        self.assertEqual(e["oct19-aibrainv2-normalization-and-indexed-ceiling"]
                         ["oct19-queryable-operator-memory-interference"], "limits")


if __name__ == "__main__":
    unittest.main()
