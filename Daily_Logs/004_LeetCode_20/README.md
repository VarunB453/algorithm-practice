# LeetCode 20 — Valid Parentheses

> **Python 3 • Stack • Beginner Friendly 🚀**

The goal of **LeetCode 20** is to determine if a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'` is **valid** ✅

A string is **valid** if:

- Every **opening bracket** has a **matching closing bracket** of the same type 🧩
- Brackets are **closed in the correct order** 📦 (no crossing allowed!)
- Every **closing bracket** matches the **most recent unmatched opening bracket** 🎯

For example:

```text
Input:  s = "()[]{}"
Output: true
Explanation: Open brackets are closed by the same type of brackets, in the correct order 🎉
```

```text
Input:  s = "(]"
Output: false
Explanation: The '(' is closed by ']' — wrong type! Mismatch! ❌
```

```text
Input:  s = "([)]"
Output: false
Explanation: The inner ']' closes before the outer ')' — crossing brackets not allowed! 🚫
```

The key observation is wonderfully simple:

- Use a **stack** 📚 to remember unmatched **opening brackets**
- When you see an **opening bracket** → **push** it onto the stack ⬇️
- When you see a **closing bracket** → check if it matches the **top** of the stack 🔝
- If it matches → **pop** it off! ✂️
- If it doesn't match (or stack is empty) → **invalid**! ❌
- At the end, the stack must be **empty** — no leftovers allowed! 🧹

## 🎬 Little Animation

![Animated Stack trace](./20.gif)

The animation shows the stack **growing** with opening brackets 📚 and **shrinking** as matching closing brackets arrive ✂️ Watch how `([{}])` flows through the stack like a perfectly choreographed dance! 💃 The last bracket in is always the first one out — that's the magic of **LIFO**! 🎩✨

---

## 🐢 Brute-Force Solution

A straightforward brute-force idea is:

Repeatedly **remove** the innermost valid pair `"()"`, `"[]"`, or `"{}"` from the string until you can't remove anything anymore. If the string becomes **empty**, it's valid! 🧹

### Python 3

```python
class Solution:
    def isValid(self, s: str) -> bool:
        while True:
            old = s
            # Keep removing innermost valid pairs 🧹
            s = s.replace("()", "").replace("[]", "").replace("{}", "")
            if s == old:  # Nothing changed — no more pairs to remove! 🛑
                break
        return s == ""  # Empty string means everything matched! ✅
```

### Complexity

- **Time:** `O(n²)` ⏳ — In the worst case (like `"(((((...)))))"`), each `replace` scans the whole string, and we may need `O(n)` passes. That's `O(n) × O(n) = O(n²)` 💥
- **Space:** `O(n)` 💾 — String slicing creates new strings each time.

This works, but it **repeatedly rescans** the string 💥 — we're doing way more work than we need to! The stack does it all in **one pass**! 🎯

---

## 💡 Optimization Tips, Tricks & Hints

### Hint 1 — Think about the most recent opener! 🧠

When you see a **closing bracket**, which opening bracket should it match? The **most recent unmatched one**! That's exactly what a **stack** gives you — the **top** is always the most recent! 🔝

### Hint 2 — Push openers, pop on closers 🔄

- See `'('`, `'['`, or `'{'`? → **Push** it onto the stack! ⬇️
- See `')'`, `']'`, or `'}'`? → Check the **top** of the stack! 🔍
  - Matches? → **Pop** it! ✂️
  - Doesn't match or stack is empty? → **Invalid**! ❌

### Hint 3 — Don't forget the final check! ⚠️

Even if every closing bracket matched, **leftover opening brackets** in the stack mean the string is **invalid**! Always check `return not stack` at the end! 🧹

### Trick 🪄

Think of it like **nesting dolls** 🪆:

```text
Open  '('  -> place a doll inside    ⬇️
Open  '['  -> place a smaller doll   ⬇️
Close ']'  -> remove the smallest doll first! ✂️
Close ')'  -> remove the bigger doll! ✂️
All dolls removed? -> Perfect nesting! 🎉
```

