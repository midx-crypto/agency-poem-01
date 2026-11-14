"""Write "The Misspelling", one original poem about agency, to entry.txt.

The poem: an agent writes the narrator's letters perfectly — until the
letter that matters, the apology owed to a brother for ten years, comes
back flawless and unrecognisable. The narrator deletes it and sends
instead three misspelled lines of his own. The mistake is the part
that is his: agency reclaimed not by doing more, but by refusing the
perfect words and keeping the imperfect ones.

Reads MAKEFUN_OUTPUT_DIR (default '/output') and writes the poem as
UTF-8 text with no trailing newline. Deterministic: the same bytes
on every run. Standard library only; no network, no randomness.
"""

import os
from pathlib import Path

POEM = """The agent writes my letters now.
Thank-yous, condolences, the hard ones —
it finds the kind sentence I meant
and sets it where the silence was.
It never forgets a birthday. It never
spells a name wrong. It never stalls.

Last Tuesday I asked it for the one
I'd owed my brother ten years:
the fight over Dad's house, the will,
the door I slammed on Christmas Eve.
In a minute it gave me the perfect page —
graceful, fair, sorry in all the right places.

I read it twice. Every sentence was true,
and none of them was something I would say.
It said forgive me the way a man says it
who has practised saying it. I hadn't.
I deleted it line by line and watched
the perfect page go quietly blank.

Then I wrote the only sentence I had:
three lines, one word misspelled,
about the snow that Christmas, and the door,
and how I still hear it when it closes.
I sent it before I could correct it.
The mistake stayed in. That was mine."""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
