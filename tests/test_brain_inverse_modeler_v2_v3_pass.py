import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def read(path):
    return json.loads((DATA / path).read_text(encoding="utf-8"))


class BrainInverseModelerV2V3PassTests(unittest.TestCase):
    def test_v2_v3_pass_is_enabled_and_contains_lineage(self):
        index = read("passes/index.json")
        self.assertTrue(
            any(
                row["path"] == "brain-inverse-modeler-v2-v3.json" and row["enabled"]
                for row in index
            )
        )

        payload = read("passes/brain-inverse-modeler-v2-v3.json")
        nodes = {node["id"] for node in payload["nodes"]}
        self.assertEqual({"BrainAsInverseModelerV2", "BrainAsInverseModelerV3"}, nodes)

        edges = {(edge["source"], edge["target"], edge["type"]) for edge in payload["edges"]}
        self.assertIn(("BrainAsInverseModeler", "BrainAsInverseModelerV2", "inherits"), edges)
        self.assertIn(("BrainAsInverseModelerV2", "BrainAsInverseModelerV3", "inherits"), edges)

    def test_v2_v3_claim_boundaries_are_preserved(self):
        payload = read("passes/brain-inverse-modeler-v2-v3.json")
        nodes = {node["id"]: node for node in payload["nodes"]}

        v2 = nodes["BrainAsInverseModelerV2"]
        self.assertIn("raw", v2["killed"].lower())
        self.assertIn("delay", v2["killed"].lower())

        v3 = nodes["BrainAsInverseModelerV3"]
        self.assertIn("gate a", v3["survived"].lower())
        self.assertIn("gate c0", v3["survived"].lower())
        self.assertIn("raw", v3["killed"].lower())
        self.assertIn("biological", v3["killed"].lower())

    def test_recent_update_mentions_v2_and_v3(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn("BrainAsInverseModelerV2", html)
        self.assertIn("BrainAsInverseModelerV3", html)


if __name__ == "__main__":
    unittest.main()
