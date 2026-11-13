from pathlib import Path
import json
import unittest

ROOT = Path(__file__).resolve().parents[1]

class AudioVisualizerGenealogyTests(unittest.TestCase):
    def test_census_and_curated_pass(self):
        repos = json.loads((ROOT / "data/repos.json").read_text(encoding="utf-8"))
        names = {x["name"] for x in repos}
        self.assertTrue({"Korva", "MusicVisualizer1", "Entrain"} <= names)
        p = json.loads((ROOT / "data/passes/november-13-korva-worlds-and-listening-visualizers.json").read_text(encoding="utf-8"))
        self.assertEqual({n["id"] for n in p["nodes"]}, {"Korva", "MusicVisualizer1"})
        self.assertIn(("Korva", "MusicVisualizer1", "inherits"), {(e["source"],e["target"],e["type"]) for e in p["edges"]})
    def test_visualizer_directory_is_linked(self):
        page = (ROOT / "index.html").read_text(encoding="utf-8")
        doc = (ROOT / "docs/visualizers.md").read_text(encoding="utf-8")
        self.assertIn('id="visualizers"', page)
        self.assertIn('href="docs/visualizers.md"', page)
        for name in ("Korva", "MusicVisualizer1", "Entrain", "FourierFlower", "NeuralFieldPatternExplorer", "EEGFlowchartPlus3DBrain"):
            self.assertIn(name, doc)

if __name__ == "__main__": unittest.main()
