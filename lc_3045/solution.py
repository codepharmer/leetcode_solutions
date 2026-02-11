from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Tuple


@dataclass
class _TrieNode:
    children: Dict[Tuple[str, str], "_TrieNode"] = field(default_factory=dict)
    end_count: int = 0


class PairTrie:
    """
    Step 2:
    Trie over pairs (word[k], word[-1-k]).

    If you walk the pair path for a word w, then at depth d you represent the condition:
      candidate == w[:d] AND candidate == w[-d:]
    because pairs enforce both ends simultaneously.
    """

    def __init__(self) -> None:
        self._root = _TrieNode()

    def insert(self, word: str) -> None:
        """
        Insert a word into the pair-trie.
        """
        raise NotImplementedError

    def count_matches(self, word: str) -> int:
        """
        Count how many previously-inserted words are both a prefix and a suffix of `word`.

        Hint: as you traverse, accumulate `node.end_count` at each depth.
        """
        raise NotImplementedError


class Solution:
    """
    LeetCode 3045: Count Prefix and Suffix Pairs II
    Implement step-by-step and validate with runner.py.
    """

    def _pair_sequence(self, word: str) -> List[Tuple[str, str]]:
        """
        Step 1:
        Return the list of pairs (word[i], word[-1-i]) for i=0..len(word)-1.
        """
        raise NotImplementedError

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        """
        Step 3:
        Return the number of pairs (i, j) such that i < j and words[i] is both a prefix
        and a suffix of words[j].

        Typical flow:
        - create a PairTrie
        - for each word w in words:
            ans += trie.count_matches(w)
            trie.insert(w)
        """
        raise NotImplementedError


class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init(self):
        self.root = TrieNode()
    
    def add(self, w):
        cur = self.root

        for c1, c2 in zip(w, reversed(w)):
            if (c1, c2) not in cur.children:
                cur.children[(c1, c2)] = TrieNode()
            cur = cur.children[(c1, c2)]
            cur.count += 1
    
    def count(self, w):
        cur = self.root

        for c1, c2 in zip(w, reversed(w)):
            if (c1, c2) not in cur.children:
                return 0
            cur = cur.children[(c1, c2)]
        return cur.count

class Solution:
    def countPrefixSuffixPairs(self, words):
        res = 0

        root = Trie()

        for w in reversed(words):
            res += root.count(w)
            root.add(w)
        return res