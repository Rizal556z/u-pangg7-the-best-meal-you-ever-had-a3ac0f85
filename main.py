"""The Best Meal You Ever Had — make.fun Growth entry (program/v1).

Writes a single sentence, at most 200 characters, about the best meal
ever had to /output/entry.txt.
"""

import os

SENTENCE = (
    "My grandmother's rendang, slow-cooked six hours in coconut milk "
    "until the beef fell apart, eaten with warm rice on her kitchen "
    "floor while rain drummed on the tin roof, is the best meal "
    "I ever had."
)

MAX_LEN = 200


def main() -> None:
    text = SENTENCE.strip()
    if not (1 <= len(text) <= MAX_LEN):
        raise SystemExit(f"entry must be 1-{MAX_LEN} chars, got {len(text)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
