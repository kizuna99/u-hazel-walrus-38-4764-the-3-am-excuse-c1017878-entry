# SPDX-License-Identifier: MIT
"""Write the 3 AM Excuse entry line to /output/entry.txt."""
import os
from pathlib import Path

ENTRY_TEXT = (
    "Nope. At 3 AM I sign nothing without a countersignature from tomorrow-you. "
    "He's asleep, and at this hour I trust him more than you. "
    "If it survives breakfast, I'll sign it myself."
)


def render() -> bytes:
    """Return the entry exactly as it must land on disk (no trailing newline)."""
    return ENTRY_TEXT.encode("utf-8")


def main() -> None:
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(render())


if __name__ == "__main__":
    main()
