"""The Vacuum's Alibi — writes one funny line to /output/entry.txt.

Pure stdlib (os only). The line is a single sentence of at most 200
characters, validated before it is written: a robot vacuum's deadpan,
log-style excuse for missing a spot, with the punch at the end.
The joke: the dust bunny claims squatter's rights, and the vacuum's
own warranty becomes the excuse — bureaucracy beats cleaning.
"""

import os

MAX_CHARS = 200

LINE = "Log 04:12 - corner skipped: the dust bunny there filed for squatter's rights, and my warranty excludes evictions."


def validate(line):
    """Enforce the gate: single sentence, 1-200 chars, UTF-8 encodable."""
    if not isinstance(line, str):
        raise ValueError("line must be a string")
    line.encode("utf-8")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError("line must be 1-%d characters, got %d" % (MAX_CHARS, len(line)))
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line, no line breaks")
    terminators = sum(line.count(c) for c in ".!?")
    if terminators != 1:
        raise ValueError("line must be a single sentence, got %d terminators" % terminators)
    if line.rstrip()[-1] not in ".!?":
        raise ValueError("line must end with sentence punctuation")
    return True


def main():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
