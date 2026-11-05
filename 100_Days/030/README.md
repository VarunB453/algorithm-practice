<div align="center">

# 🧩 LeetCode 20 — Valid Parentheses

### A stack-based solution to keep every bracket in its proper place! ✨

![Language](https://img.shields.io/badge/Language-Python%203-3776AB?logo=python&logoColor=white)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-2EA44F)
![Topic](https://img.shields.io/badge/Topic-Stack-8A2BE2)
![Complexity](https://img.shields.io/badge/Optimal%20Time-O(n)-blue)

**Problem:** Given a string containing `()`, `{}`, and `[]`, determine whether the brackets are valid.

</div>

---

## 🎯 The Core Idea

A bracket string is valid only when:

1. Every opening bracket has a matching closing bracket.
2. Brackets close in the correct **last-in, first-out (LIFO)** order.
3. No closing bracket appears without its matching opening bracket.
4. No unmatched opening bracket remains at the end.

A **stack** is ideal because the most recently opened bracket must be the first one closed.

## 🐢 1. Brute-Force Approach

### Hint

Repeatedly remove adjacent matching pairs: `()`, `{}`, and `[]`.

If the string is valid, removing matching pairs eventually reduces it to an empty string. If no more pairs can be removed while characters remain, the string is invalid.

### Python 3 — Brute Force

```python
class Solution:
    def isValid(self, s: str) -> bool:
        while True:
            previous = s
            s = s.replace("()", "")
            s = s.replace("{}", "")
            s = s.replace("[]", "")

            # No pair was removed, so further progress is impossible.
            if s == previous:
                break

        return s == ""
```

### Complexity

- **Time:** `O(n²)` in the worst case. Each replacement can scan the string, and many passes may be required.
- **Space:** `O(n)` for the newly created strings.

This approach is easy to understand, but repeated string construction makes it less efficient.

---

## 🚀 2. Optimal Approach — Stack

### 💡 Hints & Tricks

- Store only **opening brackets** in the stack.
- Use a dictionary that maps each closing bracket to its expected opening bracket.
- When a closing bracket appears:
  - If the stack is empty, return `False`.
  - If the top of the stack is not the expected opening bracket, return `False`.
  - Otherwise, pop the matching opening bracket.
- At the end, the stack must be empty.

**Key trick:** The top of the stack represents the most recent unmatched opening bracket. This enforces correct nesting automatically.

### Python 3 — Optimal Solution

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return len(stack) == 0
```

### 🔍 How the Algorithm Works

Consider:

```text
s = "{[()]}"
```

| Character | Action | Stack (bottom → top) |
|---|---|---|
| `{` | Push | `{` |
| `[` | Push | `{ [` |
| `(` | Push | `{ [ (` |
| `)` | Match `(`, then pop | `{ [` |
| `]` | Match `[`, then pop | `{` |
| `}` | Match `{`, then pop | empty |

The input is valid because every closing bracket matches the most recent unmatched opening bracket, and the stack is empty at the end.

### 🎞️ Animated Stack Walkthrough

![Animated stack walkthrough](assets/valid-parentheses-stack.gif)

### Complexity Analysis

Let `n` be the length of the input string.

| Complexity | Cost | Explanation |
|---|---:|---|
| **Time** | `O(n)` | Each character is processed once; stack operations take `O(1)` time. |
| **Space** | `O(n)` | In the worst case, all characters are opening brackets and are stored in the stack. |

<badge>Optimal</badge> The stack solution achieves linear time and is the standard optimal approach for this problem.

---

## 🧪 Edge Cases to Remember

| Input | Output | Reason |
|---|---|---|
| `""` | `True` | Empty string has no unmatched brackets. |
| `"()"` | `True` | Correct pair. |
| `"()[]{}"` | `True` | All pairs are correctly closed. |
| `"(]"` | `False` | Bracket types do not match. |
| `"([)]"` | `False` | Brackets close in the wrong order. |
| `"((("` | `False` | Opening brackets remain. |
| `"]"` | `False` | No opening bracket exists to match it. |

## 🧠 Interview Takeaways

- Recognize **nested matching** as a strong signal for a stack.
- Remember the LIFO principle: last opened, first closed.
- Check for an empty stack before reading `stack[-1]`.
- Validate both the match at each closing bracket and the final empty-stack condition.
- The input constraints for this problem guarantee that the string contains only bracket characters. The implementation therefore treats every non-closing character as an opening bracket.

## 🏁 Final Comparison

| Approach | Time | Space | Notes |
|---|---:|---:|---|
| Brute force — repeated removal | `O(n²)` | `O(n)` | Simple, but repeatedly rebuilds strings. |
| Optimal — stack | `O(n)` | `O(n)` | One pass with constant-time stack operations. |

<div align="center">

### Keep calm and let the stack do the matching! 📚

**Pattern to remember:** Matching nested structures → **Stack (LIFO)**

</div>
