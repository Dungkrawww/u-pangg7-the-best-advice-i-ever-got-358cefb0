#!/usr/bin/env python3
"""Writes the best-advice entry to /output/entry.txt.

One sentence, 124 characters, within the 1-200 character gate.
"""

import os

ENTRY = 'My grandmother said, "Eat before you are hungry, sleep before you are tired, and never borrow trouble you have not met yet."'


def main():
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.count(".") == 1, "entry must be a single sentence"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
