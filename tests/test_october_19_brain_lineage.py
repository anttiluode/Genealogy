"""October 19: a single surviving SihtiBrain card with nine preserved receipts."""

from pathlib import Path
import unittest

from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]
PASS_ID = "october-19-sihtibrain-to-ai-query-memory"
RETIRED = {
    "SihtiBrainV2", "SihtibrainV3", "AIBrain", "AIbrainV2",
    "RealTimeReadWriteClaude",
}
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

    def test_one_surviving_curated_card_and_no_old_inventory_entries(self):
        nodes = [n for n in self.atlas["nodes"] if n.get("pass_id") == PASS_ID]
        self.assertEqual([n["id"] for n in nodes], ["SihtiBrain"])
        self.assertEqual(nodes[0]["era_order"], 136)
        inventory = {r["name"]: r for r in self.atlas["repos"]}
        self.assertIn("SihtiBrain", inventory)
        self.assertEqual(inventory["SihtiBrain"]["inventory_status"], "reviewed")
        self.assertFalse(RETIRED.intersection(inventory))
        self.assertFalse(RETIRED.intersection(n["id"] for n in self.atlas["nodes"]))

    def test_sihtistack_has_separate_historical_negative_receipt(self):
        # The consolidated SihtiBrain card still owns its original nine source receipts.
        # SihtiStack was subsequently unretired on user request to expose its
        # own distinct frozen-model return gate, NOT the larger brain project.
        stack = [n for n in self.atlas["nodes"] if n["id"] == "SihtiStack"]
        self.assertEqual(len(stack), 1)
        self.assertEqual(stack[0]["pass_id"], "october-19-sihtistack-return-channel")
        self.assertIn("2/12", stack[0]["killed"])
        self.assertIn("SihtiStack", {r["name"] for r in self.atlas["repos"]})

    def test_all_nine_results_have_rehomed_source_and_real_controls(self):
        evidence = {e["id"]: e for e in self.atlas["evidence"]}
        for key in RECEIPTS:
            self.assertIn(key, evidence)
            item = evidence[key]
            self.assertEqual(item["node"], "SihtiBrain")
            self.assertTrue(item["source"].startswith(
                "https://github.com/anttiluode/SihtiBrain/blob/main/"
            ))
            self.assertTrue(item["controls"])
            self.assertTrue(item["limitations"])
        self.assertEqual(evidence["oct19-v2-preregistered-calcium-advantage-fail"]["result"], "contradicts")
        self.assertEqual(evidence["oct19-v3-phase-averaged-tracking-cancel"]["result"], "contradicts")
        self.assertEqual(evidence["oct19-aibrainv2-normalization-and-indexed-ceiling"]["result"], "mixed")

    def test_negative_boundaries_stay_visible_on_one_card(self):
        node = next(n for n in self.atlas["nodes"] if n["id"] == "SihtiBrain")
        for term in ("three-factor", "62.13%", "0.781", "95.4%", "53.4%", "73.9%", "2/12"):
            self.assertIn(term, node["killed"])

    def test_questions_still_demand_strong_controls(self):
        questions = {q["id"]: q for q in self.atlas["questions"]}
        for qid in ("oct19-operator-read-beyond-normalization-and-index",
                    "oct19-phase-aware-probes-vs-velocity-tracking"):
            self.assertEqual(questions[qid]["state"], "open")
            self.assertTrue(questions[qid]["competing_explanations"])
            self.assertGreaterEqual(len(questions[qid]["candidate_experiment"]["outcomes"]), 2)

    def test_motifs_and_evidence_relationships_survive(self):
        motifs = {m["id"]: m for m in self.atlas["motifs"]}
        for mid in ("oct19-distributed-visibility-and-active-probing",
                    "oct19-local-credit-vs-simpler-event",
                    "oct19-queryable-operator-memory-interference"):
            self.assertIn(mid, motifs)
            self.assertFalse(RETIRED.intersection(motifs[mid]["nodes"]))
        links = self.atlas["evidence_motif_relations"]
        self.assertEqual(links["oct19-v3-phase-averaged-tracking-cancel"]
                         ["oct19-distributed-visibility-and-active-probing"], "limits")
        self.assertEqual(links["oct19-aibrainv2-matched-graph-retention"]
                         ["oct19-queryable-operator-memory-interference"], "supports")


if __name__ == "__main__":
    unittest.main()
