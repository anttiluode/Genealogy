"""Seven October 29 additions, one honest reactivation baseline."""
import unittest
from pathlib import Path
from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]
PASS = "october-29-circulating-memory-and-state-transfer"
NAMES = ("RoundAndRound", "LoopAImemory", "MoebiusLoopMemory", "ThursdaySol",
         "ChainNeuronsWithPhaseSpikeSol", "ChainNeuronsWithPhaseSpike", "Complexity")


class October29Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.atlas = load_atlas(ROOT)
        cls.nodes = {x["id"]: x for x in cls.atlas["nodes"]}

    def test_unique_seven_and_valid(self):
        self.assertEqual(validate_atlas(self.atlas), [])
        self.assertGreaterEqual(len(self.atlas["repos"]), 561)
        for name in NAMES:
            self.assertEqual(sum(x["name"] == name for x in self.atlas["repos"]), 1)
            self.assertEqual(sum(x["id"] == name for x in self.atlas["nodes"]), 1)
            self.assertEqual(self.nodes[name]["pass_id"], PASS)

    def test_bounds_and_visible_wall(self):
        self.assertIn("Direct cue-to-state ridge ties", self.nodes["RoundAndRound"]["killed"])
        self.assertIn("0/8", self.nodes["ThursdaySol"]["killed"])
        self.assertIn("Möbius", self.nodes["MoebiusLoopMemory"]["killed"])
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn('id="oct29-roundandround"', html)
        for name in NAMES:
            self.assertIn(f'data-mad-node="{name}"', html)

    def test_lineage_not_oversold(self):
        edges = {(e["source"], e["target"], e["type"]) for e in self.atlas["edges"]}
        self.assertIn(("MoebiusLoopMemory", "LoopAImemory", "inherits"), edges)
        self.assertNotIn(("MoebiusLoopMemory", "RoundAndRound", "inherits"), edges)
        self.assertNotIn(("ChainNeuronsWithPhaseSpike", "ChainNeuronsWithPhaseSpikeSol", "inherits"), edges)


if __name__ == "__main__":
    unittest.main()
