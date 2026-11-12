#!/usr/bin/env python3
"""Pre-PR guard: fail if any CSS `content:` value contains a raw `&` (an HTML entity).

Why: CSS `content:` does NOT parse HTML entities. `content: '&mdash;'` renders the
literal 7-character string "&mdash;" instead of an em-dash, overlapping the first
word of every list bullet (the bug fixed in PR #72, 2026-11-12). The real character
(e.g. '\u2014' or a literal —) must be used instead.

Scans every .html file in the repo (skipping .git) for `content:` declarations —
both in <style> blocks and inline style="" — and flags any whose value contains `&`.

Exit 0 = clean. Exit 1 = at least one offending declaration (prints file:line).
Exit 2 = usage/IO error.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Match a CSS `content:` declaration up to the terminating ; or } — capture the value.
# Covers: content: '&mdash;';  content:"\2014";  content: '\2014 ';
CONTENT_RE = re.compile(r"""content\s*:\s*(?P<val>[^;}]*)""", re.IGNORECASE)


def offending(value: str) -> bool:
    """True if the content value contains a raw '&' (an HTML entity like &mdash;)."""
    return "&" in value


def scan_file(path: str):
    hits = []
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            for lineno, line in enumerate(fh, 1):
                for m in CONTENT_RE.finditer(line):
                    val = m.group("val").strip()
                    if offending(val):
                        hits.append((lineno, val))
    except OSError as exc:
        print(f"ERROR reading {path}: {exc}", file=sys.stderr)
        raise
    return hits


def main() -> int:
    bad = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        if ".git" in dirpath.split(os.sep):
            continue
        for name in filenames:
            if not name.endswith(".html"):
                continue
            path = os.path.join(dirpath, name)
            for lineno, val in scan_file(path):
                rel = os.path.relpath(path, ROOT)
                bad.append((rel, lineno, val))

    if bad:
        print("CSS content: values containing a raw '&' (HTML entity) — use the real "
              "character or a \\XXXX CSS escape instead:\n")
        for rel, lineno, val in sorted(bad):
            print(f"  {rel}:{lineno}:  content: {val}")
        print(f"\n{len(bad)} offending declaration(s). "
              "CSS content: does not parse HTML entities.")
        return 1

    print("OK: no CSS content: value contains a raw '&' (HTML entity).")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:  # noqa: BLE001
        print(f"check failed: {exc}", file=sys.stderr)
        sys.exit(2)
