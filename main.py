"""Write one curiosity-arousing text to /output/entry.txt.

Python 3.13, standard library only. Deterministic: the same text every run.
"""

from pathlib import Path

TEXT = (
    "On the table she left three things: a key with no lock, a map with no "
    "destination, and a note that read only, 'You already know where this "
    "goes.' She was never seen again — but every night since, at exactly "
    "3:11, the map has shown one more street."
)


def main() -> None:
    text = TEXT.strip()
    if not 1 <= len(text) <= 280:
        raise ValueError(f"entry must be 1-280 characters, got {len(text)}")
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
