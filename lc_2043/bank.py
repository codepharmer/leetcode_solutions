from typing import List


class Bank:
    """
    LeetCode 2043: Simple Bank System
    Implement methods step-by-step and validate with runner.py.
    """

    def __init__(self, balance: List[int]):
        self._balances = balance
        self._n = len(self._balances)

    def _is_valid(self, account: int) -> bool:
        if account >= 1 and account <= self._n:
            return True
        else:
            return False

    def _has_funds(self, account: int, money: int) -> bool:
        if not self._is_valid(account):
            return False
        if self._balances[account-1] >= money:
            return True
        else:
            return False

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        """
        Step 3:
        - Validate both accounts
        - Ensure account1 has enough funds
        - Move money and return True, otherwise False
        """
        if not (self._is_valid(account1) and self._is_valid(account2)):
            return False
        if not self._has_funds(account1, money):
            return False
        else:
            self._balances[account2 -1] += money
            self._balances[account1 -1] -= money
            return True
        return False


    def deposit(self, account: int, money: int) -> bool:
        """
        Step 2:
        - Validate account
        - Add money and return True, otherwise False
        """
        if self._is_valid(account):
            self._balances[account-1] += money
            return True
        else:
            return False 

    def withdraw(self, account: int, money: int) -> bool:
        """
        Step 2:
        - Validate account
        - Ensure enough funds
        - Subtract money and return True, otherwise False
        """
        if self._is_valid(account) and self._has_funds(account, money):
            self._balances[account-1] -= money
            return True
        else:
            return False
