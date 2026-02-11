# LeetCode 3045 - Count Prefix and Suffix Pairs II (Practice Sandbox)

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

Step 1: Pair Encoding
Implement:
- `_pair_sequence(word)`

Step 2: Pair-Trie (Insert + Count)
Implement:
- `PairTrie.insert(word)`
- `PairTrie.count_matches(word)`

Step 3: Full Solution
Implement:
- `countPrefixSuffixPairs(words)`

## Notes
- A pair `(i, j)` is valid if `i < j` and `words[i]` is both a prefix and a suffix of `words[j]`.
- This variant has larger constraints, so you want something like `O(total_characters)` time.
- A common trick: build a trie over pairs `(word[k], word[-1-k])` so matching the trie path enforces prefix and suffix at the same time.

