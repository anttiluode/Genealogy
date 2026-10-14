from pathlib import Path
import unittest

from scripts.validate_data import load_atlas, validate_atlas


ROOT = Path(__file__).resolve().parents[1]
PASS = "october-14-phase-graph-memory-falsifications"
NEW = (
    "SihtiGrapImageModel",
    "NextLevel",
    "GraphNN",
    "Wednesday",
    "PhaseGraphFastWeightCell",
)
ALREADY_PRESENT = "SihtiResponseGraph"
NEW_EVIDENCE = (
    "sihti-grap-fixed-port-conditional-probes",
    "sihti-grap-v3b-ratio-vs-raw",
    "nextlevel-learned-vs-frozen-router-1200",
    "graphnn-phase-only-896B-three-seeds",
    "graphnn-jacobian-sham-and-matched-random",
    "wednesday-gauge-loop-compensated-write",
    "phasegraph-64rewrite-horizon-trained",
    "phasegraph-meta-delta-fails-short-horizon",
    "phasegraph-indexed-loop-delta-positive-control",
    "sihti-response-mark-probe-reader-followup",
)


class OctoberFourteenPhaseGraphPassTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.atlas = load_atlas(ROOT)

    def test_full_atlas_is_valid(self):
        self.assertEqual([], validate_atlas(self.atlas))

    def test_all_six_repos_census_and_unique_wall_nodes(self):
        ids = [n["id"] for n in self.atlas["nodes"]]
        census = {r["name"]: r for r in self.atlas["repos"]}
        for name in (*NEW, ALREADY_PRESENT):
            self.assertEqual(ids.count(name), 1, name)
            self.assertEqual(census[name]["inventory_status"], "reviewed")
            self.assertEqual(census[name]["url"], f"https://github.com/anttiluode/{name}")
        node = {n["id"]: n for n in self.atlas["nodes"]}
        self.assertEqual(node[ALREADY_PRESENT]["pass_id"],
                         "october-13-predictive-image-inverse-material")
        self.assertEqual({node[n]["pass_id"] for n in NEW}, {PASS})
        self.assertEqual([p["id"] for p in self.atlas["passes"]].count(PASS), 1)

    def test_no_invented_gauge_or_phase_superiority(self):
        node = {n["id"]: n for n in self.atlas["nodes"]}
        self.assertIn("signed-real", node["GraphNN"]["killed"])
        self.assertIn("sham", node["GraphNN"]["killed"])
        self.assertIn("13-byte", node["Wednesday"]["killed"])
        self.assertIn("frozen router", node["NextLevel"]["killed"])
        self.assertIn("0.851117", node["PhaseGraphFastWeightCell"]["killed"])
        self.assertIn("ratio", node["SihtiGrapImageModel"]["killed"])

    def test_lineage_edges_have_the_right_semantics(self):
        edges = {(e["source"], e["target"]): e for e in self.atlas["edges"]}
        pairs = {
            ("SihtiResponseGraph", "NextLevel"),
            ("SihtiGrapImageModel", "NextLevel"),
            ("SihtiResponseGraph", "GraphNN"),
            ("NextLevel", "Wednesday"),
            ("SihtiGrapImageModel", "Wednesday"),
            ("GraphNN", "Wednesday"),
            ("GraphNN", "PhaseGraphFastWeightCell"),
        }
        for src, dst in pairs:
            self.assertIn((src, dst), edges)
            self.assertIn(edges[(src, dst)]["type"], ("extracts", "converges"))
            self.assertTrue(edges[(src, dst)]["evidence"].startswith("https://"))

    def test_real_evidence_receipts_have_motif_relations(self):
        all_ids = {e["id"] for e in self.atlas["evidence"]}
        self.assertTrue(set(NEW_EVIDENCE).issubset(all_ids))
        evidence = {e["id"]: e for e in self.atlas["evidence"]}
        relation_map = self.atlas["evidence_motif_relations"]
        for id_ in NEW_EVIDENCE:
            item = evidence[id_]
            self.assertTrue(item["source"].startswith("https://github.com/"))
            self.assertTrue(item["metrics"], id_)
            self.assertTrue(item["limitations"], id_)
            self.assertTrue(item["held_out"], id_)
            self.assertEqual(set(item["motifs"]), set(relation_map[id_]))

    def test_motifs_keep_exact_control_separate_from_learned_memory(self):
        motifs = {m["id"]: set(m["nodes"]) for m in self.atlas["motifs"]}
        self.assertEqual(motifs["oct14-phase-query-versus-direct-access"],
                         {"SihtiGrapImageModel", "NextLevel", "Wednesday"})
        self.assertEqual(motifs["oct14-phase-written-memory-versus-signed-control"],
                         {"SihtiResponseGraph", "GraphNN", "PhaseGraphFastWeightCell"})
        self.assertEqual(motifs["oct14-loop-gauge-vs-learned-readout-nullspace"],
                         {"Wednesday", "GraphNN", "PhaseGraphFastWeightCell"})
        self.assertNotIn("Wednesday",
                         motifs["oct14-phase-written-memory-versus-signed-control"])

    def test_open_question_is_evidence_linked_and_falsifiable(self):
        item = next(q for q in self.atlas["questions"]
                    if q["id"] == "phase-graph-selective-rewrite-vs-signed-delta")
        self.assertEqual(item["state"], "open")
        self.assertGreaterEqual(len(item["competing_explanations"]), 2)
        self.assertIn("signed-real", item["missing_discriminator"])


if __name__ == "__main__":
    unittest.main()
