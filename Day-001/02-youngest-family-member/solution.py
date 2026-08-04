"""
Day 001 — Problem 02: Youngest Family Member
============================================

Problem Statement
-----------------
The royal family exchanges gifts at Christmas. The youngest member receives
gifts from everyone else but does not give any gifts.

Given all gift exchanges, identify the youngest member.

Note: A family member does not give more than one gift to the same member.

Input Format
------------
First line: two integers n and m
  - n = number of family members
  - m = number of gifts exchanged
Next m lines: ai bi  (ai gives a gift to bi)

Output Format
-------------
A single integer: the youngest member's number.
If no such member exists, print -1.

Constraints
-----------
1 <= n <= 10^4
0 <= m <= 10^5
1 <= ai, bi <= n

Sample Testcases
----------------
Input:
  2 1
  1 2
Output: 2

Input:
  3 2
  1 3
  2 3
Output: 3

Topics
------
Hash Table, Graph, Hashing, Array

Key Insight
-----------
Receiver count for youngest must be n - 1 (gift from every other member).
Also give count must be 0. Base: m == 0 → 1 only if n == 1.
"""


# ---------------------------------------------------------------------------
# Original submitted approach (dict of receiver counts)
# ---------------------------------------------------------------------------

def find_youngest_member(n, m, gifts):
    """
    Submitted-style solution: count receives in a dict; look for count == n-1.

    Critical-thinking derivation:
    - Not m (total gifts) — a person can receive at most once per other person.
    - Must be n-1 (everyone else).
    - m == 0: return 1 only when n == 1, else -1.
    """
    # Base: no gifts → only valid when a sole family member exists
    if m == 0:
        return 1 if n == 1 else -1

    # receiver[member] = how many gifts they received
    receiver = {}
    for _giver, item in gifts:
        receiver[item] = receiver.get(item, 0) + 1

    # k+1 walks member ids 1..n (dicts keyed by receivers start at those ids, not 0)
    for k in range(n):
        if receiver.get(k + 1) == n - 1:
            return k + 1

    return -1


# ---------------------------------------------------------------------------
# Improved: also enforce "gives no gifts" (full statement)
# ---------------------------------------------------------------------------

def find_youngest_member_improved(n, m, gifts):
    """
    Same n-1 receive rule, plus give-count == 0.

    Why: someone can receive from everyone and still give gifts; they are not youngest.
    """
    if m == 0:
        return 1 if n == 1 else -1

    given = {}
    received = {}

    for giver, receiver in gifts:
        given[giver] = given.get(giver, 0) + 1
        received[receiver] = received.get(receiver, 0) + 1

    for member in range(1, n + 1):
        if received.get(member, 0) == n - 1 and given.get(member, 0) == 0:
            return member

    return -1


def main():
    import sys

    data = sys.stdin.read().strip().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])

    gifts = []
    index = 2
    for _ in range(m):
        a_i = int(data[index])
        b_i = int(data[index + 1])
        gifts.append((a_i, b_i))
        index += 2

    # improved enforces full statement; swap to find_youngest_member to re-run submitted logic
    print(find_youngest_member_improved(n, m, gifts))


if __name__ == "__main__":
    main()
