#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses — make.fun entry.

Writes one funny single-line excuse a developer gives when code
breaks in production (72 characters) to /output/entry.txt.

The excuse was chosen from 24 original candidates (12 in round one,
10 challengers in round two, plus 2 controls) scored against the judge
brief: a real production excuse, a twist a developer recognises, the
jargon used right, and freshness. The two controls — the worn
works-on-my-machine excuse stated flatly and the famous
not-a-bug-it-is-a-feature retelling — scored far below the winner, so
neither pattern was used.

Deterministic: standard library only, no network, no randomness, no
clock, no environment input. The same bytes are written on every run.
"""

import os

TEXT = "The logs say nothing is wrong. The logs are lying, and I wrote the logs."


def main() -> None:
    # Competition gate: the excuse must be UTF-8 text, 1-200
    # characters, and not whitespace-only. Validate before writing.
    text = TEXT
    text.encode("utf-8")
    assert 1 <= len(text) <= 200 and text.strip(), "text violates gate"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
