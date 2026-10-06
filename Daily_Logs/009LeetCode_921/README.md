# LeetCode 921 — Minimum Add to Make Parentheses Valid

> **Python 3 • Greedy / Balance Counter • Beginner Friendly • Perfectly Balanced! ⚖️🚀**

The goal of **LeetCode 921** is to find the **minimum number of parentheses** we need to add to make a string valid! 💯🎯

You are given a string `s` containing only `(` and `)`.

A string is **valid** if:

- Every opening `(` has a matching closing `)` 🤝
- Parentheses are properly **nested** 🪆
- The string is **balanced** ⚖️

Our mission is to calculate the **minimum additions** needed to make it valid! 🥳

---

## 🌟 Examples

For:

```text
Input:  s = "())"
Output: 1
```

Explanation:

```text
()) 
 ↑
We need one more ( at the beginning!

(()) → valid! 🎯
```

Add `(` at the beginning! 🎉

For:

```text
Input:  s = "((("
Output: 3
```

Explanation:

```text
(((
   ↑↑↑
We need three ) at the end!

((())) → valid! 🎊
```

For:

```text
Input:  s = "()"
Output: 0
```

Explanation:

```text
() is already valid! ✅
No additions needed! 🎉
```

For:

```text
Input:  s = "()))(("
Output: 4
```

Explanation:

```text
()))((
 ↑   ↑↑
Add ( here and )) there!

()()()() → valid! 🎊
```

---

## 🎬 Little Animation

![Minimum Add to Make Valid Animation](./921.gif)

The animation shows the **balance counter** going up and down as we scan the string! 📊🎬

Think of every `(` as saying:

> "I'm opening a door! Someone needs to close it!" 🚪😄

And every `)` as saying:

> "I'm closing a door! Hope someone opened it!" 🏃‍♂️💨

---

## 🐢 Brute-Force Solution

A natural brute-force idea is to repeatedly find and **remove valid pairs** `()`.

For example:

```text
()))((

First remove:
()

Then:
))((
```

Continue removing until no more `()` pairs exist. The remaining characters are the **unmatched** ones! 🔄

We can use a stack to simulate this process.

### Python 3

```python
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        for ch in s:
            if ch == '(':
                stack.append(ch)
            else:
                # Try to match with an opening parenthesis
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(ch)

        # Remaining items in stack are unmatched
        return len(stack)
```

### Complexity

- **Time:** `O(n)` ⏳ — we scan the string once!
- **Space:** `O(n)` 💾 — the stack can grow up to size `n` in the worst case.

This approach works, but we can do even better! 🚀

---

## 💡 Optimization Tips, Tricks & Hints

### Hint 1 — Think of Balance! ⚖️

Every `(` increases the balance by **1**.

Every `)` decreases the balance by **1**.

If balance goes **negative**, we have a problem! 🚨

---

### Hint 2 — What if we see `)` with no `(` before it? 🆘

Example:

```text
))
```

The first `)` has no matching `(`!

We **must** add one `(` before it.

So:

```text
additions += 1
```

🎯

---

### Hint 3 — What about leftover `(` at the end? 🏁

Example:

```text
(((
```

These opening parentheses never got closed!

We **must** add `)` for each one.

So:

```text
additions += balance
```

🎉

---

### Hint 4 — Do we really need a stack? 🤔

The stack only tells us **how many unmatched `(` exist**.

We can track this with a simple **counter**! 🔢

No stack needed! 🚫📚

---

### 🪄 The Big Trick

Use two variables:

```python
balance = 0      # Current unmatched opening parentheses
additions = 0    # Parentheses we need to add
```

When we see:

```text
(
```

increment `balance`.

When we see:

```text
)
```

- If `balance > 0`, decrement it (we found a match! 🤝)
- If `balance == 0`, increment `additions` (we need to add `(`! 🆘)

At the end, add `balance` to `additions` (close all unmatched `(`! 🏁)

---

## 🚀 Optimal Solution — Balance Counter

Here is the clean and optimal solution:

```python
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        additions = 0

        for ch in s:
            if ch == '(':
                balance += 1
            else:
                if balance > 0:
                    balance -= 1
                else:
                    additions += 1

        return additions + balance
```

---

## 🧠 How Does It Work?

Let's break the magic down! ✨

### Step 1 — Initialize two counters

```python
balance = 0
additions = 0
```

- `balance` tracks **unmatched opening** parentheses `(` 📈
- `additions` tracks **how many parentheses we need to add** ➕

---

### Step 2 — Opening `(`

