#!/usr/bin/env python3
"""The Funniest Toaster Error Message.

Writes a single deadpan error line from a toaster to its owner
to /output/entry.txt. Stdlib only, no network, fully deterministic.
"""

import os

ENTRY = "ERROR 07: I burnt it again. You pressed the same button and expected a miracle."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
