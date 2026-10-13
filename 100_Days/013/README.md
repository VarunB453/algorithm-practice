# LeetCode 329 — Longest Increasing Path in a Matrix

> **Python 3 • DFS • Memoization • Beginner Friendly 🚀🧩**

Welcome to **LeetCode 329**! Our mission is to find the **longest increasing path** inside a matrix. 🗺️📈

You can move in only four directions: ⬆️ Up, ⬇️ Down, ⬅️ Left, and ➡️ Right. Every move must go to a **strictly larger** number. No diagonals, no jumping over cells! 🚫↗️

The goal is to return the maximum number of cells visited in one such path. Let's climb those numbers! 🧗‍♀️🔢

---

## 🌟 Example

```text
Input:
matrix = [
  [9, 9, 4],
  [6, 6, 8],
  [2, 1, 1]
]

Output: 4
```

One longest increasing path is:

```text
1 → 2 → 6 → 9
```

We visit four cells, and every next value is larger than the previous one! 🎉

---

## 🎬 Little Animation

![Longest Increasing Path Animation](./329.gif)

The animation reference above expects a GIF named `329.gif` in the same folder. 🎞️

Imagine starting at a cell, exploring its larger neighbors, and following the longest route. With memoization, once we know the best path starting at a cell, we save that answer so we don't have to solve it again! 🧠💾

---

## 🐢 Brute-Force Solution

Start DFS from **every cell** and explore every strictly increasing path. 🔍 For each cell, check its four neighbors, move only to a larger value, and return the longest path found.

### Python 3

```python
from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            best = 1  # This cell itself is a path! 🌱

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < m and 0 <= nc < n
                        and matrix[nr][nc] > matrix[r][c]):
                    best = max(best, 1 + dfs(nr, nc))

            return best

        return max(
            dfs(r, c)
            for r in range(m)
            for c in range(n)
        )
```

### Complexity

- **Time:** Exponential in the worst case ⏳ — path suffixes can be explored repeatedly from different starting paths.
- **Space:** `O(m × n)` worst-case recursion depth for a path that visits many cells. 💾

This explores valid paths correctly, but it repeats work. Let's teach DFS to remember! 🧠

---

## 💡 Optimization Tips, Tricks & Hints

### Hint 1 — Ask a smaller question! 🧩

Instead of asking, "What's the longest path in the whole matrix?", ask:

> **What is the longest increasing path that starts at cell `(r, c)`?** 🎯

That is exactly what `dfs(r, c)` returns.

### Hint 2 — Only climb uphill! ⛰️

A move is allowed only when:

```python
matrix[nr][nc] > matrix[r][c]
```

Every move goes to a strictly larger value, so a path cannot loop back to an earlier value. 📈

### Hint 3 — Save answers with memoization! 💾

If we already calculated the longest path starting from `(r, c)`, why calculate it again? Use `@lru_cache(None)` to store one answer per cell.

```python
from functools import lru_cache

@lru_cache(None)
def dfs(r, c):
    # Compute and remember the best path starting here.
    ...
```

### Hint 4 — The answer can start ANYWHERE! 🗺️

The best path doesn't necessarily begin at the top-left corner. Run DFS from every cell, then take the maximum:

```python
max(
    dfs(r, c)
    for r in range(m)
    for c in range(n)
)
```

### 🪄 The Big Trick

This is **DFS + Memoization (Top-Down Dynamic Programming)**! 🧠✨

- **DFS** explores valid increasing moves.
- **Memoization** remembers the best answer for each cell.
- **Maximum over all cells** finds the global longest path.

Think of every cell as a trailhead. Once you've mapped the best trail from it, save the map! 🥾🗺️

---

## 🚀 Optimal Solution — DFS + Memoization

This solution follows your supplied Python approach:

```python
from typing import List
from functools import lru_cache

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        @lru_cache(None)
        def dfs(r, c):
            best = 1

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < m and 0 <= nc < n
                        and matrix[nr][nc] > matrix[r][c]):
                    best = max(best, 1 + dfs(nr, nc))

            return best

        return max(
            dfs(r, c)
            for r in range(m)
            for c in range(n)
        )
```

