#!/usr/bin/env python3
"""One-Star Review of Something Essential.

Writes a single deadpan one-star review of gravity, an everyday essential,
to /output/entry.txt. The review is fixed text: deterministic, no input,
no network, no randomness.

Craft: a deadpan complaint aimed at a force that never clocks out —
gravity works around the clock and never takes a day off, yet the one
thing it is reliably good at is dropping everything the moment it is no
longer held. The review lists its grievances in a flat, matter-of-fact
voice, then turns in the last words: the sting is that the most diligent
worker in the universe is only ever noticed when something breaks, and
the one-star verdict lands because nothing about it can be returned,
repaired, or reviewed into behaving differently.

Gate: the entry must be 1-160 characters (currently 127), a single line,
and non-blank; main() asserts all three before writing.
"""

import os

ENTRY = (
    "Gravity works around the clock, never takes a day off, and still "
    "drops everything I own the second I stop holding it. One star."
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
