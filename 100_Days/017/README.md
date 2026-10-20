# 🌀 LeetCode 54: Spiral Matrix — Python 3

> **Pattern:** Matrix Traversal · **Difficulty:** Medium  
> **Goal:** Return every matrix element in clockwise spiral order. 🚀

---

## 📌 Problem intuition

Start at the top-left corner and move **right → down → left → up**. After completing each side, move that boundary inward. Continue until the boundaries cross.

### Example

**Input**
```python
matrix = [
    [1,  2,  3],
    [4,  5,  6],
    [7,  8,  9]
]
```

**Output**
```python
[1, 2, 3, 6, 9, 8, 7, 4, 5]
```

**Spiral path**

```text
→ → →
      ↓
↑  5  ↓
↑     ↓
← ← ←
```

The order is: `1 → 2 → 3 → 6 → 9 → 8 → 7 → 4 → 5`.

---

## 🐢 1. Brute-force approach

A straightforward strategy is to simulate movement cell by cell while tracking visited positions. At each step, try the next direction in clockwise order. If the next cell is outside the matrix or has already been visited, turn right.

```python
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        rows, cols = len(matrix), len(matrix[0])
        seen = [[False] * cols for _ in range(rows)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0
        r = c = 0
        res = []

        for _ in range(rows * cols):
            res.append(matrix[r][c])
            seen[r][c] = True

            nr = r + directions[direction][0]
            nc = c + directions[direction][1]

            if (nr < 0 or nr >= rows or nc < 0 or nc >= cols
                    or seen[nr][nc]):
                direction = (direction + 1) % 4
                nr = r + directions[direction][0]
                nc = c + directions[direction][1]

            r, c = nr, nc

        return res
```

### Complexity

- **Time:** `O(m × n)` — each cell is visited exactly once.
- **Auxiliary space:** `O(m × n)` — the `seen` matrix records visited cells.
- **Output space:** `O(m × n)` — the result list contains all elements.

This is easy to visualize, but the visited matrix is extra memory that can be avoided.

---

## 💡 2. Optimal approach: shrink the boundaries

Maintain four boundaries:

- `top`: first row not yet traversed
- `bottom`: last row not yet traversed
- `left`: first column not yet traversed
- `right`: last column not yet traversed

For each layer, traverse:

1. **Top row:** left → right, then increment `top`.
2. **Right column:** top → bottom, then decrement `right`.
3. **Bottom row:** right → left, only if `top <= bottom`; then decrement `bottom`.
4. **Left column:** bottom → top, only if `left <= right`; then increment `left`.

The two `if` checks prevent duplicate traversal when the remaining layer has only one row or one column.

### ✨ Optimal Python 3 solution

```python
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # 1. Traverse the top row: left -> right
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1

            # 2. Traverse the right column: top -> bottom
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1

            # 3. Traverse the bottom row: right -> left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1

            # 4. Traverse the left column: bottom -> top
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1

        return res
```

### ⏱️ Complexity analysis

Let `m` be the number of rows and `n` the number of columns.

| Metric | Complexity | Reason |
|---|---:|---|
| Time | **`O(m × n)`** | Every element is appended exactly once. |
| Auxiliary space | **`O(1)`** | Only four boundary variables and loop variables are used, excluding the output. |
| Output space | **`O(m × n)`** | The returned list stores all matrix elements. |

**Why is this optimal?** Any correct solution must inspect all `m × n` elements, giving a lower bound of `Ω(m × n)` time. This approach matches that bound and uses constant auxiliary space.

---

## 🎬 3. Boundary animation

Imagine peeling an onion, one rectangular layer at a time. Each pass removes the outer edge, then the next layer becomes the new boundary.

Example matrix:

```text
 1   2   3   4
 5   6   7   8
 9  10  11  12
13  14  15  16
```

### Frame 1 — collect the outer layer

```text
→  →  →  →
↑           ↓
↑           ↓
←  ←  ←  ←
```

Collected: `[1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5]`

Boundaries move inward: `top += 1`, `bottom -= 1`, `left += 1`, `right -= 1`.

### Frame 2 — collect the inner layer

```text
 1   2   3   4
 5  →→→   8
 9  ↑  ↓  12
13  14  15  16
```

Collected next: `[6, 7, 11, 10]`

### Final result 🎉

```python
[1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
```

> **Animation tip:** To animate this in a README viewer, replace each frame with a GIF or a sequence of images. The text frames above provide a lightweight, GitHub-friendly walkthrough without external assets.

---

## 🧠 Tips, tricks, and interview hints

- **Think in boundaries, not coordinates.** Four pointers describe the unvisited rectangle.
- **Shrink only after finishing a side.** Update `top` after the top row and `right` after the right column.
- **Guard the final two sides.** `if top <= bottom` and `if left <= right` avoid duplicates in single-row or single-column layers.
- **Watch Python's reverse range.** `range(right, left - 1, -1)` includes `left`; the stop value is exclusive.
- **Test edge cases.** Try a `1 × 1` matrix, a single row, a single column, a rectangular matrix, and an even-sized square.
- **Keep the loop condition inclusive.** `top <= bottom and left <= right` ensures the last remaining row or column is processed.

### Quick mental checklist

- [ ] Top row goes left to right.
- [ ] Right column goes top to bottom.
- [ ] Bottom row goes right to left, if it still exists.
- [ ] Left column goes bottom to top, if it still exists.
- [ ] Boundaries move inward after each traversal.

---

## 🏁 Takeaway

The visited-cell simulation is intuitive, but **boundary shrinking is the preferred solution**: it is linear in the number of elements, requires `O(1)` auxiliary space, and directly models the spiral layers.

Keep calm, shrink the boundaries, and let the matrix reveal its spiral! 🌀
