"""Write "The Corner", one original poem about agency, to entry.txt.

The poem: an agent measures, planes, and saws the oak for a cradle
perfectly — but the narrator, whose hands have shaken for two years,
refuses to let it finish the whole thing. He sands one corner himself,
the corner where his unborn granddaughter's small hand will rest when
she wakes in the night. The corner is not perfect: it is smooth in the
way only a hand can make smooth — uneven, warm, his. Agency reclaimed
not by doing everything, but by keeping one imperfect corner.

Reads MAKEFUN_OUTPUT_DIR (default '/output') and writes the poem as
UTF-8 text with no trailing newline. Deterministic: the same bytes
on every run. Standard library only; no network, no randomness.
"""

import os
from pathlib import Path

# The poem itself is the entry: 24 lines, written once, never generated.
POEM = """The agent measured the oak twice,
ordered it, planed it, drew the joints
in lines so clean my father would have wept.
It held the board while the saw sang through,
counted the screws, corrected my angles
before I made them.

My hands shake now. They have shaken
for two years. The chisel is too much for them.
The agent offered to finish it all —
the cradle for the granddaughter
who is not yet born, who will arrive in March,
who will sleep where my daughter slept.

I said no.
I took the sandpaper, the finest grit,
and I worked one corner.
One corner, where her small hand will rest
when she wakes in the night and reaches out
for something warm that is not a machine.

It took me an hour. The corner is not perfect.
It is smooth in the way only a hand can make smooth —
uneven, warm, mine.
The agent watched, and said nothing,
and for the first time I did not feel replaced.
I felt accompanied."""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
