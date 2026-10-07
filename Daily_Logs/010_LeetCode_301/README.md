# LeetCode 301 — Remove Invalid Parentheses

> **Python 3 • Backtracking • BFS/DFS • Beginner Friendly 🚀**

The goal of **LeetCode 301** is to remove the **minimum number of invalid parentheses** so that the remaining string becomes valid! 🧩✨

We need to return **all possible valid strings** after removing the minimum number of parentheses. 🎯

---

## 🧠 Understanding the Problem

A parentheses string is valid when:

- Every `(` has a matching `)` 🤝
- While scanning left to right, the number of `)` never becomes greater than the number of `(` 📊
- At the end, the number of `(` and `)` must be equal ⚖️

For example:

```text
Input:  s = "()())()"

Output:
["(())()", "()()()"]
```

Both answers remove exactly **one** `)` and are valid! 🎉

Another example:

```text
Input:  s = "(a)())()"

Output:
["(a())()", "(a)()()"]
```

And:

```text
Input:  s = ")("

Output:
[""]
```

We must remove both parentheses because neither can form a valid pair. 🧹

---

## 🔍 Key Observation

The important part is **minimum removals**.

Before doing any expensive search, we can calculate exactly how many `(` and `)` must be removed! 🎯

For example:

```text
s = "()())()"

Scan from left to right:

(  → balanced = 1
)  → balanced = 0
(  → balanced = 1
)  → balanced = 0
)  → extra ')' found! ❌
(  → balanced = 1
)  → balanced = 0
```

So we know:

```text
Extra '(' to remove = 0
Extra ')' to remove = 1
```

That means our search only needs to remove **one `)`**. ✨

---

## 🎬 Little Animation

```text
Input: ()())()

          ↓ scan

(   → balance = 1   🟢
)   → balance = 0   🟢
(   → balance = 1   🟢
)   → balance = 0   🟢
)   → balance = -1  🔴  ← extra ')'
(   → balance = 0   🟢
)   → balance = 0   🟢

             ↓

Remove the extra ')' and explore choices:

        ()())()
          /   \
     (())()   ()()()

          ↓

     🎉 Valid answers!
```

Think of `balance` as a little scoreboard:

```text
balance > 0  → We have unmatched '(' 🟡
balance = 0  → Everything is balanced! 🟢
balance < 0  → Too many ')' ❌
```

---

## 🐢 Brute-Force Solution

A natural brute-force idea is:

> Try removing parentheses in every possible way until we find valid strings. 🎲

We could try:

```text
Remove 0 parentheses
        ↓
Remove 1 parenthesis
        ↓
Remove 2 parentheses
        ↓
Remove 3 parentheses
        ↓
...
```

For each possibility, check whether the resulting string is valid. 🔎

### Simple Brute Force Idea

Generate **every subsequence** of the string:

```python
def is_valid(s):
    balance = 0

    for ch in s:
        if ch == '(':
            balance += 1
        elif ch == ')':
            balance -= 1

            if balance < 0:
                return False

    return balance == 0
```

Then:

```python
def brute_force(s):
    valid = set()

    def dfs(i, path):
        if i == len(s):
            candidate = "".join(path)

            if is_valid(candidate):
                valid.add(candidate)

            return

        # Keep current character
        path.append(s[i])
        dfs(i + 1, path)
        path.pop()

        # Remove current character
        dfs(i + 1, path)

    dfs(0, [])
    return list(valid)
```

### Why is this slow? 🐢

For every character, we have **two choices**:

```text
Keep it  OR  Remove it
```

So there can be approximately:

```text
2^n
```

different subsequences.

And each candidate may require `O(n)` time to validate.

### Complexity

- **Time:** `O(n · 2^n)` ⏳
- **Space:** `O(n · 2^n)` 💾 for generated candidates/results

This works for small inputs, but LeetCode 301 needs something much smarter! 🚀

---

# 💡 Optimization Tips, Tricks & Hints

## Hint 1 — Find the minimum removals first! 🎯

Don't blindly remove parentheses.

First calculate:

```text
remove_left
remove_right
```

For example:

