#!/usr/bin/env python3

import sys
from pathlib import Path


def get_title(path):
    """Return the first Markdown H1 title."""
    text = path.read_text(encoding="utf-8")

    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()

    return path.stem


def collect_pages(wiki_dir):
    """Collect episode-* and column-* pages."""
    episodes = []
    columns = []

    for path in wiki_dir.glob("*.md"):
        name = path.stem

        if name.startswith("episode-"):
            episodes.append(path)
        elif name.startswith("column-"):
            columns.append(path)

    episodes.sort(key=lambda p: p.stem)
    columns.sort(key=lambda p: p.stem)

    return episodes, columns


def print_section(title, pages):
    print(f"## {title}")
    print()

    for path in pages:
        page_name = path.stem
        page_title = get_title(path)
        print(f"* [{page_title}]({page_name})")

    print()


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} WIKI_DIRECTORY", file=sys.stderr)
        sys.exit(1)

    wiki_dir = Path(sys.argv[1])

    if not wiki_dir.is_dir():
        print(f"Directory not found: {wiki_dir}", file=sys.stderr)
        sys.exit(1)

    episodes, columns = collect_pages(wiki_dir)

    print("# okoze Development Series")
    print()
    print("This wiki is the development log for the okoze project.")
    print()

    print_section("Episodes", episodes)
    print_section("Columns", columns)


if __name__ == "__main__":
    main()