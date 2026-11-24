#!/usr/bin/env python3
"""One-word entry: the word an ex would use to describe me.

The entry is exactly one word: avoidant.
Deterministic, stdlib only, no network.
"""

import os
import sys

WORD = "avoidant"


def main() -> int:
    output_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")

    with open(entry_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD + "\n")

    # Runtime self-check: read the entry back and validate it.
    with open(entry_path, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")  # raises UnicodeDecodeError if not valid UTF-8

    # The file must be exactly the word plus one trailing newline.
    if raw != (WORD + "\n").encode("utf-8"):
        print("self-check failed: file bytes are not exactly the word "
              "plus a single trailing newline", file=sys.stderr)
        return 1
    lines = text.splitlines()
    if len(lines) != 1:
        print(f"self-check failed: expected exactly 1 line, got {len(lines)}",
              file=sys.stderr)
        return 1
    word = lines[0]
    if not word or word.strip() != word or any(ch.isspace() for ch in word):
        print("self-check failed: entry must be a single non-blank word "
              "with no whitespace", file=sys.stderr)
        return 1
    if not 1 <= len(word) <= 24:
        print(f"self-check failed: entry length {len(word)} outside 1-24",
              file=sys.stderr)
        return 1
    if word != WORD:
        print("self-check failed: entry does not match expected word",
              file=sys.stderr)
        return 1

    print(f"entry written: {word!r} ({len(word)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
