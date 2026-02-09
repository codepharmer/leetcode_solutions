from __future__ import annotations

from typing import Optional


class LRUCache:
    """
    LeetCode 146: LRU Cache
    Implement step-by-step and validate with runner.py.
    """

    class _Node:
        __slots__ = ("key", "value", "prev", "next")

        def __init__(self, key: int, value: int) -> None:
            self.key = key
            self.value = value
            self.prev: Optional[LRUCache._Node] = None
            self.next: Optional[LRUCache._Node] = None

    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be positive")

        self._capacity = capacity
        self._cache: dict[int, LRUCache._Node] = {}

        # Sentinels to avoid edge cases when adding/removing.
        self._head = self._Node(-1, -1)  # Most recently used is right after head
        self._tail = self._Node(-1, -1)  # Least recently used is right before tail
        self._head.next = self._tail
        self._tail.prev = self._head

    def _add_to_front(self, node: _Node) -> None:
        """
        Step 1:
        Insert `node` right after `_head` (mark as most recently used).
        """
        raise NotImplementedError

    def _remove(self, node: _Node) -> None:
        """
        Step 1:
        Remove `node` from the linked list.
        """
        raise NotImplementedError

    def _move_to_front(self, node: _Node) -> None:
        self._remove(node)
        self._add_to_front(node)

    def _pop_lru(self) -> _Node:
        """
        Step 1:
        Remove and return the least recently used *real* node (the node before `_tail`).
        """
        raise NotImplementedError

    def get(self, key: int) -> int:
        """
        Step 2:
        Return value if present; otherwise -1.
        Also mark the key as most recently used when found.
        """
        raise NotImplementedError

    def put(self, key: int, value: int) -> None:
        """
        Step 3:
        Insert/update key with value and evict LRU if needed.
        """
        raise NotImplementedError

