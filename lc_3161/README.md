# LeetCode 3161 - Block Placement Queries (Practice Sandbox)

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

Step 1: Fenwick Tree (Prefix Sums + kth)
Implement:
- `FenwickSum.add(i, delta)`
- `FenwickSum.sum(i)`
- `FenwickSum.kth(k)`

Step 2: Fenwick Tree (Prefix Maximum)
Implement:
- `FenwickMax.maximize(i, val)`
- `FenwickMax.get(i)`

Step 3: Full Solution (Offline Reverse Processing)
Implement:
- `getResults(queries)`

## Notes
- Query type 1: `[1, x]` means build an obstacle at `x` (there is no existing obstacle at `x` when this happens).
- Query type 2: `[2, x, sz]` asks if there exists a length-`sz` block that can be placed entirely within `[0, x]` without intersecting obstacles. Touching obstacles is allowed.
- The intended solution uses offline reverse processing plus Fenwick trees.

