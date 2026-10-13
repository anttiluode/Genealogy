from pathlib import Path
import unittest

from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]
NEW = ("SihtiResponseGraph", "ResearchQuestion", "InverseMandala", "Kerrostuma")
PASS = "october-13-predictive-image-inverse-material"


class OctoberThirteenFourProjectsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.atlas = load_atlas(ROOT)

    def test_complete_atlas_and_no_duplicates(self):
        self.assertEqual([], validate_atlas(self.atlas))
        nodes = [n["id"] for n in self.atlas["nodes"]]
        census = {r["name"]: r for r in self.atlas["repos"]}
        for project in NEW:
            self.assertEqual(1, nodes.count(project))
            self.assertIn(project, census)
            self.assertEqual("reviewed", census[project]["inventory_status"])
        self.assertEqual(1, [p["id"] for p in self.atlas["passes"]].count(PASS))

    def test_each_node_carries_its_limits(self):
        nodes = {n["id"]: n for n in self.atlas["nodes"]}
        for project in NEW:
            self.assertEqual(PASS, nodes[project]["pass_id"])
            self.assertTrue(nodes[project]["evidence"].startswith("https://github.com/"))
        self.assertIn("one seed", nodes["SihtiResponseGraph"]["killed"].lower())
        self.assertIn("post-hoc", nodes["ResearchQuestion"]["killed"].lower())
        self.assertIn("physic", nodes["InverseMandala"]["killed"].lower())
        self.assertIn("rim", nodes["Kerrostuma"]["killed"].lower())

    def test_links_are_mechanism_based_not_invented_code_ancestry(self):
        edges = {(x["source"], x["target"]): x for x in self.atlas["edges"]}
        self.assertEqual("extracts", edges[("2MandalaTools", "InverseMandala")]["type"])
        for pair in (
            ("Varjoluotain", "InverseMandala"),
            ("Sihti", "SihtiResponseGraph"),
            ("Sihti", "ResearchQuestion"),
            ("CrystalMoon", "Kerrostuma"),
            ("GelatinIsland", "Kerrostuma"),
        ):
            self.assertEqual("converges", edges[pair]["type"])

    def test_empirical_ledger_keeps_positive_and_negative_results(self):
        evidence = [x for x in self.atlas["evidence"] if x["node"] in NEW]
        # Only the seven new, explicitly named October 13 receipts
        receipts = [
            "sihti-response-graph-quantized-pilot",
            "researchquestion-exact-future-quotient",
            "researchquestion-learned-hankel-comparison",
            "inverse-mandala-exact-collision",
            "inverse-mandala-coded-observation-v2",
            "kerrostuma-quench-fossils-and-network",
            "kerrostuma-wait-vs-melt-predictive-closure",
        ]
        ids = {x["id"] for x in evidence}
        self.assertTrue(set(receipts).issubset(ids))
        results = {x["id"]: x["result"] for x in evidence}
        self.assertEqual("supports", results["inverse-mandala-exact-collision"])
        self.assertEqual("mixed", results["inverse-mandala-coded-observation-v2"])
        self.assertEqual("mixed", results["researchquestion-learned-hankel-comparison"])
        self.assertEqual("mixed", results["kerrostuma-wait-vs-melt-predictive-closure"])
        self.assertEqual("mixed", results["sihti-response-graph-quantized-pilot"])

    def test_motifs_do_not_conflate_all_four_repos(self):
        motifs = {m["id"]: m for m in self.atlas["motifs"]}
        self.assertEqual({"2MandalaTools", "InverseMandala", "Varjoluotain"},
                         set(motifs["mandala-max-intervention-observability"]["nodes"]))
        self.assertEqual({"ResearchQuestion", "Kerrostuma"},
                         set(motifs["predictive-closure-versus-history-fossil"]["nodes"]))
        self.assertEqual({"Sihti", "SighImageFactorization", "SihtiResponseGraph"},
                         set(motifs["image-graph-experience-writes-operator"]["nodes"]))


if __name__ == "__main__":
    unittest.main()
