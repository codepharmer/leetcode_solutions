from typing import List, Set, Tuple


class Solution:
    def _find_crushes(self, board: List[List[int]]) -> Set[Tuple[int, int]]:
        R, C = len(board), len(board[0])
        crushes: set[tuple[int, int]] = set()

        # Horizontal runs
        for r in range(R):
            c = 0
            while c < C:
                v = abs(board[r][c])
                if v == 0:
                    c += 1
                    continue

                c2 = c
                while c2 < C and abs(board[r][c2]) == v:
                    c2 += 1

                if c2 - c >= 3:
                    for k in range(c, c2):
                        crushes.add((r, k))

                c = c2

        # Vertical runs
        for c in range(C):
            r = 0
            while r < R:
                v = abs(board[r][c])
                if v == 0:
                    r += 1
                    continue

                r2 = r
                while r2 < R and abs(board[r2][c]) == v:
                    r2 += 1

                if r2 - r >= 3:
                    for k in range(r, r2):
                        crushes.add((k, c))

                r = r2

        return crushes

    def _apply_gravity(self, board: List[List[int]]) -> None:
        R, C = len(board), len(board[0])

        for c in range(C):
            wr = R - 1
            for r in range(R - 1, -1, -1):
                if board[r][c] != 0:
                    board[wr][c] = board[r][c]
                    wr -= 1
            for r in range(wr, -1, -1):
                board[r][c] = 0

    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        R, C = len(board), len(board[0])

        def mark_and_crush() -> bool:
            changed = False

            # 1) mark horizontal runs
            for r in range(R):
                c = 0
                while c < C:
                    v = abs(board[r][c])
                    if v == 0:
                        c += 1
                        continue

                    c2 = c
                    while c2 < C and abs(board[r][c2]) == v:
                        c2 += 1

                    if c2 - c >= 3:
                        changed = True
                        for k in range(c, c2):
                            board[r][k] = -abs(board[r][k])

                    c = c2

            # 2) mark vertical runs
            for c in range(C):
                r = 0
                while r < R:
                    v = abs(board[r][c])
                    if v == 0:
                        r += 1
                        continue

                    r2 = r
                    while r2 < R and abs(board[r2][c]) == v:
                        r2 += 1

                    if r2 - r >= 3:
                        changed = True
                        for k in range(r, r2):
                            board[k][c] = -abs(board[k][c])

                    r = r2

            if not changed:
                return False

            # 3) crush: turn marked cells into 0
            for r in range(R):
                for c in range(C):
                    if board[r][c] < 0:
                        board[r][c] = 0

            return True

        def apply_gravity() -> None:
            for c in range(C):
                wr = R - 1
                for r in range(R - 1, -1, -1):
                    if board[r][c] > 0:
                        board[wr][c] = board[r][c]
                        wr -= 1
                for r in range(wr, -1, -1):
                    board[r][c] = 0

        while mark_and_crush():
            apply_gravity()

        return board
