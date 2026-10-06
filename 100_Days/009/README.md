# LeetCode 14 — Longest Common Prefix

> **Python 3 • Horizontal Scanning • Beginner Friendly • Prefix Perfection! 🌟🚀**

The goal of **LeetCode 14** is to find the **longest common prefix** shared by all strings in an array! 💯🎯

You are given an array of strings `strs`.

A **prefix** is a substring that appears at the **beginning** of a string! 🏁

Our mission is to find the **longest prefix** that appears at the start of **every** string in the array! 🥳

---

## 🌟 Examples

For:

```text
Input:  strs = ["flower","flow","flight"]
Output: "fl"
```

Explanation:

```text
flower
flow
flight
 ↑↑
"fl" is the longest common prefix! 🎯
```

For:

```text
Input:  strs = ["dog","racecar","car"]
Output: ""
```

Explanation:

```text
dog
racecar
car

No common prefix exists! 🚫
```

For:

```text
Input:  strs = ["abc","abc","abc"]
Output: "abc"
```

Explanation:

```text
All strings are identical! ✅
The entire string is the prefix! 🎉
```

For:

```text
Input:  strs = ["a"]
Output: "a"
```

Explanation:

```text
Only one string! It's its own prefix! 🎊
```

---

## 🎬 Little Animation

![Longest Common Prefix Animation](./14.gif)

The animation shows the **prefix shrinking** as we compare each string! 📉🎬

Think of every string as saying:

> "Let's find what we all have in common at the start!" 🤝😄

And the prefix as saying:

> "I'm getting shorter and shorter until we all agree!" 📏💨

---

## 🐢 Brute-Force Solution

A natural brute-force idea is to check **every possible prefix** of the first string.

For each prefix length from longest to shortest, check if **all** strings start with that prefix.

For example:

```text
strs = ["flower","flow","flight"]

Try "flower" → No! ✗
Try "flowe"  → No! ✗
Try "flow"   → No! ✗
Try "flo"    → No! ✗
Try "fl"     → Yes! ✓
```

We found it! 🎉

### Python 3

```python
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Try every prefix length from longest to shortest
        first = strs[0]

        for length in range(len(first), 0, -1):
            prefix = first[:length]

            # Check if all strings start with this prefix
            all_match = True
            for s in strs[1:]:
                if not s.startswith(prefix):
                    all_match = False
                    break

            if all_match:
                return prefix

        return ""
```

### Complexity

- **Time:** `O(n × m²)` ⏳ — for each prefix length, we check all strings
- **Space:** `O(m)` 💾 — we store the prefix (where `m` is the length of the shortest string)

This approach works, but we can do even better! 🚀

---

## 💡 Optimization Tips, Tricks & Hints

### Hint 1 — Start with the First String! 🎯

The longest possible common prefix **cannot be longer** than the first string!

So start with:

```python
prefix = strs[0]
```

And shrink it as needed! 📉

---

### Hint 2 — Shrink Until It Fits! ✂️

For each new string, if the current prefix doesn't match, **remove the last character** and try again!

```python
while not s.startswith(prefix):
    prefix = prefix[:-1]
```

Keep shrinking until it fits! 🪄

---

### Hint 3 — Empty Means Done! 🏁

If the prefix becomes empty, there's **no common prefix**!

```python
if not prefix:
    return ""
```

Stop early! 🛑

---

### Hint 4 — Do We Need to Check Every Length? 🤔

No! We can **incrementally shrink** the prefix as we scan through the strings.

No need to try every possible length! 🚫🔁

---

### 🪄 The Big Trick

Use the **first string as the initial prefix**, then **shrink it** until every string matches!

```python
prefix = strs[0]

for s in strs[1:]:
    while not s.startswith(prefix):
        prefix = prefix[:-1]
```

The prefix **only gets shorter**, never longer! 📉

---

## 🚀 Optimal Solution — Horizontal Scanning

Here is the clean and optimal solution:

```python
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]

                if not prefix:
                    return ""

        return prefix
```

---

## 🧠 How Does It Work?

Let's break the magic down! ✨

### Step 1 — Initialize with the first string

```python
prefix = strs[0]
```

We start with the **entire first string** as our candidate prefix! 🎯

```text
prefix = "flower" 🌸
```

---

### Step 2 — Compare with each string

For each subsequent string, we check if it **starts with** our current prefix:

