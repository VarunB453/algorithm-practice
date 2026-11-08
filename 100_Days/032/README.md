# 🚀 LeetCode 150 — Evaluate Reverse Polish Notation

> **Problem:** [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)  
> **Language:** Python 3  
> **Topic:** Stack · Array · Math  
> **Difficulty:** Medium

---

## 🎯 Problem Overview

Evaluate an arithmetic expression written in **Reverse Polish Notation (RPN)** and return its integer result.

In RPN, operators come **after** their operands.

For example:

```text
["2", "1", "+", "3", "*"]
```

represents:

```text
(2 + 1) * 3 = 9
```

The valid operators are `+`, `-`, `*`, and `/`. Division must **truncate toward zero** (not round down).

---

## 🧠 Key Observation

An operator always applies to the **two most recently encountered values** that have not yet been used.

That is exactly the behaviour of a **stack**:

1. Push numbers onto the stack.
2. When an operator appears, pop the right operand first, then the left operand.
3. Apply the operation and push the result back.
4. The final stack element is the answer.

⚠️ **Operand order matters!** If the stack contains `[..., a, b]`, then subtraction is `a - b`, and division is `a / b`—not the reverse.

---

## 🐢 Approach 1: Brute Force — Repeated Expression Reduction

### 💡 Idea

Repeatedly scan the token list until an operator is found. Its two preceding values are the operands. Evaluate that small expression, replace the three tokens with the result, and repeat until one value remains.

For example:

```text
["2", "1", "+", "3", "*"]
             ↓
["3", "3", "*"]
       ↓
["9"]
```

### Python 3

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tokens = tokens[:]

        while len(tokens) > 1:
            for i, token in enumerate(tokens):
                if token in {"+", "-", "*", "/"}:
                    a = int(tokens[i - 2])
                    b = int(tokens[i - 1])

                    if token == "+":
                        result = a + b
                    elif token == "-":
                        result = a - b
                    elif token == "*":
                        result = a * b
                    else:
                        result = self.divide(a, b)

                    tokens[i - 2:i + 1] = [str(result)]
                    break

        return int(tokens[0])

    def divide(self, a: int, b: int) -> int:
        quotient = abs(a) // abs(b)
        return -quotient if (a < 0) != (b < 0) else quotient
```

### Complexity

- **Time:** \(O(n^2)\) in the worst case. Repeated scanning and list slicing/replacement can each take linear time, and there can be \(O(n)\) reductions.
- **Auxiliary space:** \(O(n)\) for the copied and repeatedly reduced token list.

This approach is useful for understanding how RPN expressions can be reduced, but repeated list modifications make it inefficient.

---

## ⚡ Approach 2: Optimal — Stack

<badge>Recommended approach</badge>

### 💡 Intuition

Each token is processed exactly once. Numbers are stored until an operator needs them. The operator consumes the top two values and pushes their result.

### 🔍 Step-by-Step Example

Input:

```text
tokens = ["2", "1", "+", "3", "*"]
```

The stack evolves as follows:

| Token | Action | Stack |
|---|---|---|
| `"2"` | Push `2` | `[2]` |
| `"1"` | Push `1` | `[2, 1]` |
| `"+"` | Pop `1`, pop `2`; push `2 + 1` | `[3]` |
| `"3"` | Push `3` | `[3, 3]` |
| `"*"` | Pop `3`, pop `3`; push `3 * 3` | `[9]` |

<details>
<summary>🎞️ Stack animation — follow the values</summary>

```text
Start       []

Read 2      [2]
             ↑ push

Read 1      [2, 1]
                ↑ push

Read +      [2, 1]  → pop b = 1, pop a = 2
             2 + 1 = 3
            [3]

Read 3      [3, 3]
                ↑ push

Read *      [3, 3]  → pop b = 3, pop a = 3
             3 * 3 = 9
            [9]

Result      9 🎉
```

</details>

### ✅ Optimal Python 3 Solution

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
                continue

            b = stack.pop()  # Right operand
            a = stack.pop()  # Left operand

            if token == "+":
                result = a + b
            elif token == "-":
                result = a - b
            elif token == "*":
                result = a * b
            else:
                # Truncate division toward zero without using float.
                quotient = abs(a) // abs(b)
                result = -quotient if (a < 0) != (b < 0) else quotient

            stack.append(result)

        return stack[-1]
```

### ⏱️ Complexity Analysis

Let \(n\) be the number of tokens.

| Complexity | Cost | Explanation |
|---|---:|---|
| **Time** | \(O(n)\) | Every token is visited once; each stack operation takes \(O(1)\). |
| **Auxiliary space** | \(O(n)\) | In the worst case, the stack stores a linear number of operands. |

---

## 💎 Tips, Tricks & Interview Notes

1. **Use a stack:** RPN is naturally evaluated in last-in, first-out order.
2. **Pop in the correct order:** The first pop is `b` (right operand); the second is `a` (left operand).
3. **Do not use floor division (`//`) directly for negative results:** Python rounds floor division toward negative infinity, while this problem requires truncation toward zero.
4. **Avoid floating-point division when possible:** `abs(a) // abs(b)` followed by sign correction gives truncation toward zero without float precision concerns.
5. **The final answer is the stack's only remaining value:** A valid RPN expression reduces to one result.

### ⚠️ Common Mistakes

| Mistake | Why it fails | Correct approach |
|---|---|---|
| Computing `b - a` | Reverses subtraction operands | Compute `a - b` |
| Computing `b / a` | Reverses division operands | Compute `a / b` |
| Using `a // b` | Negative division rounds down | Use absolute division and restore the sign |
| Popping only one operand | Every binary operator needs two operands | Pop `b`, then `a` |

---

## 🧪 Quick Dry Run: Negative Division

```text
tokens = ["-7", "3", "/"]
```

```text
Push -7       [-7]
Push 3        [-7, 3]
Read /        pop b = 3, pop a = -7
              -7 / 3 = -2  (truncate toward zero)
Final stack   [-2]
```

The result is `-2`, not `-3`.

---

## 🏁 Final Takeaway

The **stack-based solution** is optimal: it evaluates the expression in one pass with linear time complexity and linear auxiliary space.

**Remember:** Push operands, pop `b` then `a`, evaluate `a operator b`, and push the result. Happy coding! 🌟
