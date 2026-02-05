from typing import List


class Solution:
    """
    LeetCode 68: Text Justification
    Implement step-by-step and validate with runner.py.
    """

    def _pack_lines(self, words: List[str], maxWidth: int) -> List[List[str]]:
        """
        Step 1:
        - Greedily pack words into lines.
        - Return a list of lines, each a list of words.
        """
        raise NotImplementedError

    def _justify_line(self, line_words: List[str], maxWidth: int, is_last: bool) -> str:
        """
        Step 2 & 3:
        - For non-last lines: fully justify.
        - For last lines: left justify (single spaces between words, pad end).
        """
        raise NotImplementedError

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
        Step 3:
        - Use _pack_lines and _justify_line to build final lines.
        """
        raise NotImplementedError
