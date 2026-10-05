# LeetCode 856 — Score of Parentheses

> **Python 3 • Stack • Beginner Friendly • Beautifully Balanced! ⚖️🚀**

The goal of **LeetCode 856** is to calculate the **score of a balanced parentheses string**! 💯🎯

You are given a balanced string `s` containing only `(` and `)`.

The scoring rules are:

- `()` has a score of **1** 🎯
- `AB` has a score of **A + B** ➕
- `(A)` has a score of **2 × A** ✖️2

Our mission is to calculate the total score of the entire parentheses string! 🥳

---

## 🌟 Examples

For:

```text
Input:  s = "()"
Output: 1
```

Explanation:

```text
() → 1 🎯
```

Simple and sweet! 🍬

For:

```text
Input:  s = "(())"
Output: 2
```

Explanation:

```text
(()) 
 ↑
 () = 1

Outer parentheses double the inside score:

2 × 1 = 2 🎉
```

For:

```text
Input:  s = "()()"
Output: 2
```

Explanation:

```text
() + ()
 1 + 1 = 2 🎊
```

For:

```text
Input:  s = "(()(()))"
Output: 6
```

The parentheses are nested and combined, so we need to carefully keep track of each level! 🧠✨

---

## 🎬 Little Animation

![Score of Parentheses Animation](./856.gif)

The animation shows the **stack levels** growing and shrinking as parentheses open and close! 📚🎬

Think of every `(` as saying:

> "Hey! We're entering a new room!" 🚪😄

And every `)` as saying:

> "Time to calculate this room's score and go back!" 🏃‍♂️💨

---

## 🐢 Brute-Force Solution

A natural brute-force idea is to repeatedly find the **innermost parentheses**.

For example:

```text
(()(()))

First find:
()

Then replace it with:
1

Continue simplifying until the whole string becomes a number! 🔄
```

We can use a recursive function that calculates the score of a substring.

### Python 3

```python
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        def score(left: int, right: int) -> int:
            total = 0
            i = left

            while i < right:
                if s[i] == '(':
                    depth = 1
                    j = i + 1

                    while depth:
                        if s[j] == '(':
                            depth += 1
                        else:
                            depth -= 1
                        j += 1

                    # Empty pair: ()
                    if j == i + 2:
                        total += 1
                    else:
                        # (A) -> 2 * score(A)
                        total += 2 * score(i + 1, j - 1)

                    i = j
                else:
                    i += 1

            return total

        return score(0, len(s))
```

### Complexity

- **Time:** `O(n²)` ⏳ — nested scanning and recursive processing can revisit characters!
- **Space:** `O(n)` 💾 — recursion depth can reach `n` in the worst case.

This approach works, but it does more work than necessary. 😅

We can do much better! 🚀

---

## 💡 Optimization Tips, Tricks & Hints

### Hint 1 — Think in Levels! 🪜

Every opening parenthesis `(` creates a **new level**.

Example:

```text
( ( ) )
↑ ↑
0 1
```

When we see `)`, we return to the previous level.

So... what data structure naturally remembers previous levels?

🥁🥁🥁

**A STACK! 📚🔥**

---

### Hint 2 — What happens when we see `()`? 🎯

The smallest valid parentheses unit is:

```text
()
```

Its score is:

```text
1
```

So when a closing `)` immediately closes an empty level, add `1`.

---

### Hint 3 — What happens when `(A)` closes? ✖️2

If the inside score is `A`:

```text
(A)
```

has score:

```text
2 × A
```

So when a closing parenthesis arrives, calculate the score inside that level.

---

### Hint 4 — Concatenation means addition! ➕

For:

```text
()()
```

we simply get:

```text
1 + 1 = 2
```

So each completed group contributes its score to the parent level.

---

### 🪄 The Big Trick

Use a stack where each element stores:

> **"What score have I collected at this parentheses level?"** 📚

Start with:

```python
stack = [0]
```

The first `0` represents the score outside all parentheses.

When we see:

```text
(
```

push a new `0`.

When we see:

```text
)
```

pop the inner score.

Then:

```text
inner = 0  →  score is 1
inner > 0  →  score is 2 × inner
```

Finally, add that score to the parent level! 🎯

---

## 🚀 Optimal Solution — Stack

Here is the clean and optimal solution:

```python
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                inner = stack.pop()
                stack[-1] += max(2 * inner, 1)

        return stack[0]
```

---

## 🧠 How Does It Work?

Let's break the magic down! ✨

### Step 1 — Start with a base level

```python
stack = [0]
```

Think of this as the score outside every pair:

```text
[ 0 ]
  ↑
base level
```

---

### Step 2 — Opening `(`

When we see:

```python
if ch == '(':
    stack.append(0)
```

