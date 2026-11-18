#!/usr/bin/env python3
"""
The Global Chronicle - 17 Nov 2026 News Summary Image.

This script reads final.png from the program's own directory and writes its
bytes unchanged to $MAKEFUN_OUTPUT_DIR/entry.png (defaulting to /output).
"""

import os
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    src = here / "final.png"

    output_dir_env = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_dir = Path(output_dir_env)
    out_dir.mkdir(parents=True, exist_ok=True)

    dest = out_dir / "entry.png"

    if not src.exists():
        raise FileNotFoundError(f"Source image not found: {src}")

    data = src.read_bytes()
    dest.write_bytes(data)


if __name__ == "__main__":
    main()
