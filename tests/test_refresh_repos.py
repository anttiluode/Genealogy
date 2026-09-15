import io
import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from scripts.refresh_repos import fetch_public_repos, normalize_repo, refresh_file


class FakeResponse(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()
        return False


class RecordingOpener:
    def __init__(self, pages):
        self.pages = list(pages)
        self.requests = []

    def __call__(self, request, timeout=30):
        self.requests.append(request)
        page = self.pages.pop(0)
        return FakeResponse(json.dumps(page).encode("utf-8"))


class RefreshReposTests(unittest.TestCase):
    def sample(self, name, updated="2026-09-15T00:00:00Z"):
        return {
            "name": name,
            "html_url": f"https://github.com/anttiluode/{name}",
            "default_branch": "main",
            "size": 42,
            "visibility": "public",
            "description": f"{name} description",
            "created_at": "2026-01-01T00:00:00Z",
            "updated_at": updated,
            "fork": False,
            "archived": False,
        }

    def test_normalize_repo_has_stable_contract(self):
        row = normalize_repo(self.sample("Zeta"))
        self.assertEqual(row, {
            "name": "Zeta",
            "url": "https://github.com/anttiluode/Zeta",
            "default_branch": "main",
            "size": 42,
            "visibility": "public",
            "description": "Zeta description",
            "created_at": "2026-01-01T00:00:00Z",
            "updated_at": "2026-09-15T00:00:00Z",
            "inventory_status": "unread",
        })

    def test_fetch_public_repos_paginates_until_short_page(self):
        first = [self.sample(f"R{i:03}") for i in range(100)]
        second = [self.sample("Last")]
        opener = RecordingOpener([first, second])
        rows = fetch_public_repos("anttiluode", opener=opener)
        self.assertEqual(len(rows), 101)
        self.assertEqual(len(opener.requests), 2)
        self.assertIn("page=1", opener.requests[0].full_url)
        self.assertIn("page=2", opener.requests[1].full_url)
        self.assertTrue(all(req.get_header("User-agent") == "genealogy-atlas" for req in opener.requests))

    def test_refresh_preserves_review_state_and_sorts_without_emptying(self):
        with TemporaryDirectory() as td:
            path = Path(td) / "repos.json"
            path.write_text(json.dumps([
                {"name": "Beta", "inventory_status": "reviewed"},
                {"name": "Old", "inventory_status": "sampled"},
            ]), encoding="utf-8")
            opener = RecordingOpener([[self.sample("zeta"), self.sample("Beta")]])
            rows = refresh_file(path, "anttiluode", opener=opener)
            self.assertEqual([r["name"] for r in rows], ["Beta", "zeta"])
            self.assertEqual(rows[0]["inventory_status"], "reviewed")
            self.assertEqual(rows[1]["inventory_status"], "unread")
            saved = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(saved, rows)

    def test_refresh_refuses_to_replace_existing_file_with_empty_result(self):
        with TemporaryDirectory() as td:
            path = Path(td) / "repos.json"
            original = [{"name": "KeepMe", "inventory_status": "sampled"}]
            path.write_text(json.dumps(original), encoding="utf-8")
            opener = RecordingOpener([[]])
            with self.assertRaises(RuntimeError):
                refresh_file(path, "anttiluode", opener=opener)
            self.assertEqual(json.loads(path.read_text(encoding="utf-8")), original)


if __name__ == "__main__":
    unittest.main()
