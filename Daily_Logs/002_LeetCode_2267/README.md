# LeetCode 2267 — Check if There Is a Valid Parentheses String Path

> **Python 3 • DFS + Memoization • Beginner Friendly 🚀**

The goal of **LeetCode 2267** is to find out if there is a **valid parentheses path** from the **top-left** cell `(0, 0)` to the **bottom-right** cell `(m - 1, n - 1)` of a grid, moving only **right** or **down**.

For example:

```text
Input:  grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]
Output: true
Explanation: One valid path is (0,0) → (0,1) → (1,1) → (2,1) → (3,1) → (3,2)
             The string along the path is "((()))" — perfectly balanced! 🎉
```

The key observation is wonderfully simple:

- Every `'('` **opens** one bracket: `balance += 1` ➕
- Every `')'` **closes** one bracket: `balance -= 1` ➖
- A path is valid only if `balance` **never goes negative** 🚫 and ends at exactly **0** at the destination 🏁
- We only move **down** or **right**, so we can **DFS** with a `balance` tracker and **memoize** states we've already explored 🗺️

---

## 🐢 Brute-Force Solution

A straightforward brute-force idea is:

Try **every possible right/down path** and check if the parentheses string along it is valid.

### Python 3

```python
class Solution:
    def hasValidPath(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        def is_valid(chars):
            balance = 0
            for ch in chars:
                if ch == '(':
                    balance += 1
                else:
                    balance -= 1
                if balance < 0:
                    return False
            return balance == 0

        def search_path(row, col, path):
            path.append(grid[row][col])

            if row == rows - 1 and col == cols - 1:
                ok = is_valid(path)
                path.pop()
                return ok

            ok = False
            if row + 1 < rows:
                ok = search_path(row + 1, col, path)
            if not ok and col + 1 < cols:
                ok = search_path(row, col + 1, path)

            path.pop()
            return ok

        return search_path(0, 0, [])
```

### Complexity

- **Time:** `O(2^(m+n) * (m+n))` ⏳ — the number of right/down paths is exponential in the worst case.
- **Space:** `O(m + n)` 💾 — the recursion depth plus the current path.

This works, but it keeps re-walking the same `(row, col, balance)` situations over and over. That repeated exploration is the clue that **memoization** can help!

---

## 💡 Optimization Tips, Tricks & Hints

### Hint 1 — Track balance, not the whole string

You don't need to rebuild the parentheses string at every step. Just keep a running `balance` — it's all you need to know if the path stays valid! 🧮

### Hint 2 — Prune impossible states early 🌿

If `balance < 0`, the path is already broken — **stop immediately**! No need to keep exploring that branch. 🛑

```python
if balance < 0:
    return False   # ✅ prune right away
```

### Hint 3 — Memoize the state (row, col, balance)

The same cell can be reached with the same balance many times. If it didn't work before, it won't work now — **cache it!** 🗂️

```python
state = (row, col, balance)
if state in memo:
    return memo[state]
```

### Trick 🪄

Think of `balance` as your **emotional stability meter** 💗:

```text
'('  -> 😊 you gain confidence (+1)
')'  -> 😟 you lose a little (-1)
balance < 0 -> 😭 too much negativity — abort!
balance == 0 at the end -> 😌 perfectly balanced, as all things should be
```

### Bonus Trick — Quick rejections ⚡

Before DFS even starts, toss out obviously impossible grids:

```python
if grid[0][0] == ')' or grid[rows - 1][cols - 1] == '(':
    return False

if (rows + cols - 1) % 2 != 0:
    return False
```

A valid path needs an **even** number of cells (equal `(` and `)`) and must **start with `(`** and **end with `)`**! 🎯

---

## 🚀 Optimal Solution (DFS + Memoization)

The optimal solution explores each **state** at most once.

```python
class Solution:
    def hasValidPath(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        if grid[0][0] == ')' or grid[rows - 1][cols - 1] == '(':
            return False

        if (rows + cols - 1) % 2 != 0:
            return False

        memo = {}

        def search_path(row, col, balance):
            if grid[row][col] == '(':
                balance += 1
            else:
                balance -= 1

            if balance < 0:
                return False

            if row == rows - 1 and col == cols - 1:
                return balance == 0

            state = (row, col, balance)

            if state in memo:
                return memo[state]

            valid_path = False

            if row + 1 < rows:
                valid_path = search_path(row + 1, col, balance)

            if not valid_path and col + 1 < cols:
                valid_path = search_path(row, col + 1, balance)

            memo[state] = valid_path
            return valid_path

        return search_path(0, 0, 0)
```

### Why this is optimal

Each state `(row, col, balance)` is computed **once** and cached — no redundant re-exploration! The `balance` is bounded by the path length, so the state space is manageable.

The algorithm maintains:

- `memo` → maps `(row, col, balance)` to whether a valid path exists from there 🗺️
- `balance` → the running parentheses score, updated as we move ➕➖

We need the memo because the same cell can be reached with the same balance via different routes — and the answer from that point on is always the same.

---

## 🔎 Dry Run

For:

```text
grid = [["(", "("],
        [")", ")"]]
```

The trace produces:

```text
Start at (0,0): char='(' → balance = 1, seen = {(0,0,1)}
Move down to (1,0): char=')' → balance = 0, seen = {(0,0,1), (1,0,0)}
Move right to (1,1): char=')' → balance = -1 → ❌ prune!
Backtrack to (0,0), move right to (0,1): char='(' → balance = 2
Move down to (1,1): char=')' → balance = 1 → at destination but balance ≠ 0 → ❌
No valid path exists → return False 😢
```

For a grid like:

```text
grid = [["(", "(", ")"],
        [")", "(", ")"]]
```

A golden path emerges:

```text
(0,0) '(' → (0,1) '(' → (0,2) ')' → (1,2) ')'
balance: 1 → 2 → 1 → 0  ✅ Valid path found! 🎉
```

Notice how memoization **skips re-exploring** states we've already seen — the search gets faster and faster as it goes! ⚡

---

## 📊 Complexity

| Approach | Time | Space |
|---|---:|---:|
| 🐢 Brute force | `O(2^(m+n) * (m+n))` | `O(m + n)` |
| 🚀 DFS + Memoization | `O(m * n * (m+n))` | `O(m * n * (m+n))` |

### Final takeaway

> **Track the balance, prune the negatives, and let memoization remember the rest.** ✨

This is a classic example of trading a little extra memory 💾 for a huge speed-up ⏩ — memoization turns "explore everything again" into "look it up instantly."

---

## 🧠 Pattern to Remember

This problem is a great introduction to the **DFS + Memoization on Grids** pattern:

```python
def search_path(row, col, balance):
    # update state
    # prune invalid
    # check memo
    # explore neighbors
    # cache result
```

The same mental model appears in many problems involving:

- Unique paths with constraints (obstacles, valid sequences)
- Minimum path sum with extra state
- Word search on grids
- Knight's tour and chessboard DP
- Any grid traversal where the "history" matters (balance, count, last move)

Happy coding! 🐍💻🎉
