import sys

from solution import Solution


def _assert(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def run_step_1() -> None:
    solver = Solution()
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    expected = [
        ["This", "is", "an"],
        ["example", "of", "text"],
        ["justification."],
    ]

    _assert(
        solver._pack_lines(words, 16) == expected,
        "Step 1: greedy line packing should match the expected grouping",
    )


def run_step_2() -> None:
    solver = Solution()

    line_words = ["This", "is", "an"]
    _assert(
        solver._justify_line(line_words, 16, is_last=False) == "This    is    an",
        "Step 2: non-last line should be fully justified",
    )

    line_words = ["example", "of", "text"]
    _assert(
        solver._justify_line(line_words, 16, is_last=False) == "example  of text",
        "Step 2: extra spaces should be distributed to the left",
    )

    line_words = ["acknowledgment"]
    _assert(
        solver._justify_line(line_words, 16, is_last=False) == "acknowledgment  ",
        "Step 2: single-word non-last line should be left-justified",
    )


def run_step_3() -> None:
    solver = Solution()

    words = ["This", "is", "an", "example", "of", "text", "justification."]
    expected = [
        "This    is    an",
        "example  of text",
        "justification.  ",
    ]
    _assert(
        solver.fullJustify(words, 16) == expected,
        "Step 3: example 1 should match expected output",
    )

    words = ["What", "must", "be", "acknowledgment", "shall", "be"]
    expected = [
        "What   must   be",
        "acknowledgment  ",
        "shall be        ",
    ]
    _assert(
        solver.fullJustify(words, 16) == expected,
        "Step 3: example 2 should match expected output",
    )


def main() -> None:
    if len(sys.argv) > 2:
        raise SystemExit("Usage: python runner.py [step]")

    step = 3
    if len(sys.argv) == 2:
        try:
            step = int(sys.argv[1])
        except ValueError as exc:
            raise SystemExit("Step must be an integer: 1, 2, or 3") from exc

    if step == 1:
        run_step_1()
    elif step == 2:
        run_step_1()
        run_step_2()
    elif step == 3:
        run_step_1()
        run_step_2()
        run_step_3()
    else:
        raise SystemExit("Step must be 1, 2, or 3")

    print(f"Step {step} passed.")


if __name__ == "__main__":
    main()
