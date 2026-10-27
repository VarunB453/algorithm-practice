# 🔢 LeetCode 36: Valid Sudoku — Python 3

> **Pattern:** Hash Sets · Matrix Traversal · **Difficulty:** Medium  
> **Goal:** Determine whether a partially filled 9 × 9 Sudoku board is valid. 🧩

---

## 🎯 Problem intuition

A Sudoku board is valid when every filled digit from `"1"` to `"9"` appears **at most once** in each:

- **Row** — all cells from left to right.
- **Column** — all cells from top to bottom.
- **3 × 3 box** — each of the nine smaller regions.

A dot (`"."`) represents an empty cell and must be ignored.

**Important:** The board does **not** need to be solvable. The task is only to check whether the currently filled cells violate Sudoku rules.

### Example

```text
board =
[
  ["5","3",".", ".", "7",".", ".", ".", "."],
  ["6",".",".", "1","9","5", ".", ".", "."],
  [".","9","8", ".", ".",".", ".", "6","."],

  ["8",".",".", ".", "6",".", ".", ".", "3"],
  ["4",".",".", "8",".","3", ".", ".", "1"],
  ["7",".",".", ".", "2",".", ".", ".", "6"],

  [".","6",".", ".", ".",".", "2","8","."],
  [".",".",".", "4","1","9", ".", ".","5"],
  [".",".",".", ".", "8",".", ".", "7","9"]
]
```

**Output**
```python
True
```

No filled digit is repeated in any row, column, or 3 × 3 box. ✅

---

## 🐢 1. Brute-force solution

### 💭 Idea

For every filled cell, scan the rest of its row, column, and 3 × 3 box to find duplicates. If a duplicate exists, return `False`; otherwise, continue.

```python
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == ".":
                    continue

                # Check the rest of this row.
                for k in range(9):
                    if k != c and board[r][k] == num:
                        return False

                # Check the rest of this column.
                for k in range(9):
                    if k != r and board[k][c] == num:
                        return False

                # Check this cell's 3 × 3 box.
                box_row = (r // 3) * 3
                box_col = (c // 3) * 3

                for br in range(box_row, box_row + 3):
                    for bc in range(box_col, box_col + 3):
                        if (br, bc) != (r, c) and board[br][bc] == num:
                            return False

        return True
```

### ⏱️ Complexity

Let \(N = 9\) be the board dimension.

- **Time:** \(O(N^3)\) — there are \(N^2\) cells, and each filled cell may scan \(O(N)\) row/column/box positions. The box scan is also bounded by a constant for a standard 9 × 9 board.
- **Auxiliary space:** \(O(1)\) — only a fixed number of variables are used.

**Trade-off:** This is straightforward, but it repeatedly checks the same cells. A set-based approach avoids those repeated scans.

---

## 💡 2. Optimal solution — track seen digits with sets

### 🧠 Key insight

As each filled cell is visited, record its digit in three places:

1. `rows[r]` — digits already seen in row `r`.
2. `cols[c]` — digits already seen in column `c`.
3. `boxes[box]` — digits already seen in its 3 × 3 box.

If the digit is already in **any** of those sets, a rule has been broken and the answer is `False`. Otherwise, add it to all three sets.

### ✨ Python 3 solution

```python
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == ".":
                    continue

                box = (r // 3) * 3 + (c // 3)

                if (num in rows[r] or
                    num in cols[c] or
                    num in boxes[box]):
                    return False

                rows[r].add(num)
                cols[c].add(num)
                boxes[box].add(num)

        return True
```

### 🔍 How is the box index calculated?

```python
box = (r // 3) * 3 + (c // 3)
```

Integer division groups row and column coordinates into 3-cell bands. The formula maps each cell to a box index from `0` through `8`.

```text
+---------+---------+---------+
|    0    |    1    |    2    |
+---------+---------+---------+
|    3    |    4    |    5    |
+---------+---------+---------+
|    6    |    7    |    8    |
+---------+---------+---------+
```

For example, cell `(r = 4, c = 7)` belongs to:

