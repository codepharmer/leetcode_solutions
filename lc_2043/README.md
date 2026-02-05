# LeetCode 2043 — Simple Bank System (Practice Sandbox)

This is a tiny step-by-step practice setup. You implement the `Bank` class in `bank.py` and run the step runner to validate progress as you go.

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

Step 1: Class + Guards  
Implement:
- `__init__`
- `_is_valid(account)`
- `_has_funds(account, money)`

Step 2: Single-Account Ops  
Implement:
- `deposit(account, money)`
- `withdraw(account, money)`

Step 3: Transfer  
Implement:
- `transfer(account1, account2, money)`

## Notes
- The runner uses only built-in Python; no extra dependencies.
- The tests read `bank._balance` directly to verify state changes.


## LeetCode 2043 — Simple Bank System

**Difficulty:** Medium

### Problem Statement
You have been tasked with writing a program for a bank that will automate all incoming transactions (`transfer`, `deposit`, and `withdraw`). The bank has `n` accounts numbered from `1` to `n`. The initial balance of each account is stored in a 0-indexed integer array `balance`, with the `(i + 1)`th account having an initial balance of `balance[i]`.

Execute all **valid** transactions. A transaction is valid if:
1. The given account number(s) are between `1` and `n`.
2. The amount of money withdrawn or transferred from an account is less than or equal to that account's balance.

### API
- `Bank(long[] balance)`  
  Initializes the object with the 0-indexed integer array `balance`.
- `boolean transfer(int account1, int account2, long money)`  
  Transfers `money` dollars from `account1` to `account2`. Return `true` if the transaction succeeds, otherwise `false`.
- `boolean deposit(int account, long money)`  
  Deposits `money` dollars into `account`. Return `true` if the transaction succeeds, otherwise `false`.
- `boolean withdraw(int account, long money)`  
  Withdraws `money` dollars from `account`. Return `true` if the transaction succeeds, otherwise `false`.

### Example 1

**Input**
```text
["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"]
[[[10, 100, 20, 50, 30]], [3, 10], [5, 1, 20], [5, 20], [3, 4, 15], [10, 50]]
```

**Output**
```text
[null, true, true, true, false, false]
```

**Explanation**
```text
Bank bank = new Bank([10, 100, 20, 50, 30]);
bank.withdraw(3, 10);    // true: account 3 has $20, withdraw $10 -> $10 remaining
bank.transfer(5, 1, 20); // true: account 5 has $30, transfer $20 -> $10; account 1 -> $30
bank.deposit(5, 20);     // true: deposit $20 -> account 5 becomes $30
bank.transfer(3, 4, 15); // false: account 3 has $10, cannot transfer $15
bank.withdraw(10, 50);   // false: account 10 does not exist
```

### Constraints
- `n == balance.length`
- `1 <= n, account, account1, account2 <= 10^5`
- `0 <= balance[i], money <= 10^12`
- At most `10^4` calls will be made to each function `transfer`, `deposit`, `withdraw`.