When we see:

```python
if ch == '(':
    balance += 1
```

We have one more unmatched opening parenthesis.

```text
balance = 1 📈
```

🚪 Someone opened a door!

---

### Step 3 — Closing `)`

Now we try to match it:

```python
if balance > 0:
    balance -= 1
```

If there's an unmatched `(`, we pair them up! 🤝

```text
balance = 0 📉
```

But if `balance == 0`:

```python
else:
    additions += 1
```

We have a `)` with no matching `(`! We must add one! 🆘

---

### Step 4 — Final Answer

At the end:

```python
return additions + balance
```

- `additions` = parentheses we added for unmatched `)` ➕
- `balance` = unmatched `(` that need closing `)` ➕

Together, they give the **minimum additions**! 🎯

---

## 🔎 Dry Run

Let's trace:

```text
s = "()))(("
```

Start:

```text
balance = 0
additions = 0
```

### Character 1: `(`

```text
balance = 1
additions = 0
```

🚪 Door opened!

### Character 2: `)`

```text
balance = 0
additions = 0
```

🤝 Matched! Balance back to zero!

### Character 3: `)`

```text
balance = 0
additions = 1
```

🆘 No `(` to match! We need to add one!

### Character 4: `)`

```text
balance = 0
additions = 2
```

🆘 Another unmatched `)`! Add another `(`!

### Character 5: `(`

```text
balance = 1
additions = 2
```

🚪 Door opened!

### Character 6: `(`

```text
balance = 2
additions = 2
```

🚪 Another door opened!

### Final Answer

```text
additions + balance = 2 + 2 = 4 🎉
```

So:

```text
"()))((" → 4
```

We need to add `((` at the start and `))` at the end! 🎊

---

## 🎨 Balance Visualization

For:

```text
"()))(("
```

you can imagine the balance moving like this:

```text
Start       → balance: 0, additions: 0

(           → balance: 1, additions: 0  🚪

)           → balance: 0, additions: 0  🤝

)           → balance: 0, additions: 1  🆘

)           → balance: 0, additions: 2  🆘

(           → balance: 1, additions: 2  🚪

(           → balance: 2, additions: 2  🚪

Answer      → 2 + 2 = 4 🎉
```

The balance counter is basically keeping track of **how many doors are still open**! 🚪📊

---

## ⚡ Why This Is Optimal

The optimal solution processes every character **exactly once**.

For each character, we do only:

- Increment a counter ➕1
- Decrement a counter ➖1
- Compare with zero 🔍

Every operation is `O(1)`.

There is no stack. 🚫📚

There is no backtracking. 🚫🔙

Just one beautiful pass through the string! 🏃‍♂️💨

---

## 📊 Complexity

Let `n = len(s)`.

| Approach | Time | Space |
|---|---:|---:|
| 🐢 Stack | `O(n)` | `O(n)` |
| 🚀 Balance Counter | `O(n)` | `O(1)` |

### Why is the optimal space `O(1)`?

We only use **two integer variables**:

```python
balance = 0
additions = 0
```

No matter how long the string is, we only need **constant extra space**! 💾✨

---

## 🧩 Pattern to Remember

This problem is a fantastic example of the **Greedy / Balance Counter** pattern! ⚖️✨

Whenever a problem has:

- Matching pairs 🤝
- Opening and closing symbols 🔓🔒
- Need to track "how many unmatched" 🔢
- Minimum additions or removals ➕➖

Think:

> **BALANCE COUNTER! ⚖️🔥**

The mental model is:

```text
OPEN  → increment balance
CLOSE → if balance > 0, decrement
        else, we need to add an open
END   → add remaining balance to answer
```

---

## 🪄 One-Line Mental Shortcut

Remember this:

```text
(       → balance + 1 📈
)       → if balance > 0: balance - 1 📉
          else: additions + 1 🆘
END     → answer = additions + balance 🎯
```

And let the counter remember **how many doors are open**! 🚪🔢

---

## 🏆 Final Takeaway

> **Track the balance, count the mismatches, and add them up!** 🚀✨

The most important trick is recognizing that we don't need a stack—just a simple counter to track unmatched parentheses.

And the beautiful little logic:

```python
if balance > 0:
    balance -= 1
else:
    additions += 1
```

handles both:

```text
) with matching (  → pair them up 🤝
) without matching ( → add one ( 🆘
```

That's the whole magic! 🪄🎯

Keep practicing, keep counting, and keep smiling! 😄🐍💻

**Happy Coding! 🎉🚀❤️**
