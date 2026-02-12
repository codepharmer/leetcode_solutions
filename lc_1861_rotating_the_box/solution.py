from typing import List


class Solution:
    """
    LeetCode 1861: Rotating the Box
    Implement step-by-step and validate with runner.py.
    """

    def _apply_gravity(self, box: List[List[str]]) -> None:
        """
        Step 1:
        Mutate box in-place so stones ('#') fall to the right within each row.
        Obstacles ('*') split rows into independent segments. Empty is '.'.

        Hint: scan each row from right to left keeping a 'write' pointer for where
        the next stone should land, resetting after each obstacle.
        """
        raise NotImplementedError

    def _rotate_clockwise(self, box: List[List[str]]) -> List[List[str]]:
        """
        Step 2:
        Return a new matrix representing box rotated 90 degrees clockwise.

        If box is m x n, result is n x m.
        """
        raise NotImplementedError

    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        """
        Step 3:
        Apply gravity, then rotate clockwise, and return the result.
        """
        ROWS, COLS = len(box), len(box[0])

        res = [["."] * ROWS for _ in range(COLS)]

        for r in reversed(range (ROWS)):
            i = COLS -1

            for c in range(COLS):
                if box[r][c] == "#":
                    res[i][ROWS-r-1] = "#"
                    i -= 1
                elif box[r][c] == "*":
                    res[c][ROWS-r-1] = "*"
                    i = c -1
       
        return res



    # def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
    #     """
    #     Step 3:
    #     Apply gravity, then rotate clockwise, and return the result.
    #     """
    #     ROWS, COLS = len(box), len(box[0])

    #     for r in range (ROWS):
    #         i = COLS -1

    #         for c in reversed(range(COLS)):
    #             if box[r][c] == "#":
    #                 box[r][c], box[r][i] = box[r][i], box[r][c]
    #                 i -= 1
    #             elif box[r][c] == "*":
    #                 i = c -1
    #     res = []

    #     for c in range(COLS):
    #         for r in reversed(range(ROWS)):
    #             col.append(box[r][c])
    #         res.append(col)
    #     return res