```python
box = (4 // 3) * 3 + (7 // 3)
#     1 * 3 + 2 = 5
```

Therefore, that cell belongs to box `5` (the middle row of boxes, rightmost box). 🎯

---

## 🎬 3. Animation — watch the sets fill up

Consider these cells as the board is scanned from left to right, top to bottom:

```text
5  3  . | .  7  . | .  .  .
6  .  . | 1  9  5 | .  .  .
.  9  8 | .  .  . | .  6  .
```

**Frame 1 — read `5` at `(0, 0)`**

```text
[5] 3  . | .  7  . | .  .  .
 6  .  . | 1  9  5 | .  .  .
 .  9  8 | .  .  . | .  6  .
```

`5` is new, so add it to `rows[0]`, `cols[0]`, and `boxes[0]`.

```text
rows[0]  = {5}
cols[0]  = {5}
boxes[0] = {5}
```

**Frame 2 — read `3` at `(0, 1)`**

`3` is not present in the relevant row, column, or box. Add it to all three.

```text
rows[0]  = {5, 3}
cols[1]  = {3}
boxes[0] = {5, 3}
```

**Frame 3 — read `6` at `(1, 0)`**

`6` is new in row `1`, column `0`, and box `0`, so it is valid.

```text
rows[1]  = {6}
cols[0]  = {5, 6}
boxes[0] = {5, 3, 6}
```

**Frame 4 — a duplicate appears**

Imagine the next cell in row `1` contained `5` instead of `.`. Since `5` is already in `cols[0]` only if it occupies column `0`; more generally, a duplicate is rejected when the digit is found in the current cell's own row, column, or box.

```python
if (num in rows[r] or
    num in cols[c] or
    num in boxes[box]):
    return False
```

The check happens **before** insertion, so the duplicate is detected immediately. No later cells need to be examined. 🚦

---

## 🧮 4. Complexity analysis

| Metric | Complexity | Explanation |
|---|---:|---|
| Time | **\(O(1)\)** for standard 9 × 9 Sudoku | Exactly 81 cells are considered at most once; set membership and insertion are \(O(1)\) on average. |
| Auxiliary space | **\(O(1)\)** for standard 9 × 9 Sudoku | The row, column, and box sets can hold only digits `1`–`9`. |
| Generalized \(N × N\) board | **\(O(N^2)\) time** | Every cell is processed once, with average \(O(1)\) set operations. |
| Generalized auxiliary space | **\(O(N^2)\)** | Across all row, column, and box sets, up to \(O(N^2)\) entries may be stored. |

For LeetCode's fixed 9 × 9 board, the solution is constant-time and constant-space in the strict asymptotic sense. For a generalized board size, the costs scale with the number of cells.

---

## 🏆 5. Tips, tricks, and interview hints

- **Skip empty cells first.** `if num == ".": continue` keeps empty cells out of every set.
- **Check before adding.** First test for duplicates; only then update the row, column, and box sets.
- **Use three separate set collections.** A digit can be legal in a row but invalid in its column or box, so all three constraints must be checked.
- **Memorize the box formula.** `(r // 3) * 3 + (c // 3)` maps any coordinate to a box ID from `0` to `8`.
- **Return early.** The first violation is enough to establish that the board is invalid.
- **Do not solve the puzzle.** Empty cells are allowed; only existing duplicate digits matter.
- **Remember the distinction between fixed and generalized sizes.** A 9 × 9 board has constant size, while an \(N × N\) generalization scales with \(N\).

### 🧠 Interview-ready summary

> “Traverse the board once. For each non-empty digit, calculate its 3 × 3 box index and check whether it already exists in the corresponding row, column, or box set. If it does, return `False`; otherwise, insert it into all three sets. If the scan finishes without a conflict, return `True`.”

---

## 🎉 Final takeaway

The brute-force approach repeatedly scans neighboring cells. The set-based solution remembers what has already appeared, turning duplicate detection into a simple membership check.

**Pattern to remember:** *One pass + three constraint trackers = clean Sudoku validation.* 🔥

Happy coding, and may every set stay duplicate-free! 🚀
