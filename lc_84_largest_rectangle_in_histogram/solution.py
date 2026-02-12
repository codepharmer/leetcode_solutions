from typing import List


class Solution:
    """
    LeetCode 84: Largest Rectangle in Histogram
    Implement step-by-step and validate with runner.py.
    """

    def _prev_smaller_indices(self, heights: List[int]) -> List[int]:
        """
        Step 1:
        For each i, return the index of the closest bar to the left with height < heights[i].
        If none exists, use -1.

        Hint: maintain a monotonic increasing stack of indices.
        Pop while the top is >= current height (>= handles equal heights correctly).
        """
        raise NotImplementedError

    def _next_smaller_indices(self, heights: List[int]) -> List[int]:
        """
        Step 2:
        For each i, return the index of the closest bar to the right with height < heights[i].
        If none exists, use n (len(heights)).

        Hint: same monotonic stack idea, but scan from right to left.
        """
        raise NotImplementedError

    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Step 3:
        Use the previous-smaller and next-smaller boundaries to compute the max rectangle.

        For each bar i:
          width = next_smaller[i] - prev_smaller[i] - 1
          area  = heights[i] * width
        Answer is max area over all i.
        """
        max_area = 0
        stack = []

        for  i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_arean, height* (i-index))
                start = index

            stack.append((start, h))
        
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        
        return max_area


