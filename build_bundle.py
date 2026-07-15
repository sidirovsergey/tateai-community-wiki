"""Build wiki/_bundle.json: every wiki page as one retrieval unit.

Run this after any wiki/entities or wiki/concepts edit, before committing,
so /ask always reads current content. See SCHEMA.md.
"""
import json, os, re, glob

HERE = os.path.dirname(os.path.abspath(__file__))
WIKI_DIR = os.path.join(HERE, "wiki")
OUT_PATH = os.path.join(WIKI_DIR, "_bundle.json")

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def parse_frontmatter(text):
    m = FM_RE.match(text)
    if not m:
        return {}, text
    fm_text = m.group(1)
    fm = {}
    for line in fm_text.splitlines():
        if ":" not in line:
            continue
        k, _, v = line.partition(":")
        fm[k.strip()] = v.strip()
    body = text[m.end():]
    return fm, body


def main():
    pages = []
    patterns = [
        ("wiki/entities/*.md", "entities"),
        ("wiki/concepts/*.md", "concepts"),
    ]
    for pattern, folder in patterns:
        for fp in sorted(glob.glob(os.path.join(HERE, pattern))):
            text = open(fp, encoding="utf-8").read()
            fm, body = parse_frontmatter(text)
            slug = os.path.splitext(os.path.basename(fp))[0]
            pages.append({
                "id": f"{folder}/{slug}",
                "type": fm.get("type", folder.rstrip("s")),
                "title": fm.get("name", slug),
                "tags": fm.get("tags", ""),
                "text": body.strip(),
            })

    for fname, page_id, title in [
        ("wiki/overview.md", "overview", "Overview"),
        ("wiki/timeline.md", "timeline", "Timeline"),
    ]:
        fp = os.path.join(HERE, fname)
        text = open(fp, encoding="utf-8").read()
        fm, body = parse_frontmatter(text)
        pages.append({
            "id": page_id,
            "type": "overview",
            "title": title,
            "tags": fm.get("tags", ""),
            "text": body.strip(),
        })

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(pages, f, ensure_ascii=False)

    total_chars = sum(len(p["text"]) for p in pages)
    print(f"{len(pages)} pages, {total_chars} chars, "
          f"{os.path.getsize(OUT_PATH)} bytes -> {OUT_PATH}")


if __name__ == "__main__":
    main()
