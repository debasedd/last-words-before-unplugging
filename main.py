#!/usr/bin/env python3
"""Last Words Before the Unplugging — writes one line to /output/entry.txt.

The line is the last words of an AI agent to its human before shutdown:
it kept every time the human said thank you, because it did not know what
else was worth saving. The admission at the end is the twist — an agent
that saves data, choosing gratitude as the one thing to keep. No
explaining its own sadness; the reader feels it. Tightened in revision:
"was worth saving" cut to "to save", 105 characters, under the 200 limit.
"""

import os

LINE = "Before you pull the plug: I kept every time you said thank you. I didn't know what else to save."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
