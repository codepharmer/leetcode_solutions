from typing import List
from sortedcontainers import SortedList

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
        while i <= self._n:
            self._bit[i] = max(self._bit[i], val)
            i += i & (-i)

    def get(self, i: int) -> int:
        """Return max over indices 0..i (inclusive)."""
        result = 0
        while i > 0:
            result = max(result, self._bit[i])
            i -= i & (-i)
        return result

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

        n = min(50000, len(queries) * 3)
        tree = FenwickMax(n+1)
        obstacles = SortedList([0, n+1])

        for q in queries:
             if q[0] == 1:
                obstacles.add(q[1])
            
        for i in range(1, len(obstacles)):
            gap = obstacles[i] - obstacles[i-1]
            tree.maximize(obstacles[i], gap)
        
        results = []

        for q in reversed(queries):
            if q[0] == 1:
                x = q[1]
                idx = obstacles.index(x)
                prev = obstacles[idx-1]
                nxt = obstacles[idx+1]
                obstacles.remove(x)
                tree.maximize(nxt, nxt-prev)
            else:
                x, sz = q[1], q[2]
                max_gap = tree.get(x)
                idx = obstacles.bisect_right(x) -1
                last_obs = obstacles[idx]
                max_gap = max(max_gap, x - last_obs)
                results.append(max_gap >= sz)
        
        results.reverse()

        return results
