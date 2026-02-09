import sys

from lru_cache import LRUCache


def _assert(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def _keys_mru_to_lru(cache: LRUCache) -> list[int]:
    out: list[int] = []
    cur = cache._head.next
    while cur is not None and cur is not cache._tail:
        out.append(cur.key)
        cur = cur.next
    return out


def run_step_1() -> None:
    cache = LRUCache(2)

    _assert(cache._head.next is cache._tail, "Step 1: empty list should be head <-> tail")
    _assert(cache._tail.prev is cache._head, "Step 1: empty list should be head <-> tail")

    n1 = cache._Node(1, 1)
    n2 = cache._Node(2, 2)

    cache._add_to_front(n1)
    _assert(_keys_mru_to_lru(cache) == [1], "Step 1: after adding 1, order should be [1]")

    cache._add_to_front(n2)
    _assert(_keys_mru_to_lru(cache) == [2, 1], "Step 1: after adding 2, order should be [2, 1]")

    cache._remove(n2)
    _assert(_keys_mru_to_lru(cache) == [1], "Step 1: after removing 2, order should be [1]")

    cache._add_to_front(n2)
    _assert(_keys_mru_to_lru(cache) == [2, 1], "Step 1: after re-adding 2, order should be [2, 1]")

    lru = cache._pop_lru()
    _assert(lru.key == 1, "Step 1: pop should remove the least recently used key (1)")
    _assert(_keys_mru_to_lru(cache) == [2], "Step 1: after pop, order should be [2]")


def run_step_2() -> None:
    cache = LRUCache(2)

    n1 = cache._Node(1, 1)
    n2 = cache._Node(2, 2)

    cache._cache[1] = n1
    cache._cache[2] = n2
    cache._add_to_front(n1)
    cache._add_to_front(n2)

    _assert(_keys_mru_to_lru(cache) == [2, 1], "Step 2: setup order should be [2, 1]")

    _assert(cache.get(1) == 1, "Step 2: get(1) should return 1")
    _assert(_keys_mru_to_lru(cache) == [1, 2], "Step 2: get should mark key as most recently used")

    _assert(cache.get(3) == -1, "Step 2: get(missing) should return -1")
    _assert(_keys_mru_to_lru(cache) == [1, 2], "Step 2: get(missing) should not change ordering")


def run_step_3() -> None:
    cache = LRUCache(2)

    cache.put(1, 1)
    _assert(_keys_mru_to_lru(cache) == [1], "Step 3: after put(1), order should be [1]")

    cache.put(2, 2)
    _assert(_keys_mru_to_lru(cache) == [2, 1], "Step 3: after put(2), order should be [2, 1]")

    _assert(cache.get(1) == 1, "Step 3: get(1) should return 1")
    _assert(_keys_mru_to_lru(cache) == [1, 2], "Step 3: get should update ordering")

    cache.put(3, 3)
    _assert(cache.get(2) == -1, "Step 3: key 2 should have been evicted")
    _assert(_keys_mru_to_lru(cache) == [3, 1], "Step 3: after put(3), order should be [3, 1]")

    cache.put(4, 4)
    _assert(cache.get(1) == -1, "Step 3: key 1 should have been evicted")

    _assert(cache.get(3) == 3, "Step 3: get(3) should return 3")
    _assert(cache.get(4) == 4, "Step 3: get(4) should return 4")

    # Update existing key should refresh recency
    cache.put(3, 30)
    _assert(cache.get(3) == 30, "Step 3: updating existing key should change stored value")
    _assert(_keys_mru_to_lru(cache)[0] == 3, "Step 3: updated key should become most recently used")


def main() -> None:
    if len(sys.argv) > 2:
        raise SystemExit("Usage: python runner.py [step]")

    step = 3
    if len(sys.argv) == 2:
        try:
            step = int(sys.argv[1])
        except ValueError as exc:
            raise SystemExit("Step must be an integer: 1, 2, or 3") from exc

    if step == 1:
        run_step_1()
    elif step == 2:
        run_step_1()
        run_step_2()
    elif step == 3:
        run_step_1()
        run_step_2()
        run_step_3()
    else:
        raise SystemExit("Step must be 1, 2, or 3")

    print(f"Step {step} passed.")


if __name__ == "__main__":
    main()

