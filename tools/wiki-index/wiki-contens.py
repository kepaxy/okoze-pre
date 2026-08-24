#!/usr/bin/env python3

from pathlib import Path


WIKI_DIR = Path("../okoze-pre.wiki")


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


def make_section(title, pages):
    lines = [
        f"## {title}",
        "",
    ]

    for path in pages:
        page_name = path.stem
        page_title = get_title(path)
        lines.append(f"* [{page_title}]({page_name})")

    lines.append("")

    return lines


def make_contents(wiki_dir):
    episodes, columns = collect_pages(wiki_dir)

    lines = [
        "# Contents",
        "",
    ]

    lines.extend(make_section("Episodes", episodes))
    lines.extend(make_section("Columns", columns))

    return "\n".join(lines)


def main():
    if not WIKI_DIR.is_dir():
        raise SystemExit(f"Directory not found: {WIKI_DIR}")

    contents = make_contents(WIKI_DIR)
    contents_path = WIKI_DIR / "Contents.md"

    contents_path.write_text(contents + "\n", encoding="utf-8")

    print(f"Generated {contents_path}")


if __name__ == "__main__":
    main()