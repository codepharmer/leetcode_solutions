from typing import List


class FenwickSum:
    """
    Step 1: Fenwick tree / BIT for prefix sums.

    Indices are 0-based externally: valid i are 0..n-1.

    You will use this to track which obstacle positions are currently present, and to
    find predecessor/successor obstacles with `kth` (order statistic).
    """

    def __init__(self, n: int):
        self._n = n
        self._bit = [0] * (n + 1)  # 1-based internally

    def add(self, i: int, delta: int) -> None:
        """Add `delta` to position i."""
        raise NotImplementedError

    def sum(self, i: int) -> int:
        """Return prefix sum for indices 0..i (inclusive)."""
        raise NotImplementedError

    def kth(self, k: int) -> int:
        """
        Return the smallest index i such that prefix_sum(i) >= k.

        k is 1-based (k=1 means "first present position").
        Assume 1 <= k <= total_sum.
        """
        raise NotImplementedError


class FenwickMax:
    """
    Step 2: Fenwick tree / BIT for prefix maximum.

    Supports point updates of the form:
      a[i] = max(a[i], val)
    and queries:
      max(a[0..i])

    This works nicely with offline reverse processing where gap lengths only ever increase.
    """

    def __init__(self, n: int):
        self._n = n
        self._bit = [0] * (n + 1)  # 1-based internally

    def maximize(self, i: int, val: int) -> None:
        """Set a[i] = max(a[i], val)."""
        raise NotImplementedError

    def get(self, i: int) -> int:
        """Return max over indices 0..i (inclusive)."""
        raise NotImplementedError


class Solution:
    """
    LeetCode 3161: Block Placement Queries
    Implement step-by-step and validate with runner.py.
    """

    def getResults(self, queries: List[List[int]]) -> List[bool]:
        """
        Step 3:
        Return results for all type-2 queries, in order.

        Hint ladder:
        - Add sentinels at 0 and at (max coordinate + 1).
        - Collect all obstacles that will ever be added (type-1 queries).
        - Build initial gap lengths between consecutive obstacles into FenwickMax.
        - Process queries in reverse:
          - type 1 becomes "remove obstacle" which merges a gap (gap length increases)
          - type 2 becomes a check using:
              maxGapInPrefix = fenwickMax.get(prevObstacle)
              tailGap        = x - prevObstacle
        """
        raise NotImplementedError