```python
while not s.startswith(prefix):
    prefix = prefix[:-1]
```

If not, we **chop off the last character** and try again! ✂️

---

### Step 3 — Shrink until match

```text
"flow" doesn't start with "flower"? 
→ Try "flowe"
→ Try "flow"
→ Try "flo"
→ Try "fl" ✓
```

We keep shrinking until we find a match! 🤝

---

### Step 4 — Empty check

```python
if not prefix:
    return ""
```

If the prefix becomes empty, **no common prefix exists**! 🚫

---

## 🔎 Dry Run

Let's trace:

```text
strs = ["flower","flow","flight"]
```

Start:

```text
prefix = "flower" 🌸
```

### String 1: "flow"

```text
Does "flow" start with "flower"? No! ✗
Does "flow" start with "flowe"?  No! ✗
Does "flow" start with "flow"?   Yes! ✓

prefix = "flow"
```

✂️ Chopped from "flower" to "flow"!

### String 2: "flight"

```text
Does "flight" start with "flow"? No! ✗
Does "flight" start with "flo"?  No! ✗
Does "flight" start with "fl"?   Yes! ✓

prefix = "fl"
```

✂️ Chopped from "flow" to "fl"!

### Final Answer

```text
"fl" 🎉
```

The longest common prefix is **"fl"**! 🎯

---

## 🎨 Prefix Visualization

For:

```text
["flower","flow","flight"]
```

you can imagine the prefix shrinking like this:

```text
Start        → prefix: "flower" 🌸

Compare "flow"
             → "flow" starts with "flower"? No! ✗
             → "flow" starts with "flowe"?  No! ✗
             → "flow" starts with "flow"?   Yes! ✓
             → prefix: "flow" 🌊

Compare "flight"
             → "flight" starts with "flow"? No! ✗
             → "flight" starts with "flo"?  No! ✗
             → "flight" starts with "fl"?   Yes! ✓
             → prefix: "fl" ✈️

Answer       → "fl" 🎉
```

The prefix is basically **shrinking to fit** every string it meets! 📏✂️

---

## ⚡ Why This Is Optimal

The optimal solution processes each string **exactly once**.

For each string, we shrink the prefix **at most** the length of the prefix times.

In the worst case, we do `O(n × m)` comparisons, where:
- `n` = number of strings
- `m` = length of the shortest string

There is no stack. 🚫📚

There is no backtracking. 🚫🔙

Just one beautiful pass through the array! 🏃‍♂️💨

---

## 📊 Complexity

Let `n` = number of strings, `m` = length of shortest string.

| Approach | Time | Space |
|---|---:|---:|
| 🐢 Brute-Force | `O(n × m²)` | `O(m)` |
| 🚀 Horizontal Scanning | `O(n × m)` | `O(1)` |

### Why is the optimal space `O(1)`?

We only use **one string variable**:

```python
prefix = strs[0]
```

No extra data structures! Just the prefix string itself! 💾✨

---

## 🧩 Pattern to Remember

This problem is a fantastic example of the **Horizontal Scanning** pattern! 🔍✨

Whenever a problem has:

- Finding common elements across multiple items 🔗
- Comparing strings character by character 🔤
- Shrinking a candidate solution ✂️
- Early termination when no match 🛑

Think:

> **HORIZONTAL SCANNING! 🔥**

The mental model is:

```text
START with first item as candidate
COMPARE with each subsequent item
SHRINK candidate until it fits
RETURN when all items match
```

---

## 🪄 One-Line Mental Shortcut

Remember this:

```text
START  → prefix = first string 🎯
SCAN   → for each string, shrink prefix until match ✂️
CHECK  → if prefix empty, return "" 🚫
END    → return prefix 🎉
```

And let the prefix **shrink to perfection**! 📏✨

---

## 🏆 Final Takeaway

> **Start big, shrink smart, and find what everyone shares!** 🚀✨

The most important trick is recognizing that we can **incrementally shrink** the prefix instead of trying every possible length.

And the beautiful little logic:

```python
while not s.startswith(prefix):
    prefix = prefix[:-1]
```

handles the **shrinking** perfectly!

```text
Too long? → Chop! ✂️
Still too long? → Chop again! ✂️✂️
Perfect fit? → Keep it! ✓
```

That's the whole magic! 🪄🎯

Keep practicing, keep shrinking, and keep smiling! 😄🐍💻

**Happy Coding! 🎉🚀❤️**
