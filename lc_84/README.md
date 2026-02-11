# LeetCode 84 - Largest Rectangle in Histogram (Practice Sandbox)

This is a step-by-step practice setup. You implement the `Solution` class in `solution.py` and run the step runner to validate progress.

## Quick Start

Run a specific step:

```bash
python runner.py 1
python runner.py 2
python runner.py 3
```

Run all steps (defaults to step 3):

```bash
python runner.py
```

## Step Plan

Step 1: Previous Smaller Index (to the left)
Implement:
- `_prev_smaller_indices(heights)`

Step 2: Next Smaller Index (to the right)
Implement:
- `_next_smaller_indices(heights)`

Step 3: Largest Rectangle Area
Implement:
- `largestRectangleArea(heights)`

## Notes
- The intended solution is `O(n)` time using a monotonic increasing stack of indices.
- In steps 1 and 2, treat "smaller" as **strictly** smaller. (Pop while `>=` to handle equal heights correctly.)

## LeetCode 84 - Largest Rectangle in Histogram

Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

### Example 1

Input:
```text
heights = [2,1,5,6,2,3]
```

Output:
```text
10
```

Explanation: The largest rectangle has area 10.

### Example 2

Input:
```text
heights = [2,4]
```

Output:
```text
4
```

### Constraints
- `1 <= heights.length <= 10^5`
- `0 <= heights[i] <= 10^4`

