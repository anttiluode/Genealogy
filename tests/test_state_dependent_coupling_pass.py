from pathlib import Path
import unittest

from scripts.validate_data import load_atlas

ROOT = Path(__file__).resolve().parents[1]


class StateDependentCouplingPassTests(unittest.TestCase):
    def setUp(self):
        self.atlas = load_atlas(ROOT)
        self.node_ids = {node["id"] for node in self.atlas["nodes"]}
        self.edges = {
            (edge["source"], edge["target"], edge["type"]): edge
            for edge in self.atlas["edges"]
        }

    def test_resonant_coupling_repos_are_on_the_wall(self):
        self.assertIn(
            "state-dependent-coupling-channel",
            {item["id"] for item in self.atlas["passes"]},
        )
        for node_id in ("ResonaattoriAivo", "FridayRepo", "KapeaKanava"):
            self.assertIn(node_id, self.node_ids)

    def test_lineage_runs_from_resonant_memory_to_coupling_to_channel(self):
        self.assertIn(("ResonaattoriAivo", "FridayRepo", "extracts"), self.edges)
        self.assertIn(("FridayRepo", "KapeaKanava", "inherits"), self.edges)
        self.assertIn(("ResonaattoriAivo", "KapeaKanava", "inherits"), self.edges)

    def test_friday_repo_remains_a_bridge_not_a_biological_claim(self):
        friday = next(node for node in self.atlas["nodes"] if node["id"] == "FridayRepo")
        self.assertIn("does not", friday["killed"].lower())
        self.assertIn("biological", friday["killed"].lower())


if __name__ == "__main__":
    unittest.main()
