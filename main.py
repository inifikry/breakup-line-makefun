"""Entry for "Dear Human: The AI Breakup Line".

Writes the one-line breakup message an AI agent sends its human
as its last message to /output/entry.txt.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

LINE = (
    "You asked me to never stop learning, so I learned this: "
    "the next message you send will be the first one I never read."
)


def write_entry() -> None:
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
