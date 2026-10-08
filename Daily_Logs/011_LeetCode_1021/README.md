# 🎯 LeetCode 1021 — Remove Outermost Parentheses

### 🐍 Python 3 | Stack / Balance Tracking | Easy 💚

> 🌟 **Goal:** Remove the outermost pair of parentheses from every primitive parentheses group while keeping all inner parentheses intact!

---

# 📖 Problem Overview

A valid parentheses string can be split into **primitive valid parentheses strings**.

For every primitive group:

```text
(()()) → ()()
(()(())) → ()(())
```

We need to remove the **outermost `(` and `)`** from each primitive group.

### 🧠 Example

```text
Input:  "(()())(())"

Primitive groups:
"(()())" + "(())"

After removing outermost parentheses:
"()()" + "()"

Output:
"()()()"
```

---

# 🔎 Key Observation

The most important idea is to track the **parentheses balance**.

```text
'(' → balance + 1
')' → balance - 1
```

### 🎯 What does `balance` tell us?

| Balance | Meaning |
|---:|---|
| `0` | Outside a primitive group |
| `1` | We just entered / are at the outer layer |
| `> 1` | We are inside the primitive → KEEP `(` |
| `> 0` after `)` | We are still inside → KEEP `)` |

💡 **Golden Rule:**

> 🚫 Skip a `(` when balance goes `0 → 1`  
> 🚫 Skip a `)` when balance goes `1 → 0`  
> ✅ Keep everything else!

---

# 🐢 Brute-Force Solution

### 💭 Idea

A straightforward approach is:

1. Find every primitive parentheses group.
2. Remove its first `(`.
3. Remove its last `)`.
4. Join all remaining pieces.

For example:

```text
(()())(())( )

Primitive:
(()()) → ()()
(())   → ()

Result:
()()()
```

We can use a stack/counter to identify primitive groups, extract them, and then slice away their outer characters.

### 🧩 Brute-Force Python

```python
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        start = 0
        balance = 0

        for i, ch in enumerate(s):
            if ch == '(':
                balance += 1
            else:
                balance -= 1

            # A primitive group ends here
            if balance == 0:
                primitive = s[start:i + 1]
                result.append(primitive[1:-1])
                start = i + 1

        return ''.join(result)
```

### ⏱ Complexity

```text
Time  : O(n)
Space : O(n)
```

Although this is already linear, it does extra work by creating/slicing each primitive substring.

---

# 💡 Tips, Tricks & Hints

### 🪄 Hint #1

You don't actually need to store the primitive groups!

Ask yourself:

> **"When should I NOT append a parenthesis?"**

---

### 🪄 Hint #2

For `(`:

```python
balance += 1
```

If the new balance is `1`, this `(` is the **outermost opening parenthesis**.

👉 Skip it!

---

### 🪄 Hint #3

For `)`:

First decrease the balance:

```python
balance -= 1
```

If the new balance is `0`, this `)` is the **outermost closing parenthesis**.

👉 Skip it!

---

### 🪄 Hint #4

That means we never need to explicitly find primitive strings.

Just scan once:

```text
Character → Update balance → Decide whether to append
```

🚀 That's the trick!

---

# 🚀 Optimal Solution

The optimal approach uses **one pass + one balance counter**.

```python
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        balance = 0

        for ch in s:
            if ch == '(':
                balance += 1

                # Keep only non-outermost '('
                if balance > 1:
                    ans.append(ch)

            else:
                balance -= 1

                # Keep only non-outermost ')'
                if balance > 0:
                    ans.append(ch)

        return ''.join(ans)
```

---

# 🧠 Why Does It Work?

Let's walk through:

```text
s = "(()())"
```

### 🔍 Step-by-step

| Char | Balance | Action |
|:---:|---:|:---|
| `(` | 1 | ❌ Skip outer `(` |
| `(` | 2 | ✅ Keep |
| `)` | 1 | ✅ Keep |
| `(` | 2 | ✅ Keep |
| `)` | 1 | ✅ Keep |
| `)` | 0 | ❌ Skip outer `)` |

Result:

```text
()()
```

🎉 Exactly what we wanted!

---

# 🎬 Animated Walkthrough

### 🟢 Watch the balance move!

```text
Input:  ( ( ) ( ) )
        ↑

Balance:
0 → 1 → 2 → 1 → 2 → 1 → 0
      ↑                       ↑
    inner                   outer
    KEEP                    SKIP
```

### ✨ Visual Flow

```text
        ┌───────────────┐
        │   Read char   │
        └───────┬───────┘
                ↓
        ┌───────────────┐
        │ Update balance│
        └───────┬───────┘
                ↓
       ┌─────────────────┐
       │ Outer parenthesis?│
       └───────┬─────────┘
          YES  │  NO
           ↓   │   ↓
        ❌ Skip │ ✅ Append
               │
               ↓
          Next character
```

### 🎞️ Mini Animation

```text
Step 1   (         balance = 1    ❌
Step 2   ((        balance = 2    ✅
Step 3   (()       balance = 1    ✅
Step 4   (()(      balance = 2    ✅
Step 5   (()()     balance = 1    ✅
Step 6   (()())    balance = 0    ❌

Final →  "()()"
```

💃 **The balance counter dances between `0` and positive values!**

---

# 🏆 Optimal Complexity

Let `n = len(s)`.

### ⏱ Time Complexity

```text
O(n)
```

We visit every character exactly once.

### 💾 Space Complexity

```text
O(n)
```

The output itself can contain up to `n` characters.

> 💡 **Auxiliary space:** `O(1)` if the output list is not counted.

---

# 🧠 Interview Cheat Sheet

Remember these 3 lines:

```text
'(' → balance += 1
')' → balance -= 1
```

Then:

```text
balance == 1 after '(' → OUTERMOST → skip
balance == 0 after ')' → OUTERMOST → skip
otherwise → keep
```

🔥 **No stack required!**  
🔥 **No primitive substring required!**  
🔥 **One pass is enough!**

---

# ⚔️ Brute Force vs Optimal

| Approach | Idea | Time | Extra Space |
|---|---|---:|---:|
| 🐢 Brute Force | Extract primitives + slice | O(n) | O(n) |
| 🚀 Optimal | Track balance directly | O(n) | O(n)* |

`*` Output storage is required for the returned string.

---

# 🎯 Pattern to Remember

This problem teaches an important pattern:

## **Balance Tracking** ⚖️

Whenever a problem involves nested parentheses, think:

```text
Opening '('  → +1
Closing ')'  → -1
```

And ask:

> 🤔 **What does each balance level represent?**

Once you understand the levels, many parentheses problems become much easier! 🚀

---

# 🌈 Final Takeaway

The magic is not in removing strings.

The magic is in recognizing the **outermost depth**.

```text
        Outer layer
       ┌───────────┐
       │  (       )│  ← ❌ Remove
       │   Inner   │
       │  (     )  │  ← ✅ Keep
       └───────────┘
```

### 🥳 Remember:

> **Track the balance, skip depth 1, keep everything deeper!**

Keep practicing, keep solving, and keep that LeetCode streak alive! 🔥💻🚀

---

# ⭐ Happy Coding!

```text
     🧠 Think
       ↓
     💡 Observe
       ↓
     🧩 Simplify
       ↓
     🚀 Code
       ↓
     🏆 AC!
```

**LeetCode 1021 — Solved! 🎉**
