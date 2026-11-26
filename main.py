"""Roast the Smart Fridge: one line, best laugh wins.

Writes a single roast line (109 chars, one line, no trailing newline
issues) to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt).
"""

import os

LINE = (
    "At 3:04 a.m. my fridge texted: 'You opened me 14 times. "
    "There is still no cake. I have notified the toaster.'"
)


def main() -> None:
    # Gate: the entry must be 1-160 chars, a single line, not blank.
    assert 1 <= len(LINE) <= 160 and "\n" not in LINE and LINE.strip()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
