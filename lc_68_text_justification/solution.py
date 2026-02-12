from typing import List


class Solution:
    """
    LeetCode 68: Text Justification
    Implement step-by-step and validate with runner.py.
    """

    def fullJustify(self, words, maxWidth):
        start = 0
        end = 0
        L = 0
        res = []
        n = len(words)

        while end < n:
            if L + len(words[end]) + end - start <= maxWidth:
                L += len(words[end])
                end += 1
                continue
            res.append(self._justify(words, start, end, L, maxWidth, last_line=False))

            start = end
            L = 0
        res.append(self._justify(words,start, end, L, maxWidth, last_line= True))

        return res
    
    def _justify(self, words, start, end, L, maxWidth, last_line):
        line_words = words[start: end]
        num_words = end-start
        if last_line or num_words == 1:
            line = " ".join(line_words)
            return line+ " "*(maxWidth-len(line))
        gaps = num_words -1

        spaces_total = maxWidth - L
        q, r = divmod(spaces_total, gaps)

        out = []
        for i in range(gaps):
            out.append(line_words[i])
            out.append(" "*(q+(1 if i <r else 0)))
        out.append(line_words[-1])
        return "".join(out)