# LeetCode 723 - Candy Crush (Practice Sandbox)

This is a step-by-step practice setup. You implement the `Solution` class in `solution.py` and run the step runner to validate progress.

## Quick Start

Run a specific step:

```bash
python runner.py 1
python runner.py 2
python runner.py 3
python runner.py 4
```

Run all steps (defaults to step 4):

```bash
python runner.py
```

## Step Plan

Step 1: Find Crushable Cells
Implement:
- `_find_crushes(board)`

Step 2: Gravity
Implement:
- `_apply_gravity(board)`

Step 3: Full Simulation
Implement:
- `candyCrush(board)`

Step 4: Extra Tests (Regression + Fuzzing)
Run:
- `python runner.py 4`

## Notes
- A cell is crushable if it is part of a horizontal or vertical group of **3 or more** equal values.
- Zeros are empty and should never be considered a candy.
- After crushing, apply gravity column-by-column so non-zero candies fall down.

## LeetCode 723 - Candy Crush

You are given an `m x n` integer matrix `board` where each value represents a type of candy, and `0` represents an empty cell.

Repeatedly do the following until the board is stable:
1. Crush (remove) all candies that are part of a horizontal or vertical sequence of at least 3 equal candies.
2. Let the remaining candies fall down due to gravity, filling empty spaces.

Return the stable board.

### Constraints
- `3 <= m, n <= 50`
- `0 <= board[i][j] <= 2000`
