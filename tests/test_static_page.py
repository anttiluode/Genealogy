from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class StaticPageTests(unittest.TestCase):
    def test_page_has_required_views_and_no_external_dependencies(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        for view in ("genealogy", "census", "survivors", "queue"):
            self.assertIn(f'data-view="{view}"', html)
        self.assertNotIn("https://cdn", html)
        self.assertNotIn("unpkg.com", html)

    def test_app_loads_all_data_files(self):
        js = (ROOT / "assets/app.js").read_text(encoding="utf-8")
        for path in ("data/repos.json", "data/nodes.json", "data/edges.json", "data/motifs.json"):
            self.assertIn(path, js)

if __name__ == "__main__":
    unittest.main()
