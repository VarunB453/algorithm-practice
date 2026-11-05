<div align="center">

# ⚾ LeetCode 682 — Baseball Game

### Decode the operations. Track the scores. Stack your way to the answer! 🚀

![LeetCode](https://img.shields.io/badge/LeetCode-682-orange?logo=leetcode)
![Language](https://img.shields.io/badge/Language-Python%203-blue?logo=python)
![Topic](https://img.shields.io/badge/Topic-Stack-purple)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen)

**A beginner-friendly walkthrough with hints, a brute-force baseline, an optimal solution, and a step-by-step animation.**

</div>

---

## 🧩 Problem Overview

You are given a list of strings, `operations`. Each string represents an operation in a baseball game. The valid operations are:

| Operation | Meaning |
|---|---|
| Integer such as `"5"` or `"-2"` | Record that score. |
| `"+"` | Record the sum of the previous two valid scores. |
| `"D"` | Record double the previous valid score. |
| `"C"` | Cancel (remove) the previous valid score. |

Return the sum of all scores remaining after processing every operation.

**Example**

```python
operations = ["5", "2", "C", "D", "+"]
```

Output:

```text
30
```

Explanation:
- `"5"` → record `5` → `[5]`
- `"2"` → record `2` → `[5, 2]`
- `"C"` → remove the last score → `[5]`
- `"D"` → double the last score (`5 × 2 = 10`) → `[5, 10]`
- `"+"` → add the last two scores (`5 + 10 = 15`) → `[5, 10, 15]`

Final total: `5 + 10 + 15 = 30` 🎯

---

## 💡 Hints Before Looking at the Solution

<details>
<summary>🔎 Hint 1 — What information must be retained?</summary>

Keep the valid scores in their original order. The next operation may need the most recent one or the most recent two.

</details>

<details>
<summary>🧠 Hint 2 — Which data structure fits?</summary>

A **stack** is ideal: append a new score, inspect the last one or two scores, and remove the latest score when `"C"` appears.

</details>

<details>
<summary>⚡ Hint 3 — How should each operation be handled?</summary>

- Integer: append `int(op)`.
- `"+"`: append `stack[-1] + stack[-2]`.
- `"D"`: append `2 * stack[-1]`.
- `"C"`: call `stack.pop()`.

</details>

---

## 🐢 Approach 1: Brute-Force Baseline

A straightforward baseline stores the score history in a list and processes each operation in sequence. Since the rules refer to the most recent scores, this approach still needs to track the current valid record. A more cumbersome alternative could repeatedly reconstruct or copy the history after changes, but that adds unnecessary work.

### Why avoid repeated copying?

If the list is copied after every operation, the extra copying can take **\(O(n^2)\)** time in the worst case. The problem does not require that work: Python lists already support efficient append and end removal.

### Brute-force-style implementation (with unnecessary copying)

```python
from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []

        for op in operations:
            # Unnecessary copy: included only to illustrate the baseline.
            current = scores[:]

            if op == "+":
                current.append(current[-1] + current[-2])
            elif op == "D":
                current.append(2 * current[-1])
            elif op == "C":
                current.pop()
            else:
                current.append(int(op))

            scores = current

        return sum(scores)
```

**Complexity**
- **Time:** \(O(n^2)\) worst case, because copying the growing list for each operation can cost \(1 + 2 + \cdots + n\).
- **Auxiliary space:** \(O(n)\) for the stored scores and copied list.

> ⚠️ This is intentionally inefficient for comparison. The copying is unnecessary; use the stack-based implementation below in practice.

---

## 🚀 Approach 2: Optimal Stack Solution

### Core idea

Maintain a stack containing only the scores that currently count. Each operation affects only the end of the stack, so there is no need to search through the history or rebuild it.

```python
from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                stack.append(2 * stack[-1])
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))

        return sum(stack)
```

### 🔍 Code walkthrough

| Code | Purpose |
|---|---|
| `stack = []` | Starts an empty history of valid scores. |
| `stack[-1] + stack[-2]` | Computes the sum of the two latest valid scores. |
| `2 * stack[-1]` | Doubles the latest valid score. |
| `stack.pop()` | Removes the latest valid score. |
| `stack.append(int(op))` | Converts a numeric string into an integer and records it. |
| `sum(stack)` | Returns the total of the remaining valid scores. |

### 🎬 Step-by-step animation

Follow the stack as each operation is processed. The stack shown is the list of currently valid scores.

<details open>
<summary>▶️ Frame 1 — Operation "5"</summary>

```text
Operation: "5"
Action:     Push 5

Stack:  [5]
Total:   5
```

</details>

<details>
<summary>▶️ Frame 2 — Operation "2"</summary>

```text
Operation: "2"
Action:     Push 2

Stack:  [5, 2]
Total:   7
```

</details>

<details>
<summary>▶️ Frame 3 — Operation "C"</summary>

```text
Operation: "C"
Action:     Remove the latest score (2)

Stack:  [5]
Total:   5
```

</details>

<details>
<summary>▶️ Frame 4 — Operation "D"</summary>

```text
Operation: "D"
Action:     Push 2 × 5 = 10

Stack:  [5, 10]
Total:   15
```

</details>

<details>
<summary>▶️ Frame 5 — Operation "+"</summary>

```text
Operation: "+"
Action:     Push 5 + 10 = 15

Stack:  [5, 10, 15]
Total:   30
```

</details>

**Final answer: `30`** 🏆

---

## ⏱️ Time and Space Complexity

Let \(n\) be the number of operations.

| Complexity | Result | Reason |
|---|---|---|
| **Time** | \(O(n)\) | Each operation is processed once; `append()` and end `pop()` are amortized \(O(1)\). The final `sum()` is \(O(n)\). |
| **Auxiliary space** | \(O(n)\) | In the worst case, every operation adds a score to the stack. |

The stack solution is optimal in asymptotic time because every operation must be examined at least once, giving a lower bound of \(\Omega(n)\).

---

## 🧠 Tips, Tricks, and Common Mistakes

- **Use `stack[-1]` for the latest score.** Python negative indexing makes stack operations concise.
- **Use `stack[-2]` for the second-latest score.** The problem guarantees that `"+"` has two valid scores available.
- **Do not subtract a cancelled score from a running total unless you manage every operation carefully.** Removing the score from the stack keeps the valid history correct.
- **Convert numeric operations with `int(op)`.** The input consists of strings, even when they represent integers.
- **Do not recompute the entire history after every operation.** Appending and popping from the end is sufficient.
- **Follow the operation order.** A score created by `"+"` or `"D"` becomes a valid score and may be used by later operations.

## 🧪 Edge Cases to Consider

| Case | Operations | Expected result |
|---|---|---:|
| One score | `["7"]` | `7` |
| Negative score | `["-3"]` | `-3` |
| Double a negative | `["-3", "D"]` | `-9` |
| Cancel the latest score | `["5", "2", "C"]` | `5` |
| Sum two prior scores | `["1", "2", "+"]` | `6` |

---

## 🏁 Final Takeaway

The important pattern is **stack + operation rules**:

1. Read each operation.
2. Modify the end of the stack according to its meaning.
3. Sum the remaining scores.

This gives a clean **\(O(n)\)-time, \(O(n)\)-space** solution. The stack directly represents the valid game history, making the code both efficient and easy to reason about. Keep practising—one operation at a time! 🎉

---

<div align="center">

**Happy Coding!** 💻⚾  
*Think clearly. Track state. Solve efficiently.*

</div>
