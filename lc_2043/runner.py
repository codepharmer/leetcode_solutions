import sys

from bank import Bank


def _assert(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def run_step_1() -> None:
    bank = Bank([10, 100, 20, 50, 30])

    _assert(bank._is_valid(1) is True, "Step 1: account 1 should be valid")
    _assert(bank._is_valid(5) is True, "Step 1: account 5 should be valid")
    _assert(bank._is_valid(0) is False, "Step 1: account 0 should be invalid")
    _assert(bank._is_valid(6) is False, "Step 1: account 6 should be invalid")

    _assert(bank._has_funds(3, 20) is True, "Step 1: account 3 has $20")
    _assert(bank._has_funds(3, 21) is False, "Step 1: account 3 should not have $21")
    _assert(bank._has_funds(10, 1) is False, "Step 1: invalid account should fail funds check")


def run_step_2() -> None:
    bank = Bank([10, 100, 20, 50, 30])

    _assert(bank.withdraw(3, 10) is True, "Step 2: withdraw should succeed")
    _assert(bank._balances[2] == 10, "Step 2: account 3 should now have $10")

    _assert(bank.withdraw(3, 11) is False, "Step 2: withdraw should fail for insufficient funds")
    _assert(bank._balances[2] == 10, "Step 2: account 3 balance should remain $10")

    _assert(bank.deposit(5, 20) is True, "Step 2: deposit should succeed")
    _assert(bank._balances[4] == 50, "Step 2: account 5 should now have $50")

    _assert(bank.deposit(10, 20) is False, "Step 2: deposit should fail for invalid account")


def run_step_3() -> None:
    bank = Bank([10, 100, 20, 50, 30])

    _assert(bank.withdraw(3, 10) is True, "Step 3: withdraw should succeed")
    _assert(bank.transfer(5, 1, 20) is True, "Step 3: transfer should succeed")
    _assert(bank.deposit(5, 20) is True, "Step 3: deposit should succeed")
    _assert(bank.transfer(3, 4, 15) is False, "Step 3: transfer should fail (insufficient funds)")
    _assert(bank.withdraw(10, 50) is False, "Step 3: withdraw should fail (invalid account)")

    _assert(bank._balances == [30, 100, 10, 50, 30], "Step 3: balances should match example")


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
