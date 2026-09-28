# 🥳 LeetCode 1614 — Maximum Nesting Depth of the Parentheses

> **Python 3 • Stack/Counter Thinking • Beginner Friendly 🚀**

The goal of **LeetCode 1614: Maximum Nesting Depth of the Parentheses** is to find the deepest level of nested parentheses in a valid parentheses string.

For example:

```text
Input:  "(1+(2*3)+((8)/4))+1"
Output: 3
```

The key observation is wonderfully simple:

- `(` means **go one level deeper** ⬆️
- `)` means **come back one level** ⬇️
- The largest depth ever reached is the answer 🏆

## 🎬 Little Animation

![Animated depth trace](./leetcode_1614_max_depth_animation.gif)

The animation shows the running `depth` and `maximum depth` while scanning the string from left to right.

---

## 🐢 Brute-Force Solution

A straightforward brute-force idea is:

For every position `i`, scan the prefix `s[0:i+1]` again and calculate its parenthesis balance.  
The maximum balance over all positions is the answer.

### Python 3

```python
class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0

        for i in range(len(s)):
            depth = 0

            for j in range(i + 1):
                if s[j] == '(':
                    depth += 1
                elif s[j] == ')':
                    depth -= 1

            ans = max(ans, depth)

        return ans
```

### Complexity

- **Time:** `O(n²)` ⏳ — each prefix is scanned again.
- **Space:** `O(1)` 💾 — only counters are used.

This works, but it performs the same counting work repeatedly. That is the clue that an optimization is possible.

---

## 💡 Optimization Tips, Tricks & Hints

### Hint 1 — Do not recompute old work

When scanning from left to right, the depth at position `i+1` differs from the depth at position `i` by only one step.

So keep the current depth in a variable.

### Hint 2 — Parentheses are enough

Characters such as digits, `+`, `-`, `*`, and `/` do not affect nesting depth.

Only these two symbols matter:

```text
'('  → depth += 1
')'  → depth -= 1
```

### Hint 3 — Track the best answer immediately

Whenever an opening parenthesis appears, update:

```python
ans = max(ans, depth)
```

There is no need to store the whole string, stack, or list.

### Trick 🪄

Think of `depth` as your **current floor in a building**:

```text
(     → 🏢 go upstairs
)     → 🏃 go downstairs
```

The answer is simply the **highest floor reached**.

---

## 🚀 Optimal Solution

The optimal solution scans the string exactly once.

```python
class Solution:
    def maxDepth(self, s: str) -> int:
        depth = ans = 0

        for ch in s:
            if ch == '(':
                depth += 1
                ans = max(ans, depth)
            elif ch == ')':
                depth -= 1

        return ans
```

### Why this is optimal

Each character is processed exactly once, so there is no repeated prefix scanning.

The algorithm maintains only two integers:

- `depth` → current nesting level
- `ans` → maximum nesting level seen so far

No auxiliary stack is required because the problem asks only for the **maximum depth**, not the matching positions of parentheses.

---

## 🔎 Dry Run

For:

```text
s = "(1+(2*3)+((8)/4))+1"
```

The important characters produce this depth trace:

```text
(  → depth = 1, ans = 1
(  → depth = 2, ans = 2
)  → depth = 1
(  → depth = 2
(  → depth = 3, ans = 3
)  → depth = 2
)  → depth = 1
)  → depth = 0
```

Therefore:

```text
Maximum depth = 3 🎯
```

---

## 📊 Complexity

| Approach | Time | Space |
|---|---:|---:|
| 🐢 Brute force | `O(n²)` | `O(1)` |
| 🚀 One-pass optimal | `O(n)` | `O(1)` |

### Final takeaway

> **Scan once, maintain the current balance, and remember the largest value.** ✨

This is a classic example of replacing repeated work with a simple running state.

---

## 🧠 Pattern to Remember

This problem is a great introduction to the **running counter / prefix balance** pattern:

```python
state += change
answer = max(answer, state)
```

The same mental model appears in many problems involving:

- Parentheses
- Prefix sums
- Running balances
- Nested structures
- Resource levels
- Increment/decrement simulations

Happy coding! 🐍💻🎉
