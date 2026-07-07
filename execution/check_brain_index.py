#!/usr/bin/env python3
"""Quality gate for brain/ notes.

Checks:
1. Every note in brain/{decisions,notes,references,metrics,ideas}/ follows
   the YYYY-MM-DD_slug.md filename convention.
2. Every note is listed (by filename stem) in brain/INDEX.md.
3. Every [[wikilink]] in brain notes resolves to an existing note filename.

Exit 0 = all gates pass. Exit 1 = failures printed below.
"""

import re
import sys
from pathlib import Path

BRAIN = Path(__file__).resolve().parent.parent / "brain"
CATEGORIES = ["decisions", "notes", "references", "metrics", "ideas"]
DATED = re.compile(r"^\d{4}-\d{2}-\d{2}_[a-z0-9][a-z0-9-]*\.md$")
WIKILINK = re.compile(r"\[\[([^\]|#]+)")


def main() -> int:
    failures = []
    index_text = (BRAIN / "INDEX.md").read_text(encoding="utf-8")

    notes = [p for c in CATEGORIES for p in sorted((BRAIN / c).glob("*.md"))]
    stems = {p.stem for p in notes}

    for note in notes:
        if not DATED.match(note.name):
            failures.append(f"BAD FILENAME  {note.relative_to(BRAIN)} — want YYYY-MM-DD_slug.md")
        if note.stem not in index_text:
            failures.append(f"NOT IN INDEX  {note.relative_to(BRAIN)}")

    # Wikilinks may also point at project files (e.g. [[sycamore]])
    project_stems = {p.stem for p in BRAIN.parent.glob("projects/*/*.md")}
    project_stems |= {p.name for p in BRAIN.parent.glob("projects/*")}
    context_stems = {p.stem for p in BRAIN.parent.glob("context/*.md")}
    linkable = stems | project_stems | context_stems

    for note in notes:
        for target in WIKILINK.findall(note.read_text(encoding="utf-8")):
            if target.strip() not in linkable:
                failures.append(f"DEAD LINK     {note.name} -> [[{target.strip()}]]")

    if failures:
        print(f"FAIL — {len(failures)} issue(s):")
        for f in failures:
            print(f"  {f}")
        return 1

    print(f"PASS — {len(notes)} note(s) checked: filenames dated, all indexed, links resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
