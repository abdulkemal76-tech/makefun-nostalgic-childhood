#!/usr/bin/env python3
"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

Writes one sentence (at most 280 characters) recalling a childhood
memory to /output/entry.txt.
"""

import os

SENTENCE = (
    "I was eight the afternoon my sister was born, and my grandmother "
    "kept stirring sweet rice porridge in a pot so big I could have "
    "bathed in it while the whole house smelled of coconut and pandan "
    "until midnight."
)


def main() -> None:
    text = SENTENCE.strip()
    assert 1 <= len(text) <= 280, f"entry is {len(text)} characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
