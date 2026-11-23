#!/usr/bin/env python3
"""One-Star Review of Something Essential.

Writes a single deadpan one-star review of the sun, an everyday essential,
to /output/entry.txt. The review is fixed text: deterministic, no input,
no network, no randomness.
"""

import os

ENTRY = (
    "The sun is too bright to look at, too hot to stand under, "
    "and still shows up every morning like it owns the place. One star."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 160, f"entry is {len(ENTRY)} chars, must be 1-160"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back and confirm exactly what was written, byte for byte.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == ENTRY, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
