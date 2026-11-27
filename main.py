"""Funniest Autocorrect Fail — make.fun entry.

Writes one autocorrect-fail line to entry.txt in the output directory
named by MAKEFUN_OUTPUT_DIR (default /output). No network, no input
files, no dependencies beyond the standard library; the output is the
same on every run.
"""

import os

TEXT = "I need a new mistress. Mine sags in the middle and squeaks every time I roll over at night."

# The sealed gate only accepts 1 to 199 characters; fail loudly here
# rather than shipping an entry the gate would refuse.
assert 1 <= len(TEXT) <= 199, "entry text outside the 1-199 character gate"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
