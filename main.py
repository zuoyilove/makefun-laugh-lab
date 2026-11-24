# One-Liner Laugh Lab — make.fun entry
# (u-suroso-69-one-liner-laugh-lab-6ccf3aae)
#
# One short funny line answering the prompt — the excuse a robot vacuum
# gives after eating a sock — written as plain text to /output/entry.txt.
# The line is a fixed string: the grader runs the program twice and the
# runs must be deterministic, so there is no randomness and no input.
# The gate allows 1 to 200 characters.

LINE = (
    "The sock attacked first. I finished what it started and filed "
    "the leftovers under 'lunch'."
)

MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars, gate is 1-200"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.strip() == LINE, "entry must not be only whitespace / padded"
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
