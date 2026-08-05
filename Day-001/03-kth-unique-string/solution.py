"""
Day 001 — Problem 03: Kth Unique String
=======================================

Problem Statement
-----------------
Ashish has a collection of N strings (duplicates allowed). Find the kth unique
string in the order they first appear.

If there are fewer than k unique strings, display -1.

Input Format
------------
First line: integer N (number of strings)
Next N lines: the strings
Next line: integer k

Output Format
-------------
The kth distinct string, or -1 if fewer than k unique strings exist.

Constraints
-----------
1 <= N <= 10^3
1 <= String.length() <= 10^3

Sample Testcases
----------------
Input:
  6
  d
  b
  c
  b
  c
  a
  2
Output: a
Explanation:
  Distinct (count == 1) in appearance order: "d", then "a".
  k == 2 → "a"

Input:
  3
  dac
  ba
  a
  1
Output: dac

Companies
---------
Amazon

Topics
------
Array, Counting, Hash Map, Sorting, Strings

Key Insight
-----------
Count frequencies first. A string is unique if count == 1.
Walk the list in order and pick the k-th string whose count is 1
(order of first occurrence).
"""


# ---------------------------------------------------------------------------
# Original submitted approach
# ---------------------------------------------------------------------------

def find_unique_num(str_list, k):
    """
    Submitted-style: nested loops + dict of "later-repeat" counts.

    value == 0 was intended to mean "unique".

    Known issues:
    - Re-visiting a duplicate key resets that key's count with
      `repeat_count[elem] = repeat_count.get(elem, 0)`, wiping earlier tallies.
    - O(N^2) nested scans; for N=10^3 this still fits constraints, but is fragile.
    """
    repeat_count = {}
    for index, elem in enumerate(str_list):
        # resets count if elem already seen — buggy for duplicates
        repeat_count[elem] = repeat_count.get(elem, 0)

        for z in range(index + 1, len(str_list)):
            if str_list[z] == elem:
                repeat_count[elem] = repeat_count.get(elem, 0) + 1

    count = 0
    for key, value in repeat_count.items():
        if value == 0:
            if count + 1 == k:
                return key
            else:
                count = count + 1

    return -1


# ---------------------------------------------------------------------------
# Improved: O(N) frequency map, then walk in input order
# ---------------------------------------------------------------------------

def find_kth_unique(str_list, k):
    """
    Correct and simpler version of the same idea.

    1. Count how many times each string appears.
    2. Walk the list once; keep strings whose count == 1 (unique).
    3. Return the k-th such string in first-appearance order, else -1.

    Time: O(N * L) for hashing strings of length L, effectively O(total chars)
    Space: O(N)
    """
    freq = {}
    for s in str_list:
        freq[s] = freq.get(s, 0) + 1

    unique_seen = 0
    for s in str_list:
        if freq[s] == 1:
            unique_seen += 1
            if unique_seen == k:
                return s

    return -1


def main():
    import sys

    n = int(sys.stdin.readline().strip())
    str_list = []
    for _ in range(n):
        str_list.append(sys.stdin.readline().strip())
    k = int(sys.stdin.readline().strip())

    # improved for correct samples; swap to find_unique_num for submitted version
    print(find_kth_unique(str_list, k))


if __name__ == "__main__":
    main()
