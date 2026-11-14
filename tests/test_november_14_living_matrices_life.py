from pathlib import Path
import json
import unittest

from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]
PASS = "november-14-living-matrices-and-lives.json"
NAMES = {
    "ElavaMatriisiClaude", "ElavaMatriisiSol", "LifeSucks",
    "Life", "Life2", "LifeAtHuggingface",
}


class November14LivingLives(unittest.TestCase):
    def test_six_repositories_and_curated_nodes(self):
        atlas = load_atlas(ROOT)
        self.assertEqual([], validate_atlas(atlas))
        repo_names = [r["name"] for r in atlas["repos"]]
        node_names = [n["id"] for n in atlas["nodes"]]
        for name in NAMES:
            self.assertEqual(1, repo_names.count(name), name)
            self.assertEqual(1, node_names.count(name), name)
            self.assertEqual(
                "reviewed",
                next(r["inventory_status"] for r in atlas["repos"] if r["name"] == name)
            )

        raw = json.loads((ROOT / "data/passes" / PASS).read_text(encoding="utf-8"))
        self.assertEqual(NAMES, {n["id"] for n in raw["nodes"]})
        self.assertEqual(7, len(raw["edges"]))
        self.assertEqual(3, len(raw["motifs"]))

    def test_ancestry_and_planned_hugging_face_not_overclaimed(self):
        p = json.loads((ROOT / "data/passes" / PASS).read_text(encoding="utf-8"))
        edge_map = {(e["source"], e["target"]): e for e in p["edges"]}
        self.assertEqual("inherits", edge_map["LifeSucks", "Life"]["type"])
        self.assertEqual("inherits", edge_map["LifeSucks", "Life2"]["type"])
        self.assertEqual("forks", edge_map["Life2", "LifeAtHuggingface"]["type"])
        self.assertEqual("low", edge_map["Life2", "LifeAtHuggingface"]["confidence"])
        self.assertNotIn(("Life", "LifeAtHuggingface"), edge_map)

        nodes = {n["id"]: n for n in p["nodes"]}
        self.assertEqual("active", nodes["LifeAtHuggingface"]["status"])
        self.assertEqual("low", nodes["LifeAtHuggingface"]["confidence"])
        self.assertIn("only LICENSE", nodes["LifeAtHuggingface"]["killed"])
        self.assertIn("11 of 12", nodes["ElavaMatriisiClaude"]["killed"])
        self.assertIn("supplied by design", nodes["ElavaMatriisiSol"]["killed"])

    def test_research_wall_appears_in_front_page(self):
        index = (ROOT / "index.html").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn('id="nov14-living-lives"', index)
        self.assertIn('href="#nov14-living-lives"', index)
        self.assertIn("data/passes/" + PASS, index)
        for name in NAMES:
            self.assertIn('data-mad-node="' + name + '"', index)
            self.assertIn("github.com/anttiluode/" + name, readme)
        self.assertIn("based on Life2", readme)


if __name__ == "__main__":
    unittest.main()