```text
"())("

Scan:

(  → balance = 1
)  → balance = 0
)  → extra ')' → remove_right = 1
(  → balance = 1

At the end:

remove_left = 1
remove_right = 1
```

So exactly **two parentheses** must be removed. ✂️

---

## Hint 2 — Never let balance become negative! 🚨

During DFS:

```python
if balance < 0:
    return
```

Why?

Because once we have:

```text
"))("
 ^
```

there is already a `)` without a matching `(`.

Adding more characters cannot repair that prefix. ❌

So we can immediately stop exploring that branch.

This is called **pruning** 🌳✂️

---

## Hint 3 — Only remove parentheses when necessary 🎯

If we still need to remove a `)`:

```python
remove_right > 0
```

then we can choose to remove it.

Similarly for `(`:

```python
remove_left > 0
```

This prevents us from deleting more parentheses than necessary.

---

## Hint 4 — Avoid duplicate work! 🧹

Suppose we have:

```text
"((()))"
```

Removing the first `(` or the second identical `(` can lead to the same result.

Instead of exploring both, skip consecutive duplicate parentheses when making the **remove** decision.

```python
if i > start and s[i] == s[i - 1]:
    continue
```

This can dramatically reduce duplicate branches! 🚀

---

## 🪄 The Big Trick

The problem becomes much easier when we separate it into two phases:

```text
1️⃣ Calculate minimum removals
        ↓
2️⃣ DFS only among strings with those removals
```

Instead of:

```text
Try everything 😵‍💫
```

we do:

```text
Calculate what MUST be removed 🎯
        ↓
Search only valid possibilities 🌳
        ↓
Prune impossible branches ✂️
        ↓
Collect unique answers 🎉
```

---

# 🚀 Optimal Solution — DFS + Backtracking

Here is the clean Python 3 solution:

```python
class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        # Find the minimum number of '(' and ')' to remove.
        remove_left = 0
        remove_right = 0

        for ch in s:
            if ch == '(':
                remove_left += 1

            elif ch == ')':
                if remove_left > 0:
                    remove_left -= 1
                else:
                    remove_right += 1

        result = []

        def dfs(index, path, balance, left_rem, right_rem):
            # Invalid prefix -> prune!
            if balance < 0:
                return

            if index == len(s):
                if balance == 0 and left_rem == 0 and right_rem == 0:
                    result.append("".join(path))
                return

            ch = s[index]

            # Remove current parenthesis
            if ch == '(' and left_rem > 0:
                # Skip duplicate removal choices.
                if index == 0 or s[index - 1] != '(':
                    dfs(
                        index + 1,
                        path,
                        balance,
                        left_rem - 1,
                        right_rem
                    )

            elif ch == ')' and right_rem > 0:
                # Skip duplicate removal choices.
                if index == 0 or s[index - 1] != ')':
                    dfs(
                        index + 1,
                        path,
                        balance,
                        left_rem,
                        right_rem - 1
                    )

            # Keep current character
            path.append(ch)

            if ch == '(':
                dfs(
                    index + 1,
                    path,
                    balance + 1,
                    left_rem,
                    right_rem
                )

            elif ch == ')':
                dfs(
                    index + 1,
                    path,
                    balance - 1,
                    left_rem,
                    right_rem
                )

            else:
                dfs(
                    index + 1,
                    path,
                    balance,
                    left_rem,
                    right_rem
                )

            path.pop()

        dfs(
            0,
            [],
            0,
            remove_left,
            remove_right
        )

        return result
```

---

# 🔎 Dry Run

Let's use:

```text
s = "()())()"
```

First calculate removals:

```text
remove_left  = 0
remove_right = 1
```

Now DFS explores possibilities.

```text
                    ()())()
                       |
             ┌─────────┴─────────┐
             │                   │
          KEEP ')'           REMOVE ')'
             │                   │
             ❌                  ↓
                       valid candidates
                       /          \
                  (())()        ()()()
```

Eventually:

```text
result = [
    "(())()",
    "()()()"
]
```

🎉 Both are valid and both use exactly **one removal**.

---

# 🎞️ DFS Animation

Imagine the recursion as a tree 🌳:

