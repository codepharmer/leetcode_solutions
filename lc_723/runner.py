import sys
import random

from solution import Solution


def _assert(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def _copy_board(board: list[list[int]]) -> list[list[int]]:
    return [row[:] for row in board]


def _format_board(board: list[list[int]]) -> str:
    return "\n".join(str(row) for row in board)


def _is_gravity_applied(board: list[list[int]]) -> bool:
    """Return True if every column has all zeros above all non-zeros."""
    R, C = len(board), len(board[0])
    for c in range(C):
        seen_zero = False
        for r in range(R - 1, -1, -1):  # bottom -> top
            if board[r][c] == 0:
                seen_zero = True
                continue
            if seen_zero:
                return False
    return True


def _is_stable(board: list[list[int]]) -> bool:
    """Return True if there is no horizontal or vertical run of length >= 3."""
    R, C = len(board), len(board[0])
    for r in range(R):
        for c in range(C):
            v = board[r][c]
            if v == 0:
                continue

            # Horizontal contiguous count around (r, c)
            cnt = 1
            cc = c - 1
            while cc >= 0 and board[r][cc] == v:
                cnt += 1
                cc -= 1
            cc = c + 1
            while cc < C and board[r][cc] == v:
                cnt += 1
                cc += 1
            if cnt >= 3:
                return False

            # Vertical contiguous count around (r, c)
            cnt = 1
            rr = r - 1
            while rr >= 0 and board[rr][c] == v:
                cnt += 1
                rr -= 1
            rr = r + 1
            while rr < R and board[rr][c] == v:
                cnt += 1
                rr += 1
            if cnt >= 3:
                return False

    return True


def _ref_candy_crush(board: list[list[int]]) -> tuple[list[list[int]], bool]:
    """
    Slow, independent reference implementation:
    repeatedly crush any cell that belongs to a run (>=3) and apply gravity.
    """
    R, C = len(board), len(board[0])
    ever_crushed = False

    while True:
        crush: set[tuple[int, int]] = set()

        # Identify all cells that belong to a horizontal/vertical run (>= 3).
        for r in range(R):
            for c in range(C):
                v = board[r][c]
                if v == 0:
                    continue

                cnt = 1
                cc = c - 1
                while cc >= 0 and board[r][cc] == v:
                    cnt += 1
                    cc -= 1
                cc = c + 1
                while cc < C and board[r][cc] == v:
                    cnt += 1
                    cc += 1
                if cnt >= 3:
                    crush.add((r, c))
                    continue

                cnt = 1
                rr = r - 1
                while rr >= 0 and board[rr][c] == v:
                    cnt += 1
                    rr -= 1
                rr = r + 1
                while rr < R and board[rr][c] == v:
                    cnt += 1
                    rr += 1
                if cnt >= 3:
                    crush.add((r, c))

        if not crush:
            return board, ever_crushed

        ever_crushed = True
        for r, c in crush:
            board[r][c] = 0

        # Gravity
        for c in range(C):
            wr = R - 1
            for r in range(R - 1, -1, -1):
                if board[r][c] != 0:
                    board[wr][c] = board[r][c]
                    wr -= 1
            for r in range(wr, -1, -1):
                board[r][c] = 0


def _ref_candy_crush_runs(board: list[list[int]]) -> tuple[list[list[int]], bool]:
    """
    Faster reference implementation that finds runs by scanning rows/cols.
    This is still independent from the submitted solution (no negative marking).
    """
    R, C = len(board), len(board[0])
    ever_crushed = False

    while True:
        crush: set[tuple[int, int]] = set()

        # Horizontal runs
        for r in range(R):
            c = 0
            while c < C:
                v = board[r][c]
                if v == 0:
                    c += 1
                    continue

                c2 = c + 1
                while c2 < C and board[r][c2] == v:
                    c2 += 1

                if c2 - c >= 3:
                    for k in range(c, c2):
                        crush.add((r, k))

                c = c2

        # Vertical runs
        for c in range(C):
            r = 0
            while r < R:
                v = board[r][c]
                if v == 0:
                    r += 1
                    continue

                r2 = r + 1
                while r2 < R and board[r2][c] == v:
                    r2 += 1

                if r2 - r >= 3:
                    for k in range(r, r2):
                        crush.add((k, c))

                r = r2

        if not crush:
            return board, ever_crushed

        ever_crushed = True
        for r, c in crush:
            board[r][c] = 0

        # Gravity
        for c in range(C):
            wr = R - 1
            for r in range(R - 1, -1, -1):
                if board[r][c] != 0:
                    board[wr][c] = board[r][c]
                    wr -= 1
            for r in range(wr, -1, -1):
                board[r][c] = 0


def run_step_1() -> None:
    solver = Solution()

    board = [
        [1, 1, 1, 2],
        [1, 3, 4, 2],
        [1, 5, 6, 2],
    ]
    expected = {
        (0, 0),
        (0, 1),
        (0, 2),
        (1, 0),
        (2, 0),
        (0, 3),
        (1, 3),
        (2, 3),
    }
    _assert(
        solver._find_crushes(_copy_board(board)) == expected,
        "Step 1: should find all cells that belong to a run of >= 3 (horizontal or vertical)",
    )

    board = [
        [7, 1, 7],
        [7, 1, 7],
        [2, 2, 2],
        [7, 1, 7],
    ]
    expected = {(2, 0), (2, 1), (2, 2)}
    _assert(
        solver._find_crushes(_copy_board(board)) == expected,
        "Step 1: should find only the obvious horizontal triple (no false positives)",
    )


def run_step_2() -> None:
    solver = Solution()

    board = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 4, 5],
    ]
    expected = [
        [0, 0, 0],
        [2, 1, 0],
        [3, 4, 5],
    ]
    solver._apply_gravity(board)
    _assert(
        board == expected,
        "Step 2: gravity should drop non-zero values to the bottom of each column",
    )


