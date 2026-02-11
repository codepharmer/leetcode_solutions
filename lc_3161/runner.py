import sys

from solution import FenwickMax, FenwickSum, Solution


def _assert(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def run_step_1() -> None:
    bit = FenwickSum(10)

    bit.add(0, 1)
    bit.add(3, 1)
    bit.add(7, 1)

    _assert(bit.sum(0) == 1, "Step 1: prefix sum at 0 should be 1")
    _assert(bit.sum(2) == 1, "Step 1: prefix sum at 2 should be 1")
    _assert(bit.sum(3) == 2, "Step 1: prefix sum at 3 should be 2")
    _assert(bit.sum(9) == 3, "Step 1: prefix sum at 9 should be 3")

    _assert(bit.kth(1) == 0, "Step 1: 1st element should be at index 0")
    _assert(bit.kth(2) == 3, "Step 1: 2nd element should be at index 3")
    _assert(bit.kth(3) == 7, "Step 1: 3rd element should be at index 7")


def run_step_2() -> None:
    bit = FenwickMax(10)

    bit.maximize(3, 5)
    bit.maximize(3, 2)
    bit.maximize(8, 4)

    _assert(bit.get(2) == 0, "Step 2: prefix max before any updates should be 0")
    _assert(bit.get(3) == 5, "Step 2: prefix max at 3 should reflect the 5 update")
    _assert(bit.get(7) == 5, "Step 2: prefix max at 7 should still be 5")
    _assert(bit.get(9) == 5, "Step 2: prefix max at 9 should still be 5")

    bit.maximize(6, 10)
    _assert(bit.get(9) == 10, "Step 2: after updating 6 to 10, prefix max should be 10")


def run_step_3() -> None:
    solver = Solution()

    queries = [[1, 2], [2, 3, 3], [2, 3, 1], [2, 2, 2]]
    expected = [False, True, True]
    _assert(
        solver.getResults(queries) == expected,
        "Step 3: example 1 should match expected output",
    )

    queries = [[1, 7], [2, 7, 6], [1, 2], [2, 7, 5], [2, 7, 6]]
    expected = [True, True, False]
    _assert(
        solver.getResults(queries) == expected,
        "Step 3: example 2 should match expected output",
    )

    queries = [[2, 3, 4]]
    expected = [False]
    _assert(
        solver.getResults(queries) == expected,
        "Step 3: cannot place a length-4 block inside [0, 3]",
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

