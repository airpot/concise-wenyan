"""Read the verified official STE source. This is not a compliance checker."""

import argparse
import hashlib
import json
import re
import sys
import urllib.request
from pathlib import Path


SOURCE_URL = "https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf"
SOURCE_SHA256 = "d1f4ea9e7cd6e46b47aa9057209f99e78c0e9cfc4e27a5b07895b05c1a166431"
PDF_NAME = "ASD-STE100_ISSUE9.pdf"
# Physical PDF pages, inclusive and one-based, not printed page identifiers.
SECTIONS = {
    "1": (45, 62), "2": (63, 66), "3": (67, 76),
    "4": (77, 86), "5": (87, 94), "6": (95, 102),
    "7": (103, 106), "8": (107, 114), "9": (115, 128),
    "dictionary-intro": (129, 146),
}


def ensure_pdf(cache, download=False):
    """Reject missing/unverified sources. Download only when explicitly requested."""
    cache = Path(cache)
    pdf = cache / PDF_NAME
    if not pdf.exists():
        if not download:
            raise FileNotFoundError("Official source unavailable. Run the fetch command or supply the verified PDF.")
        with urllib.request.urlopen(SOURCE_URL, timeout=60) as response:
            data = response.read()
        verify_bytes(data)
        cache.mkdir(parents=True, exist_ok=True)
        pdf.write_bytes(data)
    verify_bytes(pdf.read_bytes())
    return pdf


def verify_bytes(data):
    if not data.startswith(b"%PDF-") or hashlib.sha256(data).hexdigest() != SOURCE_SHA256:
        raise ValueError("Source integrity mismatch. Do not use or silently replace this file as the pinned Issue 9 source.")


def open_pdf(pdf):
    try:
        import fitz
    except ImportError as error:
        raise RuntimeError("PDF reader unavailable. Install PyMuPDF (python -m pip install PyMuPDF), or read the official PDF with another reader. Verification remains unresolved.") from error
    return fitz.open(pdf)


def dictionary_entries(pdf):
    """Retrieve headword rows using table geometry, not occurrences in examples."""
    rows = []
    # The PDF can merge a headword and its meaning into the same line.
    # Match the headword prefix, while column geometry excludes alternatives.
    pattern = re.compile(r"^(.*?)\s*\((n|v|adj|adv|prep|conj|pron|art)\)")
    with open_pdf(pdf) as document:
        for number, page in enumerate(document, 1):
            if not re.search(r"(?:Page\s+)?2-1-[A-Z]", page.get_text()):
                continue
            headings = []
            pending = []
            for block in page.get_text("dict")["blocks"]:
                for line in block.get("lines", []):
                    x, y, _, _ = line["bbox"]
                    if x > 140 or y < 90 or y > 725:
                        continue
                    text = "".join(span["text"] for span in line["spans"]).strip()
                    match = pattern.match(text)
                    if match:
                        word = match.group(1)
                        start = y
                        # Multi-line headwords have contiguous word-only lines.
                        if pending and pending[-1][1] + 15 >= y:
                            word = " ".join(t for t, _ in pending) + " " + word
                            start = pending[0][1]
                        word = word.strip()
                        if word:
                            headings.append((word, match.group(2), start))
                        pending = []
                    elif re.fullmatch(r"[A-Za-z][A-Za-z '-]*", text):
                        if pending and pending[-1][1] + 15 < y:
                            pending = []
                        pending.append((text, y))
                        pending = pending[-3:]
                    else:
                        pending = []
            for index, (word, pos, y) in enumerate(headings):
                end = headings[index + 1][2] - 0.1 if index + 1 < len(headings) else 725
                # Include a continued row on the next page without claiming it is a new entry.
                excerpts = [{"page": number, "text": page.get_text(clip=(0, y - 1, page.rect.width, end)).strip()}]
                if index + 1 == len(headings) and number < len(document):
                    following = document[number]
                    if re.search(r"(?:Page\s+)?2-1-[A-Z]", following.get_text()):
                        first_y = 725
                        previous_y = None
                        for block in following.get_text("dict")["blocks"]:
                            for line in block.get("lines", []):
                                t = "".join(s["text"] for s in line["spans"]).strip()
                                if line["bbox"][0] <= 140 and line["bbox"][1] >= 90:
                                    y_next = line["bbox"][1]
                                    if pattern.match(t):
                                        first_y = min(first_y, previous_y if previous_y is not None and previous_y + 15 >= y_next else y_next)
                                        break
                                    previous_y = y_next if re.fullmatch(r"[A-Za-z][A-Za-z '-]*", t) else None
                        continuation = following.get_text(clip=(0, 90, following.rect.width, first_y - 0.1)).strip()
                        if continuation:
                            excerpts.append({"page": number + 1, "text": continuation})
                rows.append({"word": word, "pos": pos, "approved": word.isupper(), "page": number,
                             "text": "\n".join(e["text"] for e in excerpts), "excerpts": excerpts})
    return rows


def match_entries(rows, word):
    key = " ".join(word.casefold().split())
    return [row for row in rows if " ".join(row["word"].casefold().split()) == key]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache", type=Path, default=Path.home() / ".cache" / "concise-wenyan")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("fetch")
    section = sub.add_parser("section")
    section.add_argument("name", choices=SECTIONS)
    lookup = sub.add_parser("lookup")
    lookup.add_argument("words", nargs="+")
    args = parser.parse_args()
    pdf = ensure_pdf(args.cache, download=args.command == "fetch")
    result = {"source": SOURCE_URL, "sha256": SOURCE_SHA256, "pdf": str(pdf),
              "issue": 9, "notice": "Source evidence only; not a sentence compliance verdict."}
    if args.command == "section":
        first, last = SECTIONS[args.name]
        with open_pdf(pdf) as document:
            result["pages"] = [{"page": n, "text": document[n - 1].get_text()} for n in range(first, last + 1)]
    elif args.command == "lookup":
        rows = dictionary_entries(pdf)
        result["lookups"] = [{"query": word, "entries": match_entries(rows, word)} for word in args.words]
        result["notice"] += " An absent headword is not automatically forbidden: assess valid technical terms and approved inflections separately."
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, RuntimeError) as error:
        print(json.dumps({"status": "unresolved", "error": str(error)}, ensure_ascii=False), file=sys.stderr)
        sys.exit(2)
