# Problem 01 — Chessboard Cell Color

## 📌 Problem

**Source:** [Unstop — 100 Days of Code](https://unstop.com/practice/100-days-of-code)

**Topic:** String, Array

**Difficulty:** Easy

**Companies:** Facebook, MakeMyTrip, Citadel, Hike, Spotify

Treat a chessboard as a 2D plane (files `a`–`h`, ranks `1`–`8`). Given a cell as a string of length 2, print whether it is **White** or **Black**.

| | |
| --- | --- |
| **Input** | One string `s` (`\|s\| = 2`) |
| **Output** | `White` or `Black` |
| **Sample** | `b2` → `Black`, `a1` → `Black` |

---

## 🔍 Critical Thinking Approach

How I worked through the problem, step by step:

### 1. Read and frame the problem

I read the statement 2–3 times carefully, then broke the ask into small notes on paper:

* **What I have:** a string coordinate of length 2 (letter + digit).
* **What I’m asked:** print whether that cell is White or Black.
* **What might be going on:** the board is described as a cartesian plane — so this should connect to grids and products of two axes, not just string trivia.

### 2. Understand the board as a grid

I looked at the chessboard diagram and checked the main layout rules:

* The board is **8×8**, like a finite cartesian grid.
* **X-axis** = files `a`–`h` (letters).
* **Y-axis** = ranks `1`–`8` (numbers).
* Every cell is a pair from that product — same idea as a cartesian product of two sets.

### 3. Discover the color pattern (problem half #1)

I drew an **8×8 grid on paper** and filled in black/white from the diagram. Then I searched for a **common pattern** in how colors alternate — not memorizing every square, but why the pattern looks the way it does.

After thinking through how cartesian-product style indexing relates to chess coloring, I landed on the key hint:

* **Even** `(file + rank)` cells → **Black**
* **Odd** `(file + rank)` cells → **White**

(with known squares like `a1` as a check). That resolved the pattern half of the problem.

### 4. Turn the input string into the formula (problem half #2)

With the rule known, the next task was: **one two-character string → apply the formula**.

That part was more mechanical:

1. Treat the string like a tiny array of characters.
2. Index out the two pieces: letter at `s[0]`, digit at `s[1]`.
3. Map the alphabet letter to a rank/value (`a=1 … h=8`).
4. Convert the digit and apply `(file + rank) % 2` → return `"Black"` or `"White"`.

### 5. Recap

Pattern first, formula second:

1. Board = 8×8 cartesian grid → find the color rule.
2. String index + letter→number mapping → plug into that rule.

---

## 📐 Formula Approach

How I stated the color rule:

* Treat the board as a plane:
  * **Y-axis** = rows numbered `1`–`8` (the digit in the input, e.g. `2` in `b2`).
  * **X-axis** = rank labels `a`–`h` (the letter in the input).

* Assign each X rank an **order number**:
  * `a = 1`, `b = 2`, `c = 3`, …, `h = 8`

* Add that order number to the Y-row number:

  ```text
  result = (order of X-rank) + (Y-row number)
  ```

* Decide color from parity of `result`:

  | `result` | Color  |
  | -------- | ------ |
  | even     | Black  |
  | odd      | White  |

**Example**

* `a1` → order(`a`)=1 + Y=1 → `2` (even) → **Black**
* `b2` → order(`b`)=2 + Y=2 → `4` (even) → **Black**
* `a2` → order(`a`)=1 + Y=2 → `3` (odd)  → **White**

In code terms:

```text
result = rank_order(s[0]) + int(s[1])
color  = "Black" if result % 2 == 0 else "White"
```

---

## 🧠 Approach (final formula)

1. Map the X-rank letter to an order number: `a → 1, …, h → 8` (or use `ord(s[0]) - ord('a') + 1`).
2. Read the Y-row as an integer: `int(s[1])`.
3. Compute `result = order + Y`.
4. If `result` is **even** → `"Black"`; if **odd** → `"White"` (matches a1 black).

---

## 💻 Solution

See [`solution.py`](solution.py).

---

## ⏱️ Complexity

**Time:** `O(1)` — fixed-length string, constant work.

**Space:** `O(1)` — a few integers only.

---

## 💡 What I Learned

* Chessboard color is a **parity** problem: one addition and a modulo check.
* `ord()` maps letters to numbers without a long `if` / `elif` chain.
* Sample cases matter for the base rule (a1 black fixes the parity mapping).

---

## 🐛 Mistakes / Challenges

* Typo: wrote `elif [0] == 'c'` instead of `elif s[0] == 'c'`, so file `c` always fell through to `rank = 8`.
* Long `if` chains for `a`–`h` are easy to get wrong; indexing / `ord` is safer.

---

## 🔄 Possible Improvements

* Prefer `ord(s[0]) - ord('a') + 1` (or a small dict) over eight branches.
* Validate input only if the platform does not guarantee `\|s\| = 2`.

---

## 📝 One-Line Takeaway

> Cell color is `(file + rank) % 2` with a1 black as the anchor.
