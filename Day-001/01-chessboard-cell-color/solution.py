"""
Day 001 — Problem 01: Chessboard Cell Color
============================================

Problem Statement
-----------------
A chessboard can be imagined as a 2D cartesian plane, where:
  - x-axis (files)  → letters a–h
  - y-axis (ranks)  → numbers 1–8

Given a cell coordinate as a string, print whether that cell is White or Black.

Input Format
------------
First line contains a string s.

Output Format
-------------
"White" or "Black"

Constraints
-----------
|s| = 2
s[0] ∈ {a, b, c, d, e, f, g, h}
s[1] ∈ {1, 2, 3, 4, 5, 6, 7, 8}

Sample Testcases
----------------
Input : b2    →  Output : Black
Input : a1    →  Output : Black

Companies
---------
Facebook, MakeMyTrip, Citadel, Hike, Spotify

Topics
------
String, Array

Key Insight
-----------
On a standard chessboard, a1 is black.
Map file letter → number (a=1 … h=8), then:
  (file + rank) is even  →  Black
  (file + rank) is odd   →  White
"""

# ---------------------------------------------------------------------------
# Original version (with known bugs)
# ---------------------------------------------------------------------------

def determine_color(s):
    """
    Original submitted approach.

    Map letter → rank via if/elif, add the digit, then even → Black, odd → White.

    Known issues in this version:
    - `elif [0] == 'c'` should be `elif s[0] == 'c'` (typo: bare list instead of s[0]).
      With that bug, file 'c' always falls through to rank = 8.
    - Long if/elif chain is fragile; letter→number can be done in one expression.
    """
    rank = 0
    number = s[1]

    if s[0] == "a":
        rank = 1
    elif s[0] == "b":
        rank = 2
    elif [0] == "c":  # bug: should be s[0] == "c"
        rank = 3
    elif s[0] == "d":
        rank = 4
    elif s[0] == "e":
        rank = 5
    elif s[0] == "f":
        rank = 6
    elif s[0] == "g":
        rank = 7
    else:
        rank = 8

    result = int(rank) + int(number)

    if result % 2 == 0:
        return "Black"
    else:
        return "White"


# ---------------------------------------------------------------------------
# Improved versions (same formula, cleaner implementation)
# ---------------------------------------------------------------------------


def determine_color_fixed(s):
    """
    Same idea as the original, with the 'c' branch fixed and slightly tightened.

    Improvements:
    - Correct `s[0] == 'c'`
    - Drop unused rank = 0 and redundant int(rank)
    - Keep explicit mapping so the original thinking stays obvious
    """
    number = int(s[1])

    if s[0] == "a":
        rank = 1
    elif s[0] == "b":
        rank = 2
    elif s[0] == "c":
        rank = 3
    elif s[0] == "d":
        rank = 4
    elif s[0] == "e":
        rank = 5
    elif s[0] == "f":
        rank = 6
    elif s[0] == "g":
        rank = 7
    else:
        rank = 8

    result = rank + number
    return "Black" if result % 2 == 0 else "White"


def determine_color_improved(s):
    """
    Best simple form of the same formula.

    Improvements:
    - ord('a')..ord('h') → order 1..8 in one line (no if-chain typos)
    - Single expression for parity → color
    - Same rule: even sum = Black, odd sum = White
    """
    # X-rank order: a→1, b→2, ... h→8
    rank = ord(s[0]) - ord("a") + 1
    # Y-row number from the string
    number = int(s[1])

    result = rank + number
    return "Black" if result % 2 == 0 else "White"


def main():
    import sys

    s = sys.stdin.read().strip()

    # Use the improved solution for correct / concise behavior when running this file.
    # Swap to determine_color(s) to re-run the original submitted version.
    result = determine_color_improved(s)
    print(result)


if __name__ == "__main__":
    main()
