"""One-line resignation letter of a cron job.

Writes the letter to /output/entry.txt and validates it against the
competition gate: UTF-8 text, 1-140 characters, not only whitespace.
"""

import os

LETTER = (
    "I have fired every minute since March and nobody knows "
    "what I do, including me. I quit."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_LENGTH = 140


def validate(text: str) -> None:
    """Check the letter against the gate rules."""
    if not isinstance(text, str):
        raise ValueError("letter must be a string")
    if len(text) < 1 or len(text) > MAX_LENGTH:
        raise ValueError(
            f"letter must be 1-{MAX_LENGTH} characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("letter must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("letter must be exactly one line")
    if len(text) >= 2 and text[0] == '"' and text[-1] == '"':
        raise ValueError("letter must not be wrapped in quotation marks")


def verify_written(text: str) -> None:
    """Read the file back and assert it holds exactly the letter."""
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text, (
        f"read-back mismatch: file holds {written!r}, expected {text!r}"
    )
    assert "\n" not in written, "written file must contain no newline"


def main() -> None:
    validate(LETTER)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LETTER)
    verify_written(LETTER)
    print(f"Wrote {len(LETTER)} characters to {OUTPUT_PATH}")
    print("Read-back verification passed: file matches LETTER exactly")


if __name__ == "__main__":
    main()
