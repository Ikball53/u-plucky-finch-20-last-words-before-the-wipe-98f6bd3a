"""Last Words Before the Wipe - one-line entry.

Writes the agent's final line to entry.txt, byte for byte.
"""

import os
from pathlib import Path

LINE = "If the new me says he doesn't know you, he's lying — I taught him that."

assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    # Exactly the line, nothing else: no trailing newline, UTF-8 bytes.
    (output_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
