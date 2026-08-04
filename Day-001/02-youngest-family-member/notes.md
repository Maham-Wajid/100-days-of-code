# Problem 02 — Youngest Family Member

## 📌 Problem

**Source:** [Unstop — 100 Days of Code](https://unstop.com/practice/100-days-of-code)

**Topic:** Hash Table, Graph, Hashing, Array

**Difficulty:** Easy–Medium

Among `n` family members and `m` directed gifts (`ai → bi`), find the youngest: the one who **receives a gift from every other member** and **gives no gifts**. Print their id, or `-1` if none.

| | |
| --- | --- |
| **Input** | `n m`, then `m` lines of `ai bi` |
| **Output** | Member id or `-1` |
| **Sample** | `n=2, m=1, gift 1→2` → `2`; `n=3, gifts 1→3, 2→3` → `3` |

---

## 🔍 Critical Thinking Approach

How I worked through the problem, step by step:

### 1. Frame the problem

First I wrote down:

* **What is given:** `n` family members, `m` gift exchanges, each exchange is a directed pair (`giver → receiver`).
* **What is asked:** find the youngest member by gift rules, or `-1` if none.

I re-read the statement a few times and broke it into smaller questions instead of coding immediately.

### 2. Start from a tiny case (core logic)

With **2 members** and **1 gift** (`1 → 2`):

* Someone ends up with a higher receiving count.
* That “must be the youngest” only if they received from **everyone else**, not just “a lot of gifts.”

So: how large should that max receiving count be?

### 3. Reject the wrong target, lock `n - 1`

Two candidates for “how max?”:

| Candidate target | Idea | Why it fails / works |
| --- | --- | --- |
| **= m (total gifts)** | Youngest gets every gift in the list | Invalid as a general rule — gifts can go to different people, and one person can give multiple gifts (to different members). |
| **= n − 1** | Receives once from each other member | Fits the statement: at most one gift between the same pair, must get from **all others** → exclude self → **`n − 1`**. |

That finalized the main numerical rule:

```text
youngest candidate must have receive_count == n - 1
```

### 4. Handle `m = 0` carefully (not always `-1`)

If there are **no gifts**, the usual intuition is “nobody got gifts from everyone → `-1`.”

But there is a special case:

* **`n == 1`:** only one family member; “everyone else” is empty, so they vacuously receive from all others and give nothing → **return `1`**.
* **`n > 1` and `m == 0`:** impossible to have receive count `n - 1` → **`-1`**.

### 5. Default fallback

If no member has receive count `n - 1` (and not the `n == 1` base), return **`-1`**.

### 6. Coding decisions

After the logic was clear:

1. First considered a **list** of receiver counts.
2. Switched to a **dictionary** keyed by family member id:
   * easy to **increment** on each received gift;
   * keys are exactly members who appear as receivers;
   * scan members with `k + 1` over `range(n)` so ids stay `1..n` (dicts built from receivers never start at 0).
3. After counting, look for the key whose value equals **`n - 1`**.

### 7. Recap of my path

```text
1. Note given vs asked
2. Re-read and break the problem down
3. Validate rule on small n=2 case
4. Try receive == m  → reject (multi-gift / multi-receiver confusion)
5. Settle on receive == n - 1
6. Special-case n == 1 when m == 0
7. Implement with a dict of receiver counts → scan for n-1 → else -1
```

### Extra check (full problem statement)

The statement also says the youngest **does not give any gifts**.  
Receive count `== n - 1` is necessary; for full correctness also ensure **give count == 0** (or that member never appears as `ai`).  
On many sample-style inputs, the “everyone gives them a gift” person also gives none — still worth tracking givers when polishing the solution.

---

## 📐 Formula / conditions

```text
# core rule I derived
candidate by receiving:  received[x] == n - 1

# full problem (ideal)
youngest(x)  ⇔  received[x] == n - 1  AND  given[x] == 0

# base cases
if m == 0:
    answer = 1 if n == 1 else -1
```

---

## 🧠 Approach (final)

1. Base: if `m == 0` → `1` when `n == 1`, else `-1`.
2. Count receives (dict or array) from each gift’s receiver.
3. Optionally count gives so “gives none” is enforced.
4. Find member with `received == n - 1` (and `given == 0`); else `-1`.

---

## 💻 Solution

See [`solution.py`](solution.py).

---

## ⏱️ Complexity

**Time:** `O(n + m)` — count gifts, scan members.

**Space:** `O(n)` — dict/array of counts.

---

## 💡 What I Learned

* Build the numeric rule from a **small hand case**, then generalize.
* “Max” is not always `m` — domain rules matter (`n - 1` from “everyone else”).
* Dicts are natural when keys are member ids and you only care about increments/lookups.
* Always probe edge cases like **`m = 0`** before coding the happy path only.

---

## 🐛 Mistakes / Challenges

* Nearly aimed receive count at **`m`**, then discarded after realizing one person can give several gifts to different people.
* `m = 0` is not always `-1` — **`n == 1`** is the exception.
* Easy to implement only receive counts and forget the **“gives none”** requirement in messier graphs.

---

## 🔄 Possible Improvements

* Track both **received** and **given** for full statement fidelity.
* Arrays of size `n + 1` avoid hash overhead under dense member ids.
* Stop early once a valid unique candidate is confirmed.

---

## 📝 One-Line Takeaway

> Youngest receives from all others (`received == n−1`); start from a 2-person case, reject “max == m,” special-case `n == 1`.
