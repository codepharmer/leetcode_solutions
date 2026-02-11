import sys

from solution import Solution


def _assert(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def _copy_box(box: list[list[str]]) -> list[list[str]]:
    return [row[:] for row in box]


def run_step_1() -> None:
    solver = Solution()

    box = [list("#.*##.")]
    expected = [list(".#*.##")]
    solver._apply_gravity(box)
    _assert(
        box == expected,
        "Step 1: stones should fall to the right within obstacle-separated segments",
    )

    box = [
        list("..#"),
        list("###"),
        list("*#."),
    ]
    expected = [
        list("..#"),
        list("###"),
        list("*.#"),
    ]
    solver._apply_gravity(box)
    _assert(
        box == expected,
        "Step 1: gravity should be applied row-by-row (obstacles are fixed)",
    )


def run_step_2() -> None:
    solver = Solution()

    box = [
        list(".#"),
        list("*."),
    ]
    expected = [
        list("*."),
        list(".#"),
    ]
    _assert(
        solver._rotate_clockwise(_copy_box(box)) == expected,
        "Step 2: rotate should produce a 90-degree clockwise rotation",
    )


def run_step_3() -> None:
    solver = Solution()

    box = [list("#.#")]
    expected = [
        list("."),
        list("#"),
        list("#"),
    ]
    _assert(
        solver.rotateTheBox(_copy_box(box)) == expected,
        "Step 3: single-row example should match expected rotated output",
    )

    box = [
        list("#.*."),
        list("##*."),
    ]
    expected = [
        list("#."),
        list("##"),
        list("**"),
        list(".."),
    ]
    _assert(
        solver.rotateTheBox(_copy_box(box)) == expected,
        "Step 3: example with obstacles should match expected output",
    )

    box = [
        list("..."),
        list(".*."),
        list("..."),
    ]
    _assert(
        solver.rotateTheBox(_copy_box(box)) == [
            list("..."),
            list(".*."),
            list("..."),
        ],
        "Step 3: no stones means rotation only",
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

