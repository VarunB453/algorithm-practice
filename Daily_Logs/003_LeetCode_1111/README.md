# LeetCode 1111 — Maximum Nesting Depth of Two Valid Parentheses Strings

> **Python 3 • Greedy / Bit Manipulation • Beginner Friendly 🚀**

The goal of **LeetCode 1111** is to split a **valid parentheses string** `seq` into **two disjoint subsequences** `A` and `B`, such that:

- Both `A` and `B` are **valid parentheses strings** ✅
- Every character goes to exactly **one** of them 🎯
- The **maximum nesting depth** of `A` and `B` is **minimized** 📉

For example:

```text
Input:  seq = "(()())"
Output: [1, 0, 0, 0, 0, 1]
Explanation: A = "(())" (depth 2), B = "()" (depth 1)
             max(depth(A), depth(B)) = 2 — perfectly balanced! 🎉
```

The key observation is wonderfully simple:

- Every `'('` **opens** one level: `depth += 1` ➕
- Every `')'` **closes** one level: `depth -= 1` ➖
- We assign each parenthesis to group `depth & 1` (even/odd) 🎨
- This **alternates** nesting levels between `A` and `B`, keeping both shallow! 🏊

## 🎬 Little Animation

![Animated Parentheses Split trace](./1111.gif)

The animation shows the `depth` going up ⬆️ and down ⬇️ as we scan the string, each parenthesis getting painted 🎨 group `0` (blue) or `1` (red) based on `depth & 1`. Watch how deep nests get **split** between the two groups like a zipper! 🤐

---

## 🐢 Brute-Force Solution

A straightforward brute-force idea is:

Try **every possible assignment** of parentheses to `A` or `B`, check if both are valid, and track the minimum maximum depth.

### Python 3

```python
from itertools import product

class Solution:
    def maxDepthAfterSplit(self, seq):
        n = len(seq)
        best = float('inf')
        best_assign = None

        def depth_of(s):
            d = 0
            max_d = 0
            for ch in s:
                if ch == '(':
                    d += 1
                    max_d = max(max_d, d)
                else:
                    d -= 1
            return max_d

        def is_valid(s):
            balance = 0
            for ch in s:
                if ch == '(':
                    balance += 1
                else:
                    balance -= 1
                if balance < 0:
                    return False
            return balance == 0

        # Try all 2^n assignments
        for mask in product([0, 1], repeat=n):
            a = [seq[i] for i in range(n) if mask[i] == 0]
            b = [seq[i] for i in range(n) if mask[i] == 1]
            if is_valid(a) and is_valid(b):
                curr = max(depth_of(a), depth_of(b))
                if curr < best:
                    best = curr
                    best_assign = list(mask)

        return best_assign
```

### Complexity

- **Time:** `O(2^n * n)` ⏳ — we try all `2^n` subsets and validate each in `O(n)`.
- **Space:** `O(n)` 💾 — temporary strings for validation.

This works, but it **explodes exponentially** 💥 as the string grows. There must be a smarter way to split those parentheses!

---

## 💡 Optimization Tips, Tricks & Hints

### Hint 1 — Track depth, not the whole string 🧮

You don't need to build `A` and `B` at every step. Just keep a running `depth` — the **current nesting level** is all you need to decide the group!

### Hint 2 — Alternate by depth parity 🎨

The **magic formula**: assign each parenthesis to group `depth & 1`.

- Odd depth → group `1` 🔴
- Even depth → group `0` 🔵

This **zippers** deep nesting levels between the two groups! 🤐

```python
ans.append(depth & 1)   # ✅ 0 or 1, alternating like a zipper
```

### Hint 3 — Order matters for `(` vs `)` ⚠️

