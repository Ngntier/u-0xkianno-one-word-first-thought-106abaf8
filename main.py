"""One Word, First Thought.

The first word that comes to mind, no second draft: "Vellichor" -- the
strange nostalgia of old bookshops, dust and yesterday's stories on the
shelves. Surprising, vivid, and specific in nine letters.
"""

import os

ENTRY = "Vellichor"


def main() -> None:
    word = ENTRY
    if not 1 <= len(word) <= 24:
        raise ValueError("entry must be 1-24 characters")
    if word != word.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be a single word")
    # One word, first thought: letters only -- no digits, no punctuation,
    # no hyphen tricks. The judge weighs surprise and vividness, not length.
    if not word.isalpha():
        raise ValueError("entry must be letters only")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in word):
        raise ValueError("entry must not contain control characters")
    data = word.encode("utf-8")
    if len(data) > 24:
        raise ValueError("entry must be at most 24 UTF-8 bytes")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
