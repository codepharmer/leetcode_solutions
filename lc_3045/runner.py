import sys

from solution import PairTrie, Solution


def _assert(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def run_step_1() -> None:
    solver = Solution()

    _assert(
        solver._pair_sequence("abcd") == [("a", "d"), ("b", "c"), ("c", "b"), ("d", "a")],
        "Step 1: pair sequence should zip prefix chars with mirrored suffix chars",
    )
    _assert(
        solver._pair_sequence("aba") == [("a", "a"), ("b", "b"), ("a", "a")],
        "Step 1: palindrome should yield symmetric pairs",
    )
    _assert(
        solver._pair_sequence("a") == [("a", "a")],
        "Step 1: single char should map to (c,c)",
    )


def run_step_2() -> None:
    trie = PairTrie()

    trie.insert("a")
    _assert(
        trie.count_matches("aba") == 1,
        "Step 2: 'a' is both prefix and suffix of 'aba'",
    )

    trie.insert("aba")
    _assert(
        trie.count_matches("ababa") == 2,
        "Step 2: both 'a' and 'aba' match 'ababa'",
    )

    _assert(
        trie.count_matches("xyz") == 0,
        "Step 2: unrelated word should have 0 matches",
    )


def run_step_3() -> None:
    solver = Solution()

    words = ["a", "aba", "ababa", "aa"]
    _assert(
        solver.countPrefixSuffixPairs(words) == 4,
        "Step 3: should count all (i<j) where words[i] is prefix and suffix of words[j]",
    )

    words = ["a", "a", "a"]
    _assert(
        solver.countPrefixSuffixPairs(words) == 3,
        "Step 3: duplicates should count combinatorially (3 choose 2 = 3)",
    )

    words = ["pa", "papa", "ma", "mama"]
    _assert(
        solver.countPrefixSuffixPairs(words) == 2,
        "Step 3: should count independent matching pairs",
    )


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