def run_step_3() -> None:
    solver = Solution()

    board = [
        [7, 1, 7],
        [7, 1, 7],
        [2, 2, 2],
        [7, 1, 7],
    ]
    expected = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    _assert(
        solver.candyCrush(_copy_board(board)) == expected,
        "Step 3: chain reaction example should stabilize to all zeros",
    )

    board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    _assert(
        solver.candyCrush(_copy_board(board)) == board,
        "Step 3: board with no crushes should remain unchanged",
    )

    board = [
        [1, 1, 1],
        [0, 2, 3],
        [4, 5, 6],
    ]
    expected = [
        [0, 0, 0],
        [0, 2, 3],
        [4, 5, 6],
    ]
    _assert(
        solver.candyCrush(_copy_board(board)) == expected,
        "Step 3: simple horizontal triple should crush and then apply gravity",
    )


def run_step_4() -> None:
    solver = Solution()

    def _assert_case(board: list[list[int]], label: str, check_cell_ref: bool = False) -> None:
        got = solver.candyCrush(_copy_board(board))

        want_runs, crushed_runs = _ref_candy_crush_runs(_copy_board(board))
        if check_cell_ref:
            want_cell, crushed_cell = _ref_candy_crush(_copy_board(board))
            _assert(
                want_cell == want_runs and crushed_cell == crushed_runs,
                f"{label}: reference implementations disagree\n"
                f"input:\n{_format_board(board)}\n\n"
                f"cell_ref:\n{_format_board(want_cell)}\n\n"
                f"runs_ref:\n{_format_board(want_runs)}",
            )

        _assert(
            got == want_runs,
            f"{label}: solution output mismatch\n"
            f"input:\n{_format_board(board)}\n\n"
            f"got:\n{_format_board(got)}\n\n"
            f"want:\n{_format_board(want_runs)}",
        )

        _assert(_is_stable(got), f"{label}: output should be stable (no crushes remain)")
        if crushed_runs:
            _assert(_is_gravity_applied(got), f"{label}: output should satisfy gravity (zeros above non-zeros)")
        _assert(
            all(v >= 0 for row in got for v in row),
            f"{label}: output should not contain negative markers",
        )
        _assert(
            solver.candyCrush(_copy_board(got)) == got,
            f"{label}: output should be idempotent (already stable)",
        )

    def _assert_expected(board: list[list[int]], expected: list[list[int]], label: str) -> None:
        got = solver.candyCrush(_copy_board(board))
        _assert(
            got == expected,
            f"{label}: unexpected output\n"
            f"input:\n{_format_board(board)}\n\n"
            f"got:\n{_format_board(got)}\n\n"
            f"expected:\n{_format_board(expected)}",
        )
        _assert_case(board, label, check_cell_ref=True)

    # Fixed regression tests (some with explicit expected output).
    _assert_expected(
        board=[
            [0, 0, 0],
            [1, 0, 0],
            [0, 0, 0],
        ],
        expected=[
            [0, 0, 0],
            [1, 0, 0],
            [0, 0, 0],
        ],
        label="Step 4: stable board with floating candies should remain unchanged",
    )

    _assert_expected(
        board=[
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ],
        expected=[
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ],
        label="Step 4: all-zeros board should remain unchanged",
    )

    _assert_expected(
        board=[
            [1, 2, 3],
            [1, 2, 4],
            [1, 5, 6],
        ],
        expected=[
            [0, 2, 3],
            [0, 2, 4],
            [0, 5, 6],
        ],
        label="Step 4: simple vertical triple should crush",
    )

    _assert_expected(
        board=[
            [1, 1, 1, 2, 2, 2],
            [3, 4, 5, 6, 7, 8],
            [9, 9, 9, 1, 1, 1],
        ],
        expected=[
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [3, 4, 5, 6, 7, 8],
        ],
        label="Step 4: multiple disjoint crushes in one iteration",
    )

    _assert_expected(
        board=[
            [2000, 2000, 2000],
            [1, 2, 3],
            [4, 5, 6],
        ],
        expected=[
            [0, 0, 0],
            [1, 2, 3],
            [4, 5, 6],
        ],
        label="Step 4: large values should crush normally",
    )

    _assert_case(
        board=[
            [110, 5, 112, 113, 114],
            [210, 211, 5, 213, 214],
            [310, 311, 3, 313, 314],
            [410, 411, 412, 5, 414],
            [5, 1, 512, 3, 3],
            [610, 4, 1, 613, 614],
            [710, 1, 2, 713, 714],
            [810, 1, 2, 1, 1],
            [1, 1, 2, 2, 2],
            [4, 1, 4, 4, 1014],
        ],
        label="Step 4: larger chain-reaction board",
        check_cell_ref=True,
    )

    _assert_case(
        board=[
            [1, 2, 3, 3, 3, 9],
            [1, 2, 4, 8, 7, 9],
            [1, 2, 5, 6, 7, 9],
            [6, 6, 6, 1, 1, 1],
        ],
        label="Step 4: overlapping runs should crush all in the same iteration",
        check_cell_ref=True,
    )

    # Randomized fuzzing (small boards): cross-check both reference implementations.
    rng = random.Random(0)
    cases = 400
    max_r = 8
    max_c = 8
    max_val = 5
    for i in range(cases):
        R = rng.randint(3, max_r)
        C = rng.randint(3, max_c)
        board = [[rng.randint(0, max_val) for _ in range(C)] for _ in range(R)]
        _assert_case(board, f"Step 4 fuzz small (case {i})", check_cell_ref=True)

    # Randomized fuzzing (medium boards): run-based reference only (faster).
    rng = random.Random(1)
    cases = 300
    for i in range(cases):
        R = rng.randint(3, 20)
        C = rng.randint(3, 20)
        board = [[rng.randint(0, 12) for _ in range(C)] for _ in range(R)]
        _assert_case(board, f"Step 4 fuzz medium (case {i})", check_cell_ref=False)

    # A few larger boards (near constraints).
    rng = random.Random(2)
    for i in range(5):
        board = [[rng.randint(0, 8) for _ in range(50)] for _ in range(50)]
        _assert_case(board, f"Step 4 fuzz 50x50 (case {i})", check_cell_ref=False)


def main() -> None:
    if len(sys.argv) > 2:
        raise SystemExit("Usage: python runner.py [step]")

    step = 4
    if len(sys.argv) == 2:
        try:
            step = int(sys.argv[1])
        except ValueError as exc:
            raise SystemExit("Step must be an integer: 1, 2, 3, or 4") from exc

    if step == 1:
        run_step_1()
    elif step == 2:
        run_step_1()
        run_step_2()
    elif step == 3:
        run_step_1()
        run_step_2()
        run_step_3()
    elif step == 4:
        run_step_1()
        run_step_2()
        run_step_3()
        run_step_4()
    else:
        raise SystemExit("Step must be 1, 2, 3, or 4")

    print(f"Step {step} passed.")


if __name__ == "__main__":
    main()
