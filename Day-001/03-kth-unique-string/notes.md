# Problem 03 — Kth Unique String

## 📌 Problem

**Source:** [Unstop — 100 Days of Code](https://unstop.com/practice/100-days-of-code)

**Topic:** Array, Counting, Hash Map, Strings

**Difficulty:** Easy

**Companies:** Amazon

Given `N` strings (duplicates allowed) and an integer `k`, print the **kth unique** string in **first-appearance order**. If fewer than `k` unique strings exist, print `-1`.

| | |
| --- | --- |
| **Input** | `N`, then `N` strings, then `k` |
| **Output** | kth unique string or `-1` |
| **Sample** | `d,b,c,b,c,a` with `k=2` → `a` (uniques in order: `d`, `a`) |

---

## 🔍 Critical Thinking Approach

How I worked through the problem, step by step:

### 1. Break the problem into steps

I split the ask into clear pieces:

* We are given a **list of strings** (order matters).
* **Unique** means a string that appears **exactly once** in the whole list.
* Among those unique strings, keep the order of their first (and only) appearance.
* Return the one at index **`k`** (1-based). If not enough uniques → **`-1`**.

### 2. How to detect “appeared more than once”

I thought about iterating the list so I can mark values that show up more than once.

Choice: **two loops**

1. Outer loop: stand on each element (starting from the first).
2. Inner loop: only scan **positions after** the current index (no need to look back — earlier occurrences already “claimed” tracking from before).
3. Store per-string **repeat counts** in a **dictionary**.

Concrete plan:

* First time I “own” a string at index `i`, put key = string, **value = 0**.
* Scan `i+1 … end`; each later match → increment that key’s value.
* After counting: **value == 0** means no later repeats → unique (in this counting scheme).

Then another loop over **dictionary items** (insertion / first-seen order in Python 3.7+):

* if value is `0` → unique candidate;
* bump a counter of uniques so far;
* when counter hits `k` → return that key;
* if none match → `-1`.

### 3. Why this path made sense

* Nested loops felt natural for “compare me with everything after me.”
* A dict made incrementing per string easy without parallel arrays.
* Separating **count phase** from **pick kth phase** kept the logic readable.

### 4. Recap of my path

```text
1. Break: list → uniques (count==once) → kth in order → else -1
2. Nested loops: for each index i, count later equals of str_list[i]
3. Dict: key = string, value = how many later repeats (0 ⇒ unique)
4. Walk dict items; on value==0, count unique rank; if rank==k return key
5. Fallback -1
```

### 5. What to watch / improve

* On a second visit to a **duplicate** string, resetting the dict entry with  
  `repeat_count[elem] = repeat_count.get(elem, 0)` can **wipe** earlier counts.
* A cleaner approach (same idea, less fragile):
  1. One pass: `freq[s] += 1` for all strings.
  2. One pass in input order: keep `s` where `freq[s] == 1`, return the kth.

---

## 📐 Formula / conditions

```text
unique(s)  ⇔  frequency(s) == 1   (over the whole list)

answer = k-th unique string in first-appearance order
       = -1 if fewer than k unique strings
```

Submitted counting idea:

```text
later_repeats[s] -- increment when s appears after first consideration
unique-style score: later_repeats[s] == 0   (intended)
```

Preferred counting:

```text
freq[s] = total occurrences of s
walk list left→right; collect s where freq[s]==1; pick index k
```

---

## 🧠 Approach (final)

1. Count frequency of every string (hash map).
2. Walk the original list in order.
3. Skip strings with frequency ≠ 1.
4. Return the kth string that passes; else `-1`.

---

## 💻 Solution

See [`solution.py`](solution.py).

---

## ⏱️ Complexity

| Version | Time | Space |
| --- | --- | --- |
| Submitted (nested loops) | `O(N²)` string compares | `O(U)` unique keys |
| Improved (freq + walk) | `O(N)` | `O(U)` |

Constraints: `N ≤ 10³` so both can pass; improved is clearer and safer.

---

## 💡 What I Learned

* “Kth unique” = filter by **freq == 1**, then take order from the **original sequence**.
* Hash maps are natural for frequency / unique detection.
* Nested loops can discover uniqueness but easy to mishandle when revisiting a key already in the map.

---

## 🐛 Mistakes / Challenges

* Re-initializing a dict key on every outer-loop hit can **overwrite** a correct non-zero count when the string appears again.
* Need to preserve **first-appearance order** of uniques, not arbitrary map order alone (improved walk fixes this explicitly).

---

## 🔄 Possible Improvements

* Prefer total frequency + single ordered walk (`find_kth_unique`).
* Use `collections.Counter` for frequency if you like standard library helpers.

---

## 📝 One-Line Takeaway

> Count frequencies, then walk in input order and return the kth string with `freq == 1`.