we create a fresh score for the new nested level.

Example:

```text
(
```

Stack:

```text
[0, 0]
    ↑
 new level
```

🚪 We just entered a new room!

---

### Step 3 — Closing `)`

Now we finish the current level:

```python
inner = stack.pop()
```

Suppose:

```text
inner = 3
```

Then:

```text
(A) = 2 × A
```

so:

```text
2 × 3 = 6
```

We add it to the parent:

```python
stack[-1] += max(2 * inner, 1)
```

---

### Step 4 — Why `max(2 * inner, 1)`? 🤔

This tiny expression handles **both cases** beautifully!

#### Case 1 — `()`

The inner score is:

```text
inner = 0
```

Then:

```text
max(2 × 0, 1)
= max(0, 1)
= 1
```

Perfect! 🎯

#### Case 2 — `(A)`

If:

```text
inner = 3
```

then:

```text
max(2 × 3, 1)
= max(6, 1)
= 6
```

Exactly what we want! 🎉

One line handles both rules!

---

## 🔎 Dry Run

Let's trace:

```text
s = "(()())"
```

Start:

```text
stack = [0]
```

### Character 1: `(`

```text
stack = [0, 0]
```

🚪 Enter new level!

### Character 2: `(`

```text
stack = [0, 0, 0]
```

🚪 Another level!

### Character 3: `)`

Inner score:

```text
inner = 0
```

So:

```text
max(0, 1) = 1
```

Stack becomes:

```text
[0, 0, 1]
```

Actually, after popping the inner level:

```text
[0, 1]
```

🎯 We found `()`!

### Character 4: `(`

```text
[0, 1, 0]
```

🚪 New level!

### Character 5: `)`

Again:

```text
inner = 0
```

So we add:

```text
1
```

Stack:

```text
[0, 1, 1]
```

Then pop:

```text
[0, 2]
```

🎊 We have `() + () = 2` inside the outer parentheses!

### Character 6: `)`

Now:

```text
inner = 2
```

Therefore:

```text
2 × 2 = 4
```

Add to the base:

```text
[4]
```

Final answer:

```text
4 🎉
```

So:

```text
"(()())" → 4
```

---

## 🎨 Stack Visualization

For:

```text
(()())
```

you can imagine the stack moving like this:

```text
Start       → [0]

(           → [0, 0]

(           → [0, 0, 0]

)           → [0, 1]

(           → [0, 1, 0]

)           → [0, 2]

)           → [4]

Answer      → 4 🎉
```

The stack is basically keeping a **scoreboard for every nesting level**! 🏆📚

---

## ⚡ Why This Is Optimal

The optimal solution processes every character **exactly once**.

For each character, we do only:

- Push `0` 📥
- Pop a value 📤
- Multiply by `2` ✖️
- Add a value ➕
- Compare with `1` 🔍

Every operation is `O(1)`.

There is no backtracking. 🚫🔙

There is no repeated scanning. 🚫🔄

Just one beautiful pass through the string! 🏃‍♂️💨

---

## 📊 Complexity

Let `n = len(s)`.

| Approach | Time | Space |
|---|---:|---:|
| 🐢 Brute Force / Recursive | `O(n²)` | `O(n)` |
| 🚀 Stack | `O(n)` | `O(n)` |

### Why is the optimal space `O(n)`?

In the worst case:

```text
((((((...))))))
```

the stack can contain one entry for every open parenthesis.

So the maximum stack size is:

```text
O(n)
```

💾📚

---

## 🧩 Pattern to Remember

This problem is a fantastic example of the **Stack** pattern! 📚✨

Whenever a problem has:

- Nested structures 🪆
- Opening and closing symbols 🔓🔒
- "Go inside" and "come back out" behavior 🚪
- Need to remember previous levels 🧠

Think:

> **STACK! 📚🔥**

The mental model is:

```text
OPEN  → push a new level
CLOSE → calculate current level
        pop it
        add result to parent
```

---

## 🪄 One-Line Mental Shortcut

Remember this:

```text
()     → 1 🎯
(A)    → 2A ✖️2
AB     → A+B ➕
```

And let the stack remember **where you are**! 📚🧭

---

## 🏆 Final Takeaway

> **Open a level → calculate inside → close the level → send the score back up!** 🚀✨

The most important trick is recognizing that parentheses create **nested levels**, and a stack is perfect for remembering those levels.

And the beautiful little line:

```python
stack[-1] += max(2 * inner, 1)
```

handles both:

```text
()   → 1
(A)  → 2 × A
```

That's the whole magic! 🪄🎯

Keep practicing, keep stacking, and keep smiling! 😄🐍💻

**Happy Coding! 🎉🚀❤️**
