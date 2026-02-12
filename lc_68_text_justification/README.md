# LeetCode 68 - Text Justification (Practice Sandbox)

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

Step 1: Greedy Line Packing
Implement:
- `_pack_lines(words, maxWidth)`

Step 2: Line Justification (Non-Last Lines)
Implement:
- `_justify_line(line_words, maxWidth, is_last=False)`

Step 3: Last Line + Full Solution
Implement:
- `_justify_line(..., is_last=True)`
- `fullJustify(words, maxWidth)`

## Notes
- The runner uses only built-in Python; no extra dependencies.
- Tests call `_pack_lines` and `_justify_line` directly to help with incremental progress.

## LeetCode 68 - Text Justification

Given an array of strings `words` and a width `maxWidth`, format the text so that each line has exactly `maxWidth` characters and is fully (left and right) justified.

Use a greedy approach: pack as many words as you can in each line. Pad extra spaces `' '` when necessary so each line has exactly `maxWidth` characters. Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the leftmost gaps get more spaces than the rightmost gaps.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:
- A word is a sequence of non-space characters.
- Each word's length is greater than 0 and does not exceed `maxWidth`.
- `words` contains at least one word.

### Example 1

Input:
```text
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
```

Output:
```text
[
  "This    is    an",
  "example  of text",
  "justification.  "
]
```

### Example 2

Input:
```text
words = ["What", "must", "be", "acknowledgment", "shall", "be"]
maxWidth = 16
```

Output:
```text
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
```

Explanation:
- The last line is left-justified.
- A non-last line with a single word is also left-justified.

### Example 3

Input:
```text
words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"]
maxWidth = 20
```

Output:
```text
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
```

### Constraints
- `1 <= words.length <= 300`
- `1 <= words[i].length <= 20`
- `words[i]` consists of only English letters and symbols
- `1 <= maxWidth <= 100`
- `words[i].length <= maxWidth`
