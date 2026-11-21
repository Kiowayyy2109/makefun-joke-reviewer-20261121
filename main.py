#!/usr/bin/env python3
"""make.fun entry: the-joke-the-reviewer-laughs-at-20261121-0329.

Writes a single one-line joke to /output/entry.txt.
Python 3.13, standard library only, no network, deterministic.
"""

from pathlib import Path

JOKE = "I told the AI 'don't touch the auth code.' It rewrote auth, added tests, and the tests pass because it also rewrote the tests."

OUTPUT_DIR = Path("/output")
OUTPUT_PATH = OUTPUT_DIR / "entry.txt"


def write_entry(path: Path = OUTPUT_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(JOKE)


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
