"""
source_links.py — Expandable source URL resolution for citations.

Derives Reddit and Rate My Professor URLs from the registries in scrape.py
(filename convention: reddit_<slug>.txt, rmp_<slug>.txt). Local PDF extracts
have no public URL and are cited by filename only.

Adding a new Reddit thread or professor = one line in scrape.py's registry;
re-run build_source_manifest() to refresh documents/sources.json.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from scrape import REDDIT_THREADS, RMP_PROFESSORS

DOCS_DIR = Path("documents")
MANIFEST_PATH = DOCS_DIR / "sources.json"

REDDIT_URL_TEMPLATE = "https://www.reddit.com/r/umass/comments/{thread_id}/{slug}/"
RMP_URL_TEMPLATE = "https://www.ratemyprofessors.com/professor/{prof_id}"

REDDIT_HEADER_RE = re.compile(r"^\[Thread:\s*(.+?)\s*\|\s*r/umass\]", re.I)
RMP_HEADER_RE = re.compile(
    r"^\[Rate My Professor:\s*(.+?)\s*\|\s*.+\]", re.I
)

# Human-readable labels for local-only sources (no public URL).
LOCAL_SOURCE_LABELS: dict[str, str] = {
    "s26_course_description.txt": "Spring 2026 Course Descriptions",
    "s26_course_schedule.txt": "Spring 2026 Course Schedule",
    "s26_reg_info.txt": "Spring 2026 Registration Info",
    "f26_course_description.txt": "Fall 2026 Course Descriptions",
    "f26_course_schedule.txt": "Fall 2026 Course Schedule",
    "f26_reg_info.txt": "Fall 2026 Registration Info",
    "computer_science_bs_requirement_f23.txt": "BS Computer Science Degree Requirements (Fall 2023)",
}


def _slug_to_title(slug: str) -> str:
    return slug.replace("_", " ").strip()


def _read_file_title(path: Path, source_type: str) -> str | None:
    if not path.exists():
        return None
    first_line = path.read_text(encoding="utf-8").split("\n", 1)[0].strip()
    if source_type == "reddit":
        match = REDDIT_HEADER_RE.match(first_line)
        return match.group(1).strip() if match else None
    if source_type == "rmp":
        match = RMP_HEADER_RE.match(first_line)
        return match.group(1).strip() if match else None
    return None


def build_source_manifest(manifest_path: Path = MANIFEST_PATH) -> dict[str, dict[str, Any]]:
    """Build filename -> {type, title, url} from scrape registries and local labels."""
    manifest: dict[str, dict[str, Any]] = {}

    for slug, thread_id in REDDIT_THREADS.items():
        filename = f"reddit_{slug}.txt"
        path = DOCS_DIR / filename
        title = _read_file_title(path, "reddit") or _slug_to_title(slug)
        manifest[filename] = {
            "type": "reddit",
            "title": title,
            "url": REDDIT_URL_TEMPLATE.format(thread_id=thread_id, slug=slug),
        }

    for slug, prof_id in RMP_PROFESSORS.items():
        filename = f"rmp_{slug}.txt"
        path = DOCS_DIR / filename
        title = _read_file_title(path, "rmp") or _slug_to_title(slug).title()
        manifest[filename] = {
            "type": "rmp",
            "title": title,
            "url": RMP_URL_TEMPLATE.format(prof_id=prof_id),
        }

    for filename, title in LOCAL_SOURCE_LABELS.items():
        manifest[filename] = {
            "type": "local",
            "title": title,
            "url": None,
        }

    manifest_path.parent.mkdir(exist_ok=True)
    with manifest_path.open("w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    return manifest


def load_manifest(manifest_path: Path = MANIFEST_PATH) -> dict[str, dict[str, Any]]:
    """Load sources.json, building it first if missing."""
    if not manifest_path.exists():
        return build_source_manifest(manifest_path)
    with manifest_path.open(encoding="utf-8") as f:
        return json.load(f)


def lookup_source(
    filename: str, manifest: dict[str, dict[str, Any]]
) -> dict[str, Any]:
    """Resolve one source filename to its manifest entry."""
    entry = manifest.get(filename.strip())
    if entry:
        return entry
    return {
        "type": "unknown",
        "title": filename,
        "url": None,
    }


def url_for(source_file: str, manifest: dict[str, dict[str, Any]]) -> str | None:
    """Return a public URL for a source_file, or None for local-only sources."""
    filenames = [part.strip() for part in source_file.split(",") if part.strip()]
    urls: list[str] = []
    for filename in filenames:
        entry = lookup_source(filename, manifest)
        url = entry.get("url")
        if url and url not in urls:
            urls.append(url)
    return urls[0] if len(urls) == 1 else None


def format_source_header(
    metadata: dict[str, Any],
    manifest: dict[str, dict[str, Any]],
) -> str:
    """Build a human-readable citation header for one retrieved chunk."""
    source_file = str(metadata.get("source_file", "unknown"))
    source_type = str(metadata.get("source_type", "unknown"))
    filenames = [part.strip() for part in source_file.split(",") if part.strip()]

    if source_type == "reddit":
        primary = filenames[0] if filenames else source_file
        entry = lookup_source(primary, manifest)
        title = metadata.get("thread_title") or entry["title"]
        url = entry.get("url")
        if url:
            return f'Reddit — "{title}" ({url})'
        return f'Reddit — "{title}" ({primary})'

    if source_type == "rmp":
        primary = filenames[0] if filenames else source_file
        entry = lookup_source(primary, manifest)
        title = metadata.get("professor") or entry["title"]
        url = entry.get("url")
        if url:
            return f"Rate My Professor — {title} ({url})"
        return f"Rate My Professor — {title} ({primary})"

    labels: list[str] = []
    for filename in filenames:
        entry = lookup_source(filename, manifest)
        labels.append(entry.get("title") or filename)
    label = ", ".join(labels) if labels else source_file
    return f"UMass — {label} ({source_file})"


def main() -> None:
    manifest = build_source_manifest()
    print(f"Wrote {len(manifest)} entries -> {MANIFEST_PATH}")


if __name__ == "__main__":
    main()
