import sys

from solution import Solution


def _assert(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def run_step_1() -> None:
    solver = Solution()

    heights = [2, 1, 5, 6, 2, 3]
    expected_prev = [-1, -1, 1, 2, 1, 4]
    _assert(
        solver._prev_smaller_indices(heights) == expected_prev,
        "Step 1: prev-smaller indices should match the expected output",
    )

    heights = [2, 2, 2]
    expected_prev = [-1, -1, -1]
    _assert(
        solver._prev_smaller_indices(heights) == expected_prev,
        "Step 1: equal heights should pop (>=) so prev-smaller is -1 for all",
    )


def run_step_2() -> None:
    solver = Solution()

    heights = [2, 1, 5, 6, 2, 3]
    expected_next = [1, 6, 4, 4, 6, 6]
    _assert(
        solver._next_smaller_indices(heights) == expected_next,
        "Step 2: next-smaller indices should match the expected output",
    )

    heights = [2, 4]
    expected_next = [2, 2]
    _assert(
        solver._next_smaller_indices(heights) == expected_next,
        "Step 2: if there is no smaller bar to the right, next index should be n",
    )


def run_step_3() -> None:
    solver = Solution()

    _assert(
        solver.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10,
        "Step 3: example 1 should return 10",
    )
    _assert(
        solver.largestRectangleArea([2, 4]) == 4,
        "Step 3: example 2 should return 4",
    )
    _assert(
        solver.largestRectangleArea([2, 1, 2]) == 3,
        "Step 3: [2,1,2] should return 3",
    )
    _assert(
        solver.largestRectangleArea([0]) == 0,
        "Step 3: single zero bar should return 0",
    )
    _assert(
        solver.largestRectangleArea([2, 2, 2]) == 6,
        "Step 3: equal heights should allow spanning the full width",
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

