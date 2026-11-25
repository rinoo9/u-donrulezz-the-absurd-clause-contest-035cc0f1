"""Entry for The Absurd Clause Contest (make.fun).

Writes one original absurd clause, phrased as deadpan terms-of-service
boilerplate, to /output/entry.txt and prints it to stdout.
Deterministic: the same line every run, no input, no randomness, no network.

The joke: the clause reads like ordinary IP-assignment boilerplate until
it assigns ownership of the reader's shadow -- and leases it out on
weekends, as if a shadow were office equipment.
"""

import os

LINE = (
    "By using this service, you agree that your shadow becomes the "
    "exclusive property of the Company and may be leased to third "
    "parties on weekends without further notice."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
