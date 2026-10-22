# 🔄 LeetCode 48 — Rotate Image (Python 3)

> 🎯 **Goal:** Rotate an `n × n` matrix 90° clockwise **in place**, without creating another matrix.

[![LeetCode](https://img.shields.io/badge/LeetCode-48-orange?logo=leetcode)](https://leetcode.com/problems/rotate-image/)
![Language](https://img.shields.io/badge/Language-Python%203-blue?logo=python)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

---

## 🧩 Problem Statement

Given an `n × n` matrix, rotate it **90 degrees clockwise**. Modify the matrix in place.

### Example

**Input**
```text
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
```

**Output**
```text
[
  [7, 4, 1],
  [8, 5, 2],
  [9, 6, 3]
]
```

---

## 🐢 Brute-Force Approach

### Idea

Create a new matrix and map each original cell `(row, col)` to its rotated position `(col, n - 1 - row)`.

```python
class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        rotated = [[0] * n for _ in range(n)]

        for row in range(n):
            for col in range(n):
                rotated[col][n - 1 - row] = matrix[row][col]

        # Copy the rotated values back into the original matrix.
        for row in range(n):
            for col in range(n):
                matrix[row][col] = rotated[row][col]
```

**Complexity**
- ⏱️ Time: **O(n²)** — every cell is visited a constant number of times.
- 💾 Auxiliary space: **O(n²)** — a second matrix is allocated.

**Why not ideal?** The result is correct, but the extra matrix violates the in-place space goal.

---

## 💡 Optimal Approach: Reverse Rows + Transpose

The supplied solution uses a neat two-step transformation:

1. **Reverse the order of the rows.** This flips the matrix vertically.
2. **Transpose the matrix.** Swap `matrix[i][j]` with `matrix[j][i]` for cells below the main diagonal.

These two operations together produce a 90° clockwise rotation. No second matrix is needed.

### ✅ Python 3 Solution

```python
class Solution:
    def rotate(self, matrix):
        matrix.reverse()

        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
```

### 🎞️ Animation / Step-by-Step Trace

Start with:

```text
1 2 3
4 5 6
7 8 9
```

**Step 1 — Reverse the rows** ⬇️

```text
7 8 9
4 5 6
1 2 3
```

**Step 2 — Transpose across the main diagonal** ↘️

Swap `(1, 0)` with `(0, 1)`, then `(2, 0)` with `(0, 2)`, then `(2, 1)` with `(1, 2)`.

```text
7 4 1
8 5 2
9 6 3
```

**🎉 Result:** The matrix is rotated 90° clockwise, in place!

### 🔍 Why does this work?

Reversing the rows moves the original bottom row to the top. Transposing then exchanges row and column positions. Algebraically, the combined mapping is:

`matrix[row][col] → matrix[col][n - 1 - row]`

That is exactly the coordinate mapping for a 90° clockwise rotation.

### 📊 Complexity Analysis

| Metric | Complexity | Explanation |
|---|---:|---|
| ⏱️ Time | **O(n²)** | Transposition performs a quadratic number of cell swaps; row reversal is at most O(n). |
| 💾 Auxiliary space | **O(1)** | The matrix is modified in place; only a constant amount of temporary storage is used for swapping. |

> Note: The input matrix itself is not counted as auxiliary space.

---

## 🧠 Tips, Tricks & Interview Hints

- 🪞 **Clockwise rotation:** Reverse the rows, then transpose.
- 🔁 **Counterclockwise rotation:** Transpose first, then reverse the rows.
- 📐 **Transpose safely:** Iterate only over `j < i`; this swaps each off-diagonal pair exactly once and avoids undoing swaps.
- 🚫 **Avoid a full second matrix** when the problem explicitly asks for an in-place operation.
- 🧪 **Test edge cases:** A `1 × 1` matrix, a `2 × 2` matrix, and matrices with distinct values make mistakes easier to spot.
- 🧩 **Remember the coordinate rule:** Clockwise rotation maps `(row, col)` to `(col, n - 1 - row)`.

---

## ⚖️ Approach Comparison

| Approach | Time | Auxiliary Space | In Place? |
|---|---:|---:|---|
| Brute force: build a new matrix | O(n²) | O(n²) | ❌ |
| Reverse rows + transpose | O(n²) | O(1) | ✅ |

## 🏁 Takeaway

The key insight is that a 90° clockwise rotation can be decomposed into **two simple operations: reverse the rows and transpose**. This preserves **O(n²)** time while reducing auxiliary space from **O(n²)** to **O(1)**. 🚀

---

**Problem:** [LeetCode 48 — Rotate Image](https://leetcode.com/problems/rotate-image/)  
**Language:** Python 3  
**Pattern:** Matrix · In-place transformation · Transposition
