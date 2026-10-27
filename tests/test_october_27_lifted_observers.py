"""2026-10-27 late wave-observer arrivals: curatorial coverage and gates."""
import unittest
from pathlib import Path
from scripts.validate_data import load_atlas,validate_atlas

ROOT=Path(__file__).resolve().parents[1]
PASS="october-27-lifted-wave-observers-and-instanton"
NODES={"Slider3","AnttisInstanton2"}
ALREADY={"ParabolicOrientationSihti","Kavitaatio","WallMemoryLaw",
         "ResonanceAsControlledMethod","BigKahuna"}
EVIDENCE={
    "oct27-slider3-phase-control-detection-not-unique",
    "oct27-slider3-instantaneous-focus-misleads-coherence",
    "oct27-instanton2-heldout-no-incremental-paper-benefit",
    "oct27-instanton2-spatial-two-center-analysis-not-yet-heldout",
}

class WaveObserverPassTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a=load_atlas(ROOT)
        cls.nodes={n["id"]:n for n in cls.a["nodes"]}
        cls.ev={x["id"]:x for x in cls.a["evidence"]}
        cls.edges={(e["source"],e["target"],e["type"]) for e in cls.a["edges"]}

    def test_census_curated_and_prior_five_preserved(self):
        self.assertEqual(validate_atlas(self.a),[])
        census={r["name"]:r for r in self.a["repos"]}
        self.assertGreaterEqual(len(census),549)
        for name in NODES|ALREADY:
            self.assertIn(name,census)
            self.assertEqual(census[name]["inventory_status"],"reviewed")
            self.assertIn(name,self.nodes)
        self.assertEqual({n["id"] for n in self.a["nodes"]
                          if n.get("pass_id")==PASS},NODES)
        for name in ALREADY:
            self.assertNotEqual(self.nodes[name]["pass_id"],PASS)

    def test_convergence_not_false_inheritance(self):
        self.assertIn(("ParabolicOrientationSihti","Slider3","converges"),self.edges)
        self.assertIn(("Slider3","AnttisInstanton2","converges"),self.edges)
        self.assertNotIn(("Slider3","AnttisInstanton2","inherits"),self.edges)
        self.assertIn("three-delay",self.nodes["Slider3"]["killed"])
        self.assertIn("0.040245",self.nodes["AnttisInstanton2"]["killed"])

    def test_proper_source_controls_and_unfinished_prediction(self):
        self.assertTrue(EVIDENCE.issubset(self.ev))
        self.assertTrue(self.ev["oct27-instanton2-heldout-no-incremental-paper-benefit"]["held_out"])
        self.assertEqual(self.ev["oct27-slider3-phase-control-detection-not-unique"]["result"],"mixed")
        self.assertEqual(self.ev["oct27-instanton2-spatial-two-center-analysis-not-yet-heldout"]["result"],"inconclusive")
        self.assertIn("oct27-does-lifted-focus-lead-positive-field-center-beyond-ordinary-activity",
                      {q["id"] for q in self.a["questions"]})
        motif_ids={m["id"] for m in self.a["motifs"]}
        self.assertIn("oct27-lifted-wave-vs-ordinary-controls",motif_ids)
        self.assertIn("oct27-instantaneous-focus-vs-persistent-object",motif_ids)

    def test_live_wall_cards_and_source_review(self):
        html=(ROOT/"index.html").read_text(encoding="utf-8")
        readme=(ROOT/"README.md").read_text(encoding="utf-8")
        self.assertIn('id="oct27-wave-observers"',html)
        for n in NODES:
            self.assertIn(f'data-mad-node="{n}"',html)
        self.assertIn("549",readme)
        self.assertIn("oct27-wave-observers",readme)
        self.assertTrue((ROOT/"docs/reviews/2026-10-27-slider3-instanton2-observers.md").is_file())

if __name__=="__main__":
    unittest.main()
