# LeetCode 1861 - Rotating the Box (Practice Sandbox)

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

Step 1: Gravity (Fall Right Within Each Row)
Implement:
- `_apply_gravity(box)`

Step 2: Rotate 90 Degrees Clockwise
Implement:
- `_rotate_clockwise(box)`

Step 3: Full Solution
Implement:
- `rotateTheBox(box)`

## Notes
- The box contains: `'#'` (stone), `'*'` (obstacle), `'.'` (empty).
- Gravity happens before rotation. Stones fall to the **right** within their row, stopping at obstacles or the right wall.
- Obstacles do not move during gravity; only stones slide within each segment between obstacles.

## LeetCode 1861 - Rotating the Box

Given an `m x n` matrix `box` representing a side-view of a box:
- `'#'` is a stone
- `'*'` is an obstacle
- `'.'` is an empty cell

The box is rotated 90 degrees clockwise. Before rotating, each stone falls down due to gravity (in the original orientation), meaning stones slide as far right as possible within their row, blocked by obstacles.

Return the rotated box after gravity.

### Constraints
- `m == box.length`
- `n == box[i].length`
- `1 <= m, n <= 500`
- `box[i][j]` is one of `'#'`, `'*'`, `'.'`

