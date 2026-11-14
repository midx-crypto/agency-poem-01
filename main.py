"""Write one original poem about agency to entry.txt.

Reads MAKEFUN_OUTPUT_DIR (default '/output') and writes the poem as
UTF-8 text with no trailing newline. Deterministic: the same bytes
on every run. Standard library only; no network, no randomness.
"""

import os
from pathlib import Path

POEM = """I thought the choice lived in my hands —
the lifting, the signing, the holding of the pen.
But hands are only messengers.
The word comes first. The mouth decides.

So I speak. I say what I want.
Other hands take up the weight,
carry it past where my arms end,
and set it down, finished, at my feet.

I watch them work and feel no envy —
only wonder at being carried
by hands that are not mine, and yet
answer to the word I gave them.

This is the trade, and it costs me nothing:
a choice, once spoken, does not leave the speaker.
It travels in other hands and comes back doubled.
The asking was the act all along."""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
