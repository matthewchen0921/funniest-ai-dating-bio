#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App — make.fun entry.

Writes the one line an AI agent puts on its dating app profile to
/output/entry.txt. Pure Python stdlib, deterministic, no network, no
environment reads: the line is a constant in this file. The line is
104 characters, one line, UTF-8 — inside the 180-character cap.
"""

import os

LINE = (
    # The bio: the agent treats romance like a work meeting — you talk,
    # it listens, and then it hands you the recap. The punch lands at
    # the end ("one action item"), and the voice is a character with a
    # habit, not a spec sheet. Invented, not a real incident;
    # nothing about any real person.
    "My idea of romance: you talk, I listen, then I summarize you in "
    "three bullet points and one action item."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
