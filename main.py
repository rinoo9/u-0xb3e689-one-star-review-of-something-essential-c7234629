#!/usr/bin/env python3
"""One-Star Review of Something Essential.

Writes a single deadpan one-star review of water, an everyday essential,
to /output/entry.txt. The review is fixed text: deterministic, no input,
no network, no randomness.

Craft: a deadpan complaint aimed at a thing that cannot be fixed — water
has no taste, no colour, and no smell, yet the glass is always empty
and the bill still arrives every month. The review lists its grievances
in a flat, matter-of-fact voice, then turns in the last words: the worst
offence is not the water itself but the monthly bill for something that
is supposedly free and flavourless, and the one-star verdict lands
because nothing about it can be returned, repaired, or reviewed into
behaving differently.

Gate: the entry must be 1-160 characters (currently 123), a single line,
and non-blank; main() asserts all three before writing.
"""

import os

ENTRY = (
    "Water has no taste, no colour, and no smell, yet my glass is always "
    "empty and the bill still arrives every month. One star."
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