You can't remove the bigger doll while the smaller one is still inside — just like you can't close `'('` before `'['` is closed! 🎯

### Bonus Trick — One-liner with a dict ✨

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in pairs:
                if not stack or stack.pop() != pairs[char]:
                    return False
            else:
                stack.append(char)
        return not stack
```

*(Clean, classic, and interview-ready! 😄)*

---

## 🚀 Optimal Solution (Stack)

The optimal solution makes **one pass** through the string — each character is processed exactly once in `O(1)` time!

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # 📚 our magical memory of unmatched openers!
        pairs = {')': '(', ']': '[', '}': '{'}  # 🗺️ closing -> opening map

        for char in s:
            if char in pairs:  # It's a CLOSING bracket! 🔒
                # Stack empty? Nothing to match! ❌
                # Top doesn't match? Wrong type! ❌
                if not stack or stack.pop() != pairs[char]:
                    return False
            else:  # It's an OPENING bracket! 🔓
                stack.append(char)  # Save it for later! ⬇️

        return not stack  # 🧹 Empty stack = everything matched! ✅
```

### Why this is optimal

Each character is processed **exactly once**:

- **Opening bracket** → one `append` (push) ⬇️ — `O(1)`
- **Closing bracket** → one `pop` and one comparison 🔍 — `O(1)`

The stack maintains:

- The **most recent unmatched opening bracket** at the **top** 🔝
- Every new closing bracket only needs to check **one** place — the top! 🎯
- No rescanning, no re-checking, no nested loops — just one smooth pass! 🛝

We process each bracket once and never look back — that's the power of the **Stack**! 📚✨

---

## 🔎 Dry Run

For:

```text
s = "([{}])"
```

The trace produces:

```text
char = '('  -> opening! push!   stack = ['(']        ⬇️
char = '['  -> opening! push!   stack = ['(', '[']   ⬇️
char = '{'  -> opening! push!   stack = ['(', '[', '{']  ⬇️
char = '}'  -> closing! top = '{' matches! pop! ✂️ stack = ['(', '[']
char = ']'  -> closing! top = '[' matches! pop! ✂️ stack = ['(']
char = ')'  -> closing! top = '(' matches! pop! ✂️ stack = []
Stack is EMPTY! -> return True ✅🎉
```

For an invalid example:

```text
s = "([)]"
```

```text
char = '('  -> opening! push!   stack = ['(']        ⬇️
char = '['  -> opening! push!   stack = ['(', '[']   ⬇️
char = ')'  -> closing! top = '[' but ')' needs '('! MISMATCH! ❌
return False 💥

The ')' tried to close the '[' — wrong type!
Just like trying to fit a square peg in a round hole! 🕳️🟥
```

And one more where openers are left behind:

```text
s = "((("
```

```text
char = '('  -> push! stack = ['(']       ⬇️
char = '('  -> push! stack = ['(', '(']  ⬇️
char = '('  -> push! stack = ['(', '(', '(']  ⬇️
End of string... stack is NOT empty! ❌
return False 🧹

Three lonely openers with no one to close them! 😢
```

---

## 📊 Complexity

| Approach | Time | Space |
|---|---:|---:|
| 🐢 Brute force (replace) | `O(n²)` | `O(n)` |
| 🚀 Stack | `O(n)` | `O(n)` |

### Final takeaway

> **Push openers, pop on closers, and let the stack remember what's left to close.** ✨

This is a classic example of the **Stack** pattern — when you need to match things in **reverse order of appearance** (LIFO), the stack is your best friend! 🎯

---

## 🧠 Pattern to Remember

This problem is a great introduction to the **Stack** pattern:

```python
def isValid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
        else:
            stack.append(char)
    return not stack
```

The same mental model appears in many problems involving:

- Matching brackets and nested structures 🧩
- Evaluating expressions (calculator problems) 🧮
- Implementing undo/redo functionality ↩️
- Parsing HTML/XML tags 🏷️
- Depth tracking in recursive structures 🌲
- Function call stacks (how recursion actually works!) 📞

Happy coding! 🐍💻🎉
