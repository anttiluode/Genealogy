from pathlib import Path
import unittest

from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]


class MondayInverseLabsTests(unittest.TestCase):
    def test_monday_projects_once_and_reviewed(self):
        atlas = load_atlas(ROOT)
        self.assertEqual([], validate_atlas(atlas))
        ids = [item["id"] for item in atlas["nodes"]]
        for project in ("MondayRepo", "MondaySihti", "BrainLoops", "SihtiSort"):
            self.assertEqual(1, ids.count(project))
            self.assertEqual("reviewed", next(r["inventory_status"] for r in atlas["repos"] if r["name"] == project))
        self.assertIn("monday-inverse-residue-labs", [p["id"] for p in atlas["passes"]])

    def test_outcomes_and_conceptual_links(self):
        atlas = load_atlas(ROOT)
        nodes = {n["id"]: n for n in atlas["nodes"]}
        self.assertIn("8/8", nodes["MondayRepo"]["survived"])
        self.assertIn("fixed", nodes["MondayRepo"]["killed"].lower())
        self.assertIn("G2", nodes["MondaySihti"]["killed"])
        self.assertIn("56/64", nodes["MondaySihti"]["survived"])
        edges = {(e["source"], e["target"], e["type"]) for e in atlas["edges"]}
        for edge in (("Operaattori", "MondayRepo", "extracts"),
                     ("Operaattori", "MondaySihti", "extracts"),
                     ("Sihti", "MondaySihti", "converges")):
            self.assertIn(edge, edges)
        evidence = {x["id"]: x for x in atlas["evidence"]}
        self.assertEqual("mixed", evidence["mondaysihti-residue-bridge-gate"]["result"])
        self.assertIn("nonlinear-residue-versus-matched-history", [q["id"] for q in atlas["questions"]])


if __name__ == "__main__":
    unittest.main()
