# 🚀 Day 001

**Date:** August 5, 2026

## 📊 Today's Progress

| #  | Problem                                                  | Topic                 | Difficulty | Status |
| -- | -------------------------------------------------------- | --------------------- | ---------- | ------ |
| 01 | [Chessboard Cell Color](./01-chessboard-cell-color/)     | String, Array         | Easy       | ✅      |
| 02 | [Youngest Family Member](./02-youngest-family-member/)   | Graph, Hashing, Array | Easy       | ✅      |
| 03 | [Kth Unique String](./03-kth-unique-string/)             | Hash Map, Strings     | Easy       | ✅      |

**Progress:** `3 / 3` ✅

---

## 🧠 Today's Takeaways

### Problem 01 — Chessboard Cell Color

> Map file letter to a number; black/white is just the parity of `(file + rank)` with a1 black.

### Problem 02 — Youngest Family Member

> Youngest = unique person with out-degree 0 and in-degree n−1 (receives from all, gives none).

### Problem 03 — Kth Unique String

> Count frequencies, then walk first-appearance order and return the kth string with `freq == 1`.

---

## 💭 Daily Reflection

**What went well?**

Three different shapes same day: grid parity, graph degrees, frequency + ordered walk. Each had a clear structural rule once rephrased.

**What was difficult?**

P01: if-chain typo. P02: `n−1` vs total gifts and `m == 0`. P03: nested-loop uniqueness counts can reset dict values when revisiting a key.

**What did I learn today?**

Restate story problems as exact numeric conditions; use hash maps for counts; prefer total frequency + one ordered pass over fragile double loops.

---

## ⏱️ Time Spent

| Activity   | Time   |
| ---------- | ------ |
| Problem 01 | 45 min |
| Problem 02 | 55 min |
| Problem 03 | 50 min |
| **Total**  | **2h 30m** |
