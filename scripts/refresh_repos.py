from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

API = "https://api.github.com"
PER_PAGE = 100


def normalize_repo(repo: dict) -> dict:
    return {
        "name": repo.get("name", ""),
        "url": repo.get("html_url", ""),
        "default_branch": repo.get("default_branch") or "",
        "size": int(repo.get("size") or 0),
        "visibility": repo.get("visibility") or ("private" if repo.get("private") else "public"),
        "description": repo.get("description") or "",
        "created_at": repo.get("created_at") or "",
        "updated_at": repo.get("updated_at") or "",
        "inventory_status": "unread",
    }


def _request(url: str) -> Request:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "genealogy-atlas",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return Request(url, headers=headers)


def fetch_public_repos(user: str, opener=urlopen) -> list[dict]:
    rows: list[dict] = []
    page = 1
    while True:
        query = urlencode({"per_page": PER_PAGE, "page": page, "sort": "full_name", "direction": "asc"})
        request = _request(f"{API}/users/{user}/repos?{query}")
        with opener(request, timeout=30) as response:
            payload = json.loads(response.read().decode("utf-8"))
        if not isinstance(payload, list):
            message = payload.get("message", "unexpected GitHub response") if isinstance(payload, dict) else "unexpected GitHub response"
            raise RuntimeError(message)
        rows.extend(normalize_repo(repo) for repo in payload if not repo.get("fork", False))
        if len(payload) < PER_PAGE:
            break
        page += 1
    return rows


def _existing_status(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    try:
        existing = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}
    return {
        row.get("name", ""): row.get("inventory_status", "unread")
        for row in existing
        if row.get("name")
    }


def curated_repo_names(root: Path) -> set[str]:
    names: set[str] = set()
    data = root / "data"

    nodes_path = data / "nodes.json"
    if nodes_path.exists():
        nodes = json.loads(nodes_path.read_text(encoding="utf-8"))
        names.update(node.get("id", "") for node in nodes if node.get("id"))

    pass_root = data / "passes"
    index_path = pass_root / "index.json"
    if index_path.exists():
        index = json.loads(index_path.read_text(encoding="utf-8"))
        for entry in index:
            if not entry.get("enabled", True):
                continue
            pass_path = pass_root / entry["path"]
            payload = json.loads(pass_path.read_text(encoding="utf-8"))
            names.update(node.get("id", "") for node in payload.get("nodes", []) if node.get("id"))

    return names


def refresh_file(path: Path, user: str, opener=urlopen, reviewed_names: set[str] | None = None) -> list[dict]:
    statuses = _existing_status(path)
    reviewed_names = set(reviewed_names or ())
    rows = fetch_public_repos(user, opener=opener)
    if not rows:
        raise RuntimeError("GitHub returned an empty repository census; existing data was left untouched")
    for row in rows:
        if row["name"] in statuses:
            row["inventory_status"] = statuses[row["name"]]
        if row["name"] in reviewed_names:
            row["inventory_status"] = "reviewed"
    rows.sort(key=lambda row: row["name"].casefold())
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(rows, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    tmp.replace(path)
    return rows


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    user = argv[0] if argv else "anttiluode"
    root = Path(__file__).resolve().parents[1]
    path = root / "data" / "repos.json"
    try:
        rows = refresh_file(path, user, reviewed_names=curated_repo_names(root))
    except Exception as exc:
        print(f"repository census refresh failed: {exc}", file=sys.stderr)
        return 1
    print(f"repository census: {len(rows)} public non-fork repos")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
