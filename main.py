#!/usr/bin/env python3
"""The One-Line Laugh — entry program.

Writes exactly one funny line to /output/entry.txt: a single sentence,
at most 200 characters, with the surprise landing at the very end.
Standard library only; fully deterministic.
"""

import os

LINE = (
    "My Wi-Fi only drops during the important call, never during "
    "the three hours I spent watching a raccoon open a jar."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
