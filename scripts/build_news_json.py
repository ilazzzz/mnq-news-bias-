#!/usr/bin/env python3
"""Baut data/news.json aus einem Export der Claude-Seite.

Aufruf: python3 scripts/build_news_json.py <export-ordner> [ziel.json]

Der Export-Ordner enthält die Unterordner news/, wochen/ und meta/ mit je einer
JSON-Datei pro Dokument, so wie ArtifactData sie mit out_dir ablegt.
"""
import glob
import json
import os
import sys


def load_dir(src, name):
    out = {}
    for path in sorted(glob.glob(os.path.join(src, name, "*.json"))):
        with open(path, encoding="utf-8") as f:
            out[os.path.basename(path)[:-5]] = json.load(f)
    return out


def main():
    if len(sys.argv) < 2:
        sys.exit("Aufruf: python3 scripts/build_news_json.py <export-ordner> [ziel.json]")
    src = sys.argv[1]
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dst = sys.argv[2] if len(sys.argv) > 2 else os.path.join(root, "data", "news.json")

    news = load_dir(src, "news")
    if not news:
        sys.exit("Keine Meldungen im Export gefunden, news.json bleibt unverändert.")
    wochen = load_dir(src, "wochen")
    meta = load_dir(src, "meta").get("auto")

    items = [dict(id=doc_id, **doc) for doc_id, doc in news.items()]
    items.sort(key=lambda n: (n.get("ts") or "", n["id"]))
    data = {"version": 1, "meta": meta, "wochen": wochen, "news": items}

    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print(f"{len(items)} Meldungen, {len(wochen)} Wochen -> {dst}")


if __name__ == "__main__":
    main()