```text
                         "()())()"
                             |
                    ┌────────┴────────┐
                    │                 │
                  KEEP              REMOVE
                    │                 │
                 invalid          "()()()"
                    │
                  prune ✂️

Another branch:

                         "()())()"
                             |
                         choices
                        /       \
                    "(())()"   "()()()"
                       ✅          ✅
```

The algorithm constantly asks:

```text
🤔 Should I KEEP this parenthesis?
        OR
✂️ Should I REMOVE it?
```

But we only allow removal when we **know a removal is required**.

And if:

```text
balance < 0
```

we immediately say:

```text
🚫 STOP!
This branch can never become valid.
```

That's the magic of pruning! ✨

---

# 🧠 Why the Optimal Solution Works

There are three important ideas.

### 1️⃣ Minimum removals are calculated first

We know exactly how many:

```text
'(' → remove_left
')' → remove_right
```

must disappear.

So every final answer uses the minimum possible number of removals. 🎯

### 2️⃣ Balance guarantees validity

While scanning:

```text
'(' → balance + 1
')' → balance - 1
```

If:

```text
balance < 0
```

the current prefix is invalid.

At the end:

```text
balance == 0
```

means every opening parenthesis has been matched. 🤝

### 3️⃣ Duplicate removal is skipped

For consecutive equal parentheses:

```text
"(("
```

removing the first or second `(` creates equivalent possibilities.

So we skip duplicate removal choices:

```python
if index == 0 or s[index - 1] != '(':
```

This keeps the result unique and avoids unnecessary work. 🧹✨

---

# 📊 Complexity

Let:

- `n` = length of the string
- `R` = number of valid answers

The DFS may still explore exponentially many possibilities in the worst case.

| Approach | Time | Space |
|---|---:|---:|
| 🐢 Brute force | `O(n · 2^n)` | `O(n · 2^n)` |
| 🚀 DFS + pruning | Exponential worst case | `O(n · R)` |

For the optimal approach:

- **Time:** `O(n · 2^n)` worst case ⏳
- **Space:** `O(n · R)` for recursion/path and stored results 💾

The important practical improvement is the **pruning + minimum-removal calculation**, which avoids huge amounts of useless work. 🚀

---

# 🎯 Brute Force vs Optimal

```text
🐢 BRUTE FORCE

Generate everything
       ↓
Check everything
       ↓
Keep valid strings

😵‍💫 Lots of useless work!


🚀 OPTIMAL

Count required removals
       ↓
DFS with constraints
       ↓
Prune invalid prefixes ✂️
       ↓
Skip duplicates 🧹
       ↓
Return unique valid answers 🎉
```

The biggest lesson isn't simply:

> "Use DFS."

It's:

> **Use DFS with strong constraints and aggressive pruning.** 🧠✨

---

# 🧩 Pattern to Remember

LeetCode 301 is a fantastic example of:

```text
BACKTRACKING + PRUNING + DUPLICATE SKIPPING
```

Whenever a problem asks you to:

- Generate **all valid possibilities** 🌳
- Remove the **minimum number** of elements ✂️
- Avoid **duplicate answers** 🧹
- Stop exploring impossible states early 🚫

think:

```text
🎯 Calculate constraints
        ↓
🌳 Backtrack
        ↓
✂️ Prune
        ↓
🧹 Skip duplicates
        ↓
🎉 Collect answers
```

---

# 🏆 Final Takeaway

The most important idea is:

> **Don't search blindly. First determine what must be removed, then use DFS to explore only the possibilities that can still become valid.** 🎯

Remember these three superpowers:

```text
🔢 Count minimum removals
⚖️ Track balance
✂️ Prune impossible branches
```

And one bonus superpower:

```text
🧹 Skip duplicate removal choices
```

That's how we turn a huge brute-force search into a much smarter backtracking solution! 🚀🐍💻

---

## 🎉 Happy Coding!

```text
          🌳
         / \
        /   \
      🧠   ✂️
      |     |
   BACKTRACK PRUNE
      \     /
       \   /
        🎯
     VALID!
        🎉
```

**Keep calm, prune branches, and code on! 😄🐍💻🚀**
