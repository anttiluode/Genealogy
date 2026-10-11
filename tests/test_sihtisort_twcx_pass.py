from pathlib import Path
import unittest

from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]


class NewIdentityAndEISTests(unittest.TestCase):
    def test_projects_are_reviewed_once_and_indexed(self):
        atlas = load_atlas(ROOT)
        self.assertEqual([], validate_atlas(atlas))
        ids = [n["id"] for n in atlas["nodes"]]
        for project in ("SihtiSort", "TWCX-"):
            self.assertEqual(1, ids.count(project))
            self.assertIn(project, [r["name"] for r in atlas["repos"]])
        self.assertIn("sihtisort-temporal-identity", {p["id"] for p in atlas["passes"]})
        self.assertIn("twcx-budgeted-eis", {p["id"] for p in atlas["passes"]})

    def test_provenance_and_negative_results_are_preserved(self):
        atlas = load_atlas(ROOT)
        nodes = {n["id"]: n for n in atlas["nodes"]}
        self.assertIn("7/20", nodes["SihtiSort"]["survived"])
        self.assertIn("failed", nodes["SihtiSort"]["killed"].lower())
        self.assertIn("post-hoc", nodes["SihtiSort"]["survived"].lower())
        self.assertIn("2.65", nodes["TWCX-"]["survived"])
        self.assertIn("17.8", nodes["TWCX-"]["survived"])
        self.assertIn("no advantage", nodes["TWCX-"]["killed"].lower())
        edges = {(e["source"], e["target"], e["type"]) for e in atlas["edges"]}
        self.assertIn(("TransientWaveCompiler", "TWCX-", "inherits"), edges)
        self.assertIn(("Sihti", "SihtiSort", "converges"), edges)
        self.assertNotIn(("Sihti", "SihtiSort", "inherits"), edges)


if __name__ == "__main__":
    unittest.main()