> 📝 LeetCode guarantees a non-empty matrix for this problem, so `matrix[0]` is valid under the problem constraints.

---

## 🔎 Dry Run

Consider:

```text
matrix = [
  [9, 9, 4],
  [6, 6, 8],
  [2, 1, 1]
]
```

One longest increasing path is:

```text
1 → 2 → 6 → 9
```

Follow the idea from the smaller values upward! 🌱

```text
1 → 2 → 6 → 9
            ↑
        no larger neighbor

Path length = 4 🎉
```

For each cell, `dfs(r, c)` calculates the longest increasing path **starting from that cell**. For example, along this path:

```text
dfs(9) = 1
dfs(6) = 2   # 6 → 9
dfs(2) = 3   # 2 → 6 → 9
dfs(1) = 4   # 1 → 2 → 6 → 9
```

The answer is the maximum `dfs(r, c)` over all cells:

```text
Answer = 4 🏆
```

Memoization ensures each cell's result is computed once and then reused! 💾✨

---

## 🎨 DFS + Memoization Visualization

```text
                 Start at a cell
                       |
                       v
             Check 4 neighboring cells
                       |
                       v
        Is the neighbor strictly larger?
                /              \
              Yes               No
               |                 |
               v                 v
         Explore neighbor    Skip neighbor
               |
               v
      Keep the longest path length
               |
               v
        Cache result for cell
               |
               v
       Reuse it whenever needed!
```

The cache is like a notebook of completed trails: once a trailhead has a result, we don't need to rediscover it. 📒🧠

---

## ⚡ Why Is This Optimal?

Let `m` be the number of rows and `n` be the number of columns.

- Each cell's `dfs(r, c)` result is computed **once**. ✅
- Each cell checks at most four neighbors. ⬆️⬇️⬅️➡️
- Each neighbor check takes constant time. ⚡
- Every cell is considered as a possible starting point. 🗺️

That gives linear work in the number of cells! 🎉

---

## 📊 Complexity

| Approach | Time | Space |
|---|---:|---:|
| 🐢 Brute-force DFS | Exponential in the worst case | `O(m × n)` worst-case recursion depth |
| 🚀 DFS + Memoization | `O(m × n)` | `O(m × n)` |

### Why is the optimal time `O(m × n)`?

There are `m × n` cells. Each cell's result is calculated once, and each calculation checks only four directions:

```text
(m × n) cells × 4 neighbor checks
= O(m × n) ⚡
```

### Why is the optimal space `O(m × n)`?

The cache can store one result per cell, and the recursion stack can grow with the path length. Both are bounded by the number of cells. 💾

---

## 🧠 Pattern to Remember

This problem is a classic example of **DFS + Memoization**! 🧩🔥

Use this pattern when:
- A state can be revisited from different paths. 🔁
- The answer for a state depends on neighboring states. 🤝
- You need the longest or best path from a state. 🏆
- Recomputing the same state would waste time. ⏳

```text
DFS(cell)
  ├── Try every valid neighbor
  ├── Use the neighbor's cached answer
  ├── Keep the best path length
  └── Cache and return the answer
```

---

## 🪄 One-Line Mental Shortcut

> **Go only to larger neighbors, remember each cell's best path, and take the maximum over all cells!** 📈💾

- Strictly larger neighbor? ➡️ Explore!
- Already computed? 💾 Reuse!
- Finished every starting cell? 🏁 Take the maximum!

---

## 🏆 Final Takeaway

The winning combination is:

**DFS + Memoization = No Repeated Work!** 🧠⚡

Your key line is:

```python
best = max(best, 1 + dfs(nr, nc))
```

It means: "If I step to this larger neighbor, how long can my path become?" 📈

And this decorator:

```python
@lru_cache(None)
```

makes the solution efficient by remembering the answer for each cell. 💾✨

Keep climbing, keep caching, and keep smiling! 😄🐍💻

**Happy Coding! 🎉🚀❤️**
