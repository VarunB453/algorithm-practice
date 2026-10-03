# LeetCode 1768 — Merge Strings Alternately

> **Python 3 • Two Pointers • Beginner Friendly 🚀**

The goal of **LeetCode 1768** is to merge two strings by adding letters in **alternating** order, starting with `word1`! 💌

You are given two strings `word1` and `word2`. Merge them so that the characters take turns — one from `word1`, then one from `word2`, then back to `word1`... like a friendly handshake! 🤝

If one string is **longer** than the other, just append the extra letters to the **end** of the merged string! 📎

A merge is **valid** if:

- The first character comes from `word1` (if it's not empty) 🥇
- Characters **alternate** between the two strings 🔄
- Any **leftover** characters from the longer string get appended at the end ➕

For example:

```text
Input:  word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: a → p → b → q → c → r
             They take turns perfectly! 🎉
```

```text
Input:  word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: a → p → b → q, then 'r' and 's' are left over!
             The longer string donates its extras at the end! 📎
```

```text
Input:  word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: a → p → b → q, then 'c' and 'd' finish the party! 🎊
```

The key observation is wonderfully simple:

- Use **two pointers** — one for each string! 🎯
- On each turn, append the current character from `word1` (if any), then from `word2` (if any) 🔄
- When one string runs out, the other just keeps going! 🏃‍♂️💨
- A single loop handles **both** strings gracefully! ✨

## 🎬 Little Animation

![Animated Two Pointers trace](./1768.gif)

The animation shows the **i** and **j** pointers dancing through both strings! 🕺💃 Watch how they take turns picking letters — and when one string gets tired, the other keeps going all the way to the finish line! 🏁

---

## 🐢 Brute-Force Solution

A straightforward brute-force idea is:

Build the result **character by character** using a turn-based approach — but do it the *naive* way with extra slicing and copying! For each position, figure out whose turn it is with modulo arithmetic, then rebuild strings repeatedly! 🔍

### Python 3

```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        n, m = len(word1), len(word2)
        total = n + m

        for k in range(total):
            if k % 2 == 0:            # word1's turn 🥇
                i = k // 2
                if i < n:
                    result += word1[i]   # ⚠️ creates a NEW string each time!
            else:                     # word2's turn 🥈
                j = k // 2
                if j < m:
                    result += word2[j]   # ⚠️ creates a NEW string each time!

        # Append any leftover characters 📎
        if n > m:
            result += word1[m:]          # ⚠️ another copy!
        else:
            result += word2[n:]          # ⚠️ another copy!

        return result
```

### Complexity

- **Time:** `O((n+m)²)` ⏳ — Each `+=` on a string copies the whole accumulated result! For `n + m = 10⁵`, that's **billions** of character copies! 💥
- **Space:** `O(n + m)` 💾 — The final string (unavoidable), but tons of temporary garbage along the way! 🗑️

This works, but it's **way too slow** for large inputs! 💥 Strings in Python are **immutable** — every `+=` builds a brand-new string! The optimal approach uses a list to collect pieces and joins **once** at the end! 🎯

---

## 💡 Optimization Tips, Tricks & Hints

### Hint 1 — Collect, don't concatenate! 🧺

Python strings are **immutable** — you can't change them in place! Every `result += ch` creates a **whole new string** and copies everything over! 😱

Instead, **append to a list** and call `''.join()` **once** at the end! It's like collecting stamps in an album 📖 instead of gluing each one onto a fresh copy of the whole page! ✨

### Hint 2 — One loop, two pointers! 🎯

Here's the golden rule:

- Pointer `i` walks through `word1` 🚶‍♂️
- Pointer `j` walks through `word2` 🚶‍♀️
- Each round: take from `word1` (if available), then from `word2` (if available) 🔄
- When `i` or `j` hits the end, the `if` guard simply skips that string! 🛡️

**Why one loop?** Because the loop condition `i < n or j < m` keeps going until **both** strings are exhausted! The `or` is the secret sauce! 🥫

### Hint 3 — Don't fear the leftovers! 📎

When one string is longer, the loop naturally keeps appending from the other! No special "leftover handling" needed — the guards do all the work! 🤗

### Trick 🪄

Think of it like a **relay race** 🏃‍♂️🏃‍♀️:

```text
Two runners on a track, passing a baton! 🎽
Runner 1 (word1) goes first! 🥇
Runner 2 (word2) goes next! 🥈
They alternate strides until one runs out of track! 🏁
The runner with more energy finishes the rest of the lap! 💪
```

### Bonus Trick — Zip it up with itertools! 🤐

```python
from itertools import zip_longest

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join(a + b for a, b in zip_longest(word1, word2, fillvalue=''))
```

*(Pythonic, elegant, and interview-flexible! 😄 — `zip_longest` pairs characters and fills the gaps with empty strings!)*

---

## 🚀 Optimal Solution (Two Pointers + List)

The optimal solution makes **one pass** through both strings — appending to a list and joining **once** at the end!

```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []  # 🧺 Collect characters here — no copying!
        i = j = 0    # 🎯 Two pointers, one for each string!

        while i < len(word1) or j < len(word2):  # 🔄 Until BOTH are done!
            if i < len(word1):      # 🥇 word1's turn (if it has letters left)!
                result.append(word1[i])
                i += 1

            if j < len(word2):      # 🥈 word2's turn (if it has letters left)!
                result.append(word2[j])
                j += 1

        return ''.join(result)  # 🎉 One single join — fast and clean!
```

### Why this is optimal

Each character is visited **exactly once**:

- **Total iterations:** At most `max(n, m)` rounds — each round consumes **at least one** character! 📏
- **Each iteration:** Two comparisons, at most two appends — all `O(1)`! ⚡
- **Final join:** `O(n + m)` — one linear pass to build the result! 🤝
- **No waste:** Every character is copied exactly **once** into the final string! ✅

The two-pointer strategy works because:

- We **never miss** a character — both pointers march to the very end! ✅
- We **never copy twice** — list appends are `O(1)` amortized! ⏩
- It's a beautiful example of **two pointers + list buffer** working together! 🤝

We touch each letter at most once — that's the power of the **Two Pointers**! 🎯✨

---

## 🔎 Dry Run

For:

```text
word1 = "abc", word2 = "pqr"
```

The trace produces:

```text
Start: i=0, j=0, result=[]
  word1[0]='a' → result=['a']    i=1 🚶‍♂️
  word2[0]='p' → result=['a','p'] j=1 🚶‍♀️

Round 2: i=1, j=1
  word1[1]='b' → result=['a','p','b']    i=2 🚶‍♂️
  word2[1]='q' → result=['a','p','b','q'] j=2 🚶‍♀️

Round 3: i=2, j=2
  word1[2]='c' → result=[...,'c']    i=3 🚶‍♂️
  word2[2]='r' → result=[...,'r']    j=3 🚶‍♀️

i == 3 and j == 3 → both done! 🏁
Join: "apbqcr" ✅
```

For a case with leftovers:

```text
word1 = "ab", word2 = "pqrs"
```

```text
Start: i=0, j=0, result=[]
  word1[0]='a' → result=['a']    i=1 🚶‍♂️
  word2[0]='p' → result=['a','p'] j=1 🚶‍♀️

Round 2: i=1, j=1
  word1[1]='b' → result=['a','p','b']    i=2 🚶‍♂️
  word2[1]='q' → result=['a','p','b','q'] j=2 🚶‍♀️

Round 3: i=2, j=2
  word1 exhausted! 😴 (i=2 == len("ab"))
  word2[2]='r' → result=[...,'r']    j=3 🚶‍♀️

Round 4: i=2, j=3
  word1 still exhausted! 😴
  word2[3]='s' → result=[...,'s']    j=4 🚶‍♀️

i == 2, j == 4 → both done! 🏁
Join: "apbqrs" ✅

The longer string donated its extras! 📎
```

And one more where word1 is the marathon runner:

```text
word1 = "abcd", word2 = "pq"
```

```text
Start: i=0, j=0
  'a' → i=1 🚶‍♂️   'p' → j=1 🚶‍♀️

Round 2: i=1, j=1
  'b' → i=2 🚶‍♂️   'q' → j=2 🚶‍♀️

Round 3: i=2, j=2
  'c' → i=3 🚶‍♂️   word2 exhausted! 😴

Round 4: i=3, j=2
  'd' → i=4 🚶‍♂️   word2 still exhausted! 😴

i == 4, j == 2 → both done! 🏁
Join: "apbqcd" ✅

word1 finished the race solo! 🏃‍♂️💨
```

---

## 📊 Complexity

| Approach | Time | Space |
|---|---:|---:|
| 🐢 Brute force (string +=) | `O((n+m)²)` | `O(n + m)` |
| 🚀 Two Pointers + List | `O(n + m)` | `O(n + m)` |

### Final takeaway

> **Two pointers take turns, a list collects the pieces, and one join seals the deal.** ✨

This is a classic example of the **Two Pointers** pattern — when you need to interleave two sequences, walking both with dedicated indices keeps everything clean, clear, and linear! 🎯

---

## 🧠 Pattern to Remember

This problem is a great introduction to the **Two Pointers** pattern:

```python
def mergeAlternately(word1, word2):
    result = []
    i = j = 0
    while i < len(word1) or j < len(word2):
        if i < len(word1):
            result.append(word1[i])
            i += 1
        if j < len(word2):
            result.append(word2[j])
            j += 1
    return ''.join(result)
```

The same mental model appears in many problems involving:

- Merging two sorted arrays (Merge Sorted Array) 🤝
- Merging two sorted linked lists 🔗
- Comparing strings with backspaces (Backspace String Compare) ⌫
- Interleaving values in a linked list (Reorder List) 🔄
- Two Sum II on a sorted array 🎯
- Finding the intersection of two arrays 🔍
- Valid Palindrome (move pointers from both ends) 🔄
- Longest Common Prefix (shrink from the ends) ✂️

Happy coding! 🐍💻🎉
