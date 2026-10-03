# LeetCode 32 — Longest Valid Parentheses

> **Python 3 • Stack • Beginner Friendly 🚀**

The goal of **LeetCode 32** is to find the **length of the longest valid (well-formed) parentheses substring** in a given string `s`! 💌

You are given a string `s` containing only the characters `'('` and `')'`. Your mission is to find the longest substring that forms a **valid** parentheses sequence — one where every opening bracket `(` has a matching closing bracket `)` in the right order! 🤝

A substring is **valid** if:

- Every `(` is matched by a `)` in the correct order 🥇
- Brackets are **properly nested** — no lonely orphans allowed! 🔄
- The sequence **starts with `(`** and **ends with `)`** ➕

For example:

```text
Input:  s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
             That lonely "(" at the start never finds its match! 😢
```

```text
Input:  s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
             The ")" at index 0 is a party crasher! 🚫
```

```text
Input:  s = ""
Output: 0
Explanation: Empty string, empty party! 🎈
```

```text
Input:  s = "()(())"
Output: 6
Explanation: The whole string is valid! Perfectly nested! 🎉
```

The key observation is wonderfully simple:

- Use a **stack** to keep track of unmatched `(` positions! 🎯
- Push `(` indices onto the stack — they're waiting for their soulmate `)`! 💍
- When a `)` arrives, pop the stack — a match is made! 💘
- The **secret weapon**: start with a sentinel `-1` on the stack to handle edge cases! 🛡️
- The length of the current valid substring is `current_index - stack[-1]`! 📏

## 🎬 Little Animation

![Animated Stack trace](./32.gif)

The animation shows the **stack** dancing through the string! 🕺💃 Watch how `(` gets pushed onto the stack waiting for love, and `)` pops it off when they finally meet! When the stack goes empty, a new sentinel `-1` jumps in to save the day! 🦸‍♂️

---

## 🐢 Brute-Force Solution

A straightforward brute-force idea is:

Check **every possible substring** and verify if it's a valid parentheses sequence! For each starting point, try every ending point, and use a counter to check validity! 🔍

### Python 3

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        ans = 0

        for i in range(n):
            for j in range(i, n):
                # Check if s[i:j+1] is valid! 🔍
                balance = 0
                is_valid = True

                for k in range(i, j + 1):
                    if s[k] == '(':
                        balance += 1
                    else:
                        balance -= 1

                    if balance < 0:  # 😱 More ')' than '(' — invalid!
                        is_valid = False
                        break

                if is_valid and balance == 0:
                    ans = max(ans, j - i + 1)

        return ans
```

### Complexity

- **Time:** `O(n³)` ⏳ — Three nested loops: `O(n²)` substrings, each taking `O(n)` to validate! For `n = 10⁵`, that's **way too slow**! 💥
- **Space:** `O(1)` 💾 — Just a counter (ignoring the input string)!

This works for tiny inputs, but it's **brutally slow** for large strings! 💥 We need something smarter! 🎯

---

## 💡 Optimization Tips, Tricks & Hints

### Hint 1 — The Stack is your best friend! 🧺

Think of the stack as a **waiting room** for lonely `(` brackets! When a `)` arrives, it matches with the most recent `(` (LIFO — Last In, First Out)! 💘

The stack stores **indices**, not characters — because we need to calculate **lengths**! 📏

### Hint 2 — The Sentinel `-1` is the secret sauce! 🛡️

Here's the golden rule:

- Start with `stack = [-1]` — this sentinel marks the **"virtual boundary"** before index 0! 🏁
- When `)` pops the last element (the stack becomes empty), push the **current index** as the new boundary! 🚧
- The length of the current valid substring is `i - stack[-1]`! 📐

**Why -1?** Because if a valid substring starts at index 0, we need something "before" it to calculate the length! The sentinel is like a starting line! 🏃‍♂️

### Hint 3 — When `)` meets an empty stack... 🆘

If the stack is empty when `)` arrives, that `)` is **unmatched**! It can't form a valid substring starting before it! Push its index as the new boundary! 🚫

### Trick 🪄

Think of it like a **dance party** 💃🕺:

```text
"(" enters the dance floor and waits for a partner! 💃
")" arrives and pairs with the most recent dancer! 🕺
They dance together and leave! 💃🕺
If ")" arrives but no one is waiting... 😢
...it becomes the new "wall" — no dancing past this point! 🚧
The distance from the wall to the current dancer is the party size! 🎉
```

### Bonus Trick — Two-Pass Counter! 🔄

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Left-to-right pass
        left = right = ans = 0
        for ch in s:
            if ch == '(':
                left += 1
            else:
                right += 1
            if left == right:
                ans = max(ans, 2 * right)
            elif right > left:
                left = right = 0

        # Right-to-left pass
        left = right = 0
        for ch in reversed(s):
            if ch == '(':
                left += 1
            else:
                right += 1
            if left == right:
                ans = max(ans, 2 * left)
            elif left > right:
                left = right = 0

        return ans
```

*(No extra space! But the stack solution is more intuitive! 😄)*

---

## 🚀 Optimal Solution (Stack)