- For `'('`: **increment first**, then assign (we're entering a new level)
- For `')'`: **assign first**, then decrement (we're leaving the current level)

This keeps **matching pairs together** in the same group! 🤝

### Trick 🪄

Think of `depth` as an **elevator floor number** 🛗:

```text
'('  -> 🔼 going UP one floor
')'  -> 🔽 going DOWN one floor
depth & 1 -> 🎨 paint the floor red or blue
Matching floors get the same color — no broken pairs!
```

### Bonus Trick — One-liner magic ✨

```python
class Solution:
    def maxDepthAfterSplit(self, seq):
        ans, d = [], 0
        for c in seq:
            d += 1 if c == '(' else -1
            ans.append(d & 1 if c == '(' else (d + 1) & 1)
        return ans
```

---

## 🚀 Optimal Solution (Greedy + Bit Manipulation)

The optimal solution makes **one pass** through the string — each character is assigned in `O(1)` time!

```python
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = []
        depth = 0

        for ch in seq:
            if ch == '(':
                depth += 1
                ans.append(depth & 1)
            else:
                ans.append(depth & 1)
                depth -= 1

        return ans
```

### Why this is optimal

Each parenthesis is assigned to group `depth & 1` — the **parity of its nesting level**. Since `A` gets even levels and `B` gets odd levels (or vice versa), **no group gets two consecutive nesting levels**. The maximum depth is split as evenly as possible! ⚖️

The algorithm maintains:

- `depth` → the current nesting level, updated as we scan ➕➖
- `ans` → the group assignment (`0` or `1`) for each position 🎨

We need no memo or recursion — just **one elegant loop**! 🎯

---

## 🔎 Dry Run

For:

```text
seq = "(()())"
```

The trace produces:

```text
index 0: '(' → depth = 1, ans = [1]           🔴 level 1
index 1: '(' → depth = 2, ans = [1, 0]        🔵 level 2
index 2: ')' → ans = [1, 0, 0], depth = 1     🔵 matches its '('
index 3: '(' → depth = 2, ans = [1, 0, 0, 0]  🔵 level 2 again
index 4: ')' → ans = [1, 0, 0, 0, 0], depth = 1 🔵
index 5: ')' → ans = [1, 0, 0, 0, 0, 1], depth = 0 🔴 matches its '('

A (group 0) = "(())" → depth 2 ✅
B (group 1) = "()"     → depth 1 ✅
max(2, 1) = 2 — optimal! 🏆
```

For a deeper string like:

```text
seq = "((()))"
```

The split works like magic:

```text
index 0: '(' → depth 1 → 1 🔴
index 1: '(' → depth 2 → 0 🔵
index 2: '(' → depth 3 → 1 🔴
index 3: ')' → depth 2 → 0 🔵
index 4: ')' → depth 1 → 1 🔴
index 5: ')' → depth 0 → 0 🔵

A (group 0) = "(())" → depth 2 ✅
B (group 1) = "(())" → depth 2 ✅
max(2, 2) = 2 — perfectly balanced, as all things should be! ⚖️
```

Notice how the **deepest level** (level 3) went to group `1`, while levels 1 and 2 were **shared** between both groups — like a zipper distributing the load! 🤐

---

## 📊 Complexity

| Approach | Time | Space |
|---|---:|---:|
| 🐢 Brute force | `O(2^n * n)` | `O(n)` |
| 🚀 Greedy + Bit Manipulation | `O(n)` | `O(n)` |

### Final takeaway

> **Track the depth, alternate by parity, and let the zipper do the splitting.** ✨

This is a classic example of finding a **mathematical pattern** 🧮 instead of brute-force searching — one pass, constant work per character, beautiful result!

---

## 🧠 Pattern to Remember

This problem is a great introduction to the **Greedy with Parity** pattern:

```python
def maxDepthAfterSplit(seq):
    ans, depth = [], 0
    for ch in seq:
        if ch == '(':
            depth += 1
            ans.append(depth & 1)
        else:
            ans.append(depth & 1)
            depth -= 1
    return ans
```

The same mental model appears in many problems involving:

- Splitting sequences into balanced groups ⚖️
- Round-robin / alternating assignments 🎡
- Bit manipulation for parity checks 🔢
- Greedy algorithms with mathematical invariants 🧮
- Load balancing and resource distribution 📦

Happy coding! 🐍💻🎉
