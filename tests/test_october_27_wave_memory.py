"""October 27, 2026: OpenAI paper context and ResonantNeuron-to-cavity branch."""
import unittest
from pathlib import Path
from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]
PASS = "october-27-wave-paper-and-written-wall-memory"
NODES = {
    "ResonantNeuron", "ParabolicOrientationSihti", "Kavitaatio",
    "WallMemoryLaw", "ResonanceAsControlledMethod", "BigKahuna",
}
EVIDENCE = {
    "oct27-resonantneuron-designed-interference-gates",
    "oct27-parabolic-sihti-orientation-and-ray-controls",
    "oct27-kavitaatio-material-multibit-echo",
    "oct27-wallmemorylaw-preregistered-24bit-stadium",
    "oct27-resonance-controlledmethod-heldout-parabolic-negative",
    "oct27-bigkahuna-adaptive-needle-fails-fixed",
}

class October27WaveMemoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.atlas = load_atlas(ROOT)
        cls.nodes = {n["id"]: n for n in cls.atlas["nodes"]}
        cls.evidence = {e["id"]: e for e in cls.atlas["evidence"]}
        cls.motifs = {m["id"]: m for m in cls.atlas["motifs"]}
        cls.edges = {(e["source"], e["target"], e["type"]): e for e in cls.atlas["edges"]}

    def test_atlas_integrity_and_unique_curated_nodes(self):
        self.assertEqual(validate_atlas(self.atlas), [])
        self.assertEqual({n["id"] for n in self.atlas["nodes"] if n.get("pass_id") == PASS}, NODES)
        self.assertEqual({self.nodes[n]["era_order"] for n in NODES}, {157})
        self.assertIn(PASS, {p["id"] for p in self.atlas["passes"]})

    def test_census_and_berglund_anchor(self):
        inventory = {r["name"]: r for r in self.atlas["repos"]}
        self.assertTrue(NODES.issubset(inventory))
        for name in NODES:
            self.assertEqual(inventory[name]["inventory_status"], "reviewed")
            self.assertEqual(inventory[name]["url"], self.nodes[name]["url"])
        self.assertIn("Berglund", self.nodes["ResonantNeuron"]["claim"])
        self.assertIn("June", self.nodes["ResonantNeuron"]["claim"])
        self.assertIn("not learned", self.nodes["ResonantNeuron"]["killed"])

    def test_frozen_lineage_edges_not_hyped_as_code_forks(self):
        for source, target, kind in [
            ("ResonantNeuron", "Kavitaatio", "converges"),
            ("Sihti", "ParabolicOrientationSihti", "inherits"),
            ("Kavitaatio", "WallMemoryLaw", "inherits"),
            ("Kavitaatio", "ResonanceAsControlledMethod", "inherits"),
            ("WallMemoryLaw", "ResonanceAsControlledMethod", "converges"),
            ("Kahuna", "BigKahuna", "inherits"),
            ("ResonanceAsControlledMethod", "BigKahuna", "converges"),
        ]:
            self.assertIn((source, target, kind), self.edges)
        self.assertNotIn(("ResonantNeuron", "Kavitaatio", "inherits"), self.edges)
        self.assertNotIn(("ResonanceAsControlledMethod", "BigKahuna", "inherits"), self.edges)

    def test_successes_and_failures_both_visible(self):
        self.assertIn("848", self.nodes["WallMemoryLaw"]["survived"])
        self.assertIn("300/300", self.nodes["WallMemoryLaw"]["survived"])
        self.assertIn("0/12", self.nodes["Kavitaatio"]["killed"])
        self.assertIn("51.1%", self.nodes["ResonanceAsControlledMethod"]["killed"])
        self.assertIn("70.8%", self.nodes["ResonanceAsControlledMethod"]["killed"])
        self.assertIn("0/20", self.nodes["BigKahuna"]["killed"])
        self.assertIn("ray window", self.nodes["ParabolicOrientationSihti"]["killed"])

    def test_empirical_receipts_motifs_questions(self):
        self.assertTrue(EVIDENCE.issubset(self.evidence))
        self.assertEqual(self.evidence["oct27-resonance-controlledmethod-heldout-parabolic-negative"]["result"], "contradicts")
        self.assertEqual(self.evidence["oct27-wallmemorylaw-preregistered-24bit-stadium"]["sample"]["count"], 300)
        for motif in (
            "oct27-written-wall-not-wave",
            "oct27-openai-parabolic-directional-law",
            "oct27-question-value-vs-focus",
        ):
            self.assertIn(motif, self.motifs)
        q = {q["id"]: q for q in self.atlas["questions"]}
        self.assertIn("oct27-can-written-wall-learn-then-be-read-economically", q)
        self.assertEqual(q["oct27-can-written-wall-learn-then-be-read-economically"]["state"], "open")

    def test_live_page_and_review(self):
        html = (ROOT/"index.html").read_text(encoding="utf-8")
        readme = (ROOT/"README.md").read_text(encoding="utf-8")
        for node in NODES:
            self.assertIn(f'data-mad-node="{node}"', html)
        self.assertIn('id="oct27-wave-memory"', html)
        self.assertIn("docs/reviews/2026-10-27-wave-paper-written-wall-memory.md", html)
        self.assertIn("oct27-wave-memory", readme)
        self.assertTrue((ROOT/"docs/reviews/2026-10-27-wave-paper-written-wall-memory.md").is_file())

if __name__ == "__main__":
    unittest.main()