The optimal solution makes **one pass** through the string — using a stack to track unmatched positions!

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # 🛡️ Sentinel — the virtual starting line!
        ans = 0       # 🎯 Longest valid substring found so far!

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)  # 💃 Push '(' index — waiting for a partner!
            else:
                stack.pop()      # 🕺 ')' found a partner — pop the match!

                if not stack:
                    stack.append(i)  # 🚧 Empty! This ')' is the new wall!
                else:
                    ans = max(ans, i - stack[-1])  # 📏 Calculate length!

        return ans
```

### Why this is optimal

Each character is processed **exactly once**:

- **Total iterations:** `n` — one single loop through the string! 📏
- **Each iteration:** One stack push or pop — all `O(1)`! ⚡
- **No waste:** Every character is visited exactly **once**! ✅

The stack strategy works because:

- The **sentinel `-1`** handles edge cases gracefully! 🛡️
- The stack always stores the **boundary** of the current valid region! 🚧
- `i - stack[-1]` gives the length of the longest valid substring **ending at `i`**! 📐
- It's a beautiful example of **stack + sentinel** working together! 🤝

We touch each character exactly once — that's the power of the **Stack**! 🎯✨

---

## 🔎 Dry Run

For:

```text
s = "(()())"
```

The trace produces:

```text
Start: stack = [-1], ans = 0

i=0, ch='(' → stack = [-1, 0] 💃
  "(" pushed — waiting for love!

i=1, ch='(' → stack = [-1, 0, 1] 💃💃
  Another "(" joins the party!

i=2, ch=')' → pop! stack = [-1, 0] 💘
  Match made! Length = 2 - 0 = 2
  ans = max(0, 2) = 2 ✅

i=3, ch='(' → stack = [-1, 0, 3] 💃
  New "(" enters!

i=4, ch=')' → pop! stack = [-1, 0] 💘
  Match made! Length = 4 - 0 = 4
  ans = max(2, 4) = 4 ✅

i=5, ch=')' → pop! stack = [-1] 💘
  Match made! Length = 5 - (-1) = 6
  ans = max(4, 6) = 6 ✅

Final answer: 6 🎉
The entire string is valid! 🏆
```

For a trickier case:

```text
s = ")()())"
```

```text
Start: stack = [-1], ans = 0

i=0, ch=')' → pop! stack = [] 😱
  Stack empty! Push i=0 as new boundary!
  stack = [0] 🚧

i=1, ch='(' → stack = [0, 1] 💃
  "(" pushed!

i=2, ch=')' → pop! stack = [0] 💘
  Match made! Length = 2 - 0 = 2
  ans = max(0, 2) = 2 ✅

i=3, ch='(' → stack = [0, 3] 💃
  "(" pushed!

i=4, ch=')' → pop! stack = [0] 💘
  Match made! Length = 4 - 0 = 4
  ans = max(2, 4) = 4 ✅

i=5, ch=')' → pop! stack = [] 😱
  Stack empty! Push i=5 as new boundary!
  stack = [5] 🚧

Final answer: 4 🎉
"()()" is the longest valid substring! 🏆
```

And one more where the sentinel shines:

```text
s = "()(())"
```

```text
Start: stack = [-1], ans = 0

i=0, ch='(' → stack = [-1, 0] 💃
i=1, ch=')' → pop! stack = [-1] 💘
  Length = 1 - (-1) = 2
  ans = 2 ✅

i=2, ch='(' → stack = [-1, 2] 💃
i=3, ch='(' → stack = [-1, 2, 3] 💃💃
i=4, ch=')' → pop! stack = [-1, 2] 💘
  Length = 4 - 2 = 2
  ans = max(2, 2) = 2

i=5, ch=')' → pop! stack = [-1] 💘
  Length = 5 - (-1) = 6
  ans = max(2, 6) = 6 ✅

Final answer: 6 🎉
Perfectly nested! The whole string is valid! 🏆
```

---

## 📊 Complexity

| Approach | Time | Space |
|---|---:|---:|
| 🐢 Brute force (check all substrings) | `O(n³)` | `O(1)` |
| 🚀 Stack + Sentinel | `O(n)` | `O(n)` |

### Final takeaway

> **A stack keeps boundaries, a sentinel guards the start, and one pass finds the longest dance floor.** ✨

This is a classic example of the **Stack** pattern — when you need to match opening and closing brackets, a stack is your best friend! The sentinel `-1` is the secret weapon that makes everything work! 🎯

---

## 🧠 Pattern to Remember

This problem is a great introduction to the **Stack** pattern for bracket matching:

```python
def longestValidParentheses(s):
    stack = [-1]  # 🛡️ Sentinel
    ans = 0

    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)  # 💃 Push
        else:
            stack.pop()      # 🕺 Pop
            if not stack:
                stack.append(i)  # 🚧 New boundary
            else:
                ans = max(ans, i - stack[-1])  # 📏 Calculate

    return ans
```

The same mental model appears in many problems involving:

- Valid Parentheses (is the string valid?) ✅
- Minimum Add to Make Parentheses Valid ➕
- Remove Outermost Parentheses ✂️
- Generate Parentheses (backtracking) 🌳
- Score of Parentheses (nested depth scoring) 🎯
- Remove Invalid Parentheses (BFS) 🔍
- Decode String (nested repetition) 🔁
- Basic Calculator (expression parsing) 🧮
- Trapping Rain Water (monotonic stack) 🌊
- Largest Rectangle in Histogram 📊
- Daily Temperatures (next greater element) 🌡️
- Min Stack (O(1) minimum) 📉

Happy coding! 🐍💻🎉
