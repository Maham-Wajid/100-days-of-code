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
Walk keys in first-appearance order (dict insertion order, or the list)
and return the k-th string with count == 1.
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
        # resets if key already exists — can wipe prior tallies on revisits
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
# Optimized submitted: O(N) frequency map + walk dict in insert order
# ---------------------------------------------------------------------------

def find_kth_unique(str_list, k):
    """
    Optimized submitted solution.

    1. Count total frequency of each string (one pass).
    2. Walk the dict in insertion order (first appearance in Python 3.7+).
    3. Keep keys with freq == 1; return the k-th such key, else -1.

    Note: for strings with freq == 1, dict insertion order matches first
    appearance order in the list, so this equals walking the list.
    """
    freq = {}
    for elem in str_list:
        freq[elem] = freq.get(elem, 0) + 1

    count = 0
    for key, value in freq.items():
        if value == 1:
            if count + 1 == k:
                return key
            count = count + 1

    return -1


def main():
    import sys

    n = int(sys.stdin.readline().strip())
    str_list = []
    for _ in range(n):
        str_list.append(sys.stdin.readline().strip())
    k = int(sys.stdin.readline().strip())

    # optimized submitted version; swap to find_unique_num for first attempt
    print(find_kth_unique(str_list, k))


if __name__ == "__main__":
    main()
