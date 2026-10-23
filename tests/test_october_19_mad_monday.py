"""Mad Monday remains navigable without splitting consolidated research."""
from pathlib import Path
import unittest
from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]
PASS = "october-19-mad-monday-image-gradient"
EXPECTED = {"SihtiImageModel3", "Sihtiimagemodel4"}
EVIDENCE = {
    "oct19-mad-monday-model3-r3-coarse-oracle",
    "oct19-mad-monday-model3-r4-signed-flux",
    "oct19-mad-monday-model4-tensor-orientation",
    "oct19-mad-monday-model4-ping-sham",
    "oct19-mad-monday-inverse-v3-temporal-readout",
}

class MadMondayTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.atlas = load_atlas(ROOT)

    def test_data_valid_and_new_nodes_distinct(self):
        self.assertEqual(validate_atlas(self.atlas), [])
        nodes = [n for n in self.atlas["nodes"] if n.get("pass_id") == PASS]
        self.assertEqual({n["id"] for n in nodes}, EXPECTED)
        self.assertEqual(sum(n["id"] == "SihtiBrain" for n in self.atlas["nodes"]), 1)
        self.assertEqual(sum(n["id"] == "BrainAsInverseModelerV3" for n in self.atlas["nodes"]), 1)
        # SihtiStack has a distinct retroactive return-channel pass, not a
        # duplicate Mad Monday node or a replacement for SihtiBrain.
        stack = [n for n in self.atlas["nodes"] if n["id"] == "SihtiStack"]
        self.assertEqual(len(stack), 1)
        self.assertEqual(stack[0]["pass_id"], "october-19-sihtistack-return-channel")

    def test_result_failures_and_privileged_oracles_preserved(self):
        nodes = {n["id"]: n for n in self.atlas["nodes"]}
        self.assertIn("worsens", nodes["SihtiImageModel3"]["killed"])
        self.assertIn("privileged oracle", nodes["Sihtiimagemodel4"]["killed"])
        records = {e["id"]: e for e in self.atlas["evidence"]}
        for eid in EVIDENCE:
            self.assertIn(eid, records)
            self.assertTrue(records[eid]["controls"])
            self.assertTrue(records[eid]["limitations"])
        self.assertEqual(records["oct19-mad-monday-model4-ping-sham"]["result"], "contradicts")
        self.assertEqual(records["oct19-mad-monday-inverse-v3-temporal-readout"]["node"], "BrainAsInverseModelerV3")
        self.assertIn("Open PR #3", records["oct19-mad-monday-inverse-v3-temporal-readout"]["design"])

    def test_wall_feature_links_to_existing_cards(self):
        page = (ROOT / "index.html").read_text(encoding="utf-8")
        script = (ROOT / "assets" / "app.js").read_text(encoding="utf-8")
        for node in EXPECTED | {"SihtiBrain", "BrainAsInverseModelerV3"}:
            self.assertIn(f'data-mad-node="{node}"', page)
        self.assertIn("document.querySelectorAll('[data-mad-node]')", script)
        self.assertIn('id="mad-monday"', page)

if __name__ == "__main__":
    unittest.main()
