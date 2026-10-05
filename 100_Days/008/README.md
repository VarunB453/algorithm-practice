# LeetCode 392 — Is Subsequence

> **Python 3 • Two Pointers • Beginner Friendly 🚀**

The goal of **LeetCode 392** is to determine if string `s` is a **subsequence** of string `t`! 💌

You are given two strings `s` and `t`. Your mission is to check if `s` appears as a **subsequence** inside `t` — meaning you can delete some (or none) of the characters from `t` and get exactly `s`! 🤝

A string `s` is a **subsequence** of `t` if:

- Every character of `s` appears in `t` **in the same order** 🥇
- Characters in `s` don't need to be **adjacent** in `t` — they just need to show up in order! 🔄
- You **cannot reorder** characters — order matters! ➕

For example:

```text
Input:  s = "abc", t = "ahbgdc"
Output: true
Explanation: We can find 'a' at index 0, 'b' at index 2, 'c' at index 5!
             They appear in order! "a...b.....c" — perfect match! 🎉
```

```text
Input:  s = "axc", t = "ahbgdc"
Output: false
Explanation: We can find 'a' and 'c', but 'x' is nowhere to be found! 😢
             No matter how hard we search, 'x' doesn't exist in t! 🚫
```

```text
Input:  s = "", t = "ahbgdc"
Output: true
Explanation: An empty string is a subsequence of ANY string! 🎈
             Nothing to find means nothing to fail! 😄
```

```text
Input:  s = "abc", t = ""
Output: false
Explanation: t is empty but s has characters — impossible! 😱
```

The key observation is wonderfully simple:

- Use **two pointers** — one for `s` and one for `t`! 🎯
- Scan through `t` with one pointer, looking for characters of `s` in order! 🔍
- If we find a match, advance **both** pointers! 💘
- If we don't find a match, advance **only** the `t` pointer — keep looking! 🔎
- If we finish scanning `s`, it's a subsequence! ✅

## 🎬 Little Animation

![Two Pointers Animation](./392.gif)

The animation shows **two pointers** racing through the strings! 🏃‍♂️🏃‍♀️ Watch how the `s` pointer only moves when it finds its soulmate character in `t`! The `t` pointer never stops — it scans everything! When `s` pointer reaches the end, it's party time! 🎉

---

## 🐢 Brute-Force Solution

A straightforward brute-force idea is:

Use **recursion** to try every possible way to match characters! For each character in `s`, try to find it in `t` at every possible position after the previous match! 🔍

### Python 3

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def helper(s_idx, t_idx):
            # Base case: we've matched all of s! 🎉
            if s_idx == len(s):
                return True

            # Base case: we've exhausted t but s still has characters! 😢
            if t_idx == len(t):
                return False

            # If characters match, try advancing both pointers! 💘
            if s[s_idx] == t[t_idx]:
                # Try matching them, OR skip this t character
                return helper(s_idx + 1, t_idx + 1) or helper(s_idx, t_idx + 1)

            # No match — skip this t character and keep looking! 🔎
            return helper(s_idx, t_idx + 1)

        return helper(0, 0)
```

### Complexity

- **Time:** `O(2^n)` ⏳ — In the worst case, we explore two recursive branches at every step! For `n = 10⁴`, that's **way too slow**! 💥
- **Space:** `O(n)` 💾 — Recursion stack depth!

This works for tiny inputs, but it's **brutally slow** for large strings! 💥 We need something smarter! 🎯

---

## 💡 Optimization Tips, Tricks & Hints

### Hint 1 — Two Pointers are your best friends! 🧑‍🤝‍🧑

Think of it like a **scavenger hunt**! 🔍 You have a shopping list (`s`) and you're walking through a store (`t`)! You only check off items in order — you never go back! 🛒

- Pointer `i` tracks your position in `s` (your shopping list) 📝
- Pointer `j` tracks your position in `t` (the store aisles) 🏪
- When `s[i] == t[j]`, you found an item! Check it off! Advance both! ✅
- When `s[i] != t[j]`, keep walking! Advance only `j`! 🚶

### Hint 2 — Order is EVERYTHING! 📏

The characters must appear in the **same order** in both strings! You can't match 'b' before 'a' if `s = "ab"`! The two-pointer approach naturally enforces this because pointers only move **forward**! ➡️

### Hint 3 — When in doubt, keep scanning! 🔎

If `t[j]` doesn't match `s[i]`, don't panic! Just move `j` forward! The character we need might be hiding further ahead! 🙈

### Trick 🪄

Think of it like a **romantic movie** 💕:

```text
's' is looking for their perfect match in 't'! 💘
They walk through the crowd (t) one person at a time! 🚶
When they spot their type (matching character)! 😍
They move on to the next person on their list! 📋
If they finish their entire list — it's a HAPPY ENDING! 💑
If the crowd ends first — heartbreak! 💔
```

### Bonus Trick — Greedy is Optimal! 🏆

Why does greedy work? Because **matching as early as possible** leaves the **maximum remaining characters** in `t` for the rest of `s`! There's never a benefit to skipping a matching character! 🎯

```python
# Greedy insight: always take the FIRST match you find!
# This leaves more options for the remaining characters!
# It's like eating your favorite candy first — no regrets! 🍬
```

---

## 🚀 Optimal Solution (Two Pointers)

The optimal solution makes **one pass** through the string `t` — using two pointers to track progress!

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0  # 📝 Pointer for s — our shopping list!
        j = 0  # 🏪 Pointer for t — the store!

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1  # ✅ Found a match! Check it off! Move to next item!
            j += 1      # 🚶 Always move through the store!

        return i == len(s)  # 🎉 Did we check off everything on our list?
```

### Why this is optimal

Each character in `t` is processed **exactly once**:

- **Total iterations:** `O(n)` where `n = len(t)` — one single loop! 📏
- **Each iteration:** Simple comparison and pointer increments — all `O(1)`! ⚡
- **No waste:** Every character in `t` is visited exactly **once**! ✅

The two-pointer strategy works because:

- We **never backtrack** — pointers only move forward! ➡️
- We **match greedily** — taking the first match is always optimal! 🎯
- If we finish `s`, all characters were found **in order**! ✅
- It's a beautiful example of **greedy + two pointers** working together! 🤝

We touch each character exactly once — that's the power of the **Two Pointer** technique! 🎯✨

---

## 🔎 Dry Run

For:

```text
s = "ace", t = "abcde"
```

The trace produces:

```text
Start: i = 0 (pointing to 'a'), j = 0 (pointing to 'a')

Step 1: s[0]='a', t[0]='a' → MATCH! 💘
  i = 1, j = 1
  Found 'a'! Looking for 'c' now!

Step 2: s[1]='c', t[1]='b' → No match! 😅
  i = 1, j = 2
  'b' is not 'c' — keep walking!

Step 3: s[1]='c', t[2]='c' → MATCH! 💘
  i = 2, j = 3
  Found 'c'! Looking for 'e' now!

Step 4: s[2]='e', t[3]='d' → No match! 😅
  i = 2, j = 4
  'd' is not 'e' — keep walking!

Step 5: s[2]='e', t[4]='e' → MATCH! 💘
  i = 3, j = 5
  Found 'e'! List is complete!

i == len(s) → 3 == 3 → TRUE! ✅

Final answer: true 🎉
"ace" is a subsequence of "abcde"! 🏆
```

For a failing case:

```text
s = "aec", t = "abcde"
```

```text
Start: i = 0 (pointing to 'a'), j = 0 (pointing to 'a')

Step 1: s[0]='a', t[0]='a' → MATCH! 💘
  i = 1, j = 1
  Found 'a'! Looking for 'e' now!

Step 2: s[1]='e', t[1]='b' → No match! 😅
  i = 1, j = 2

Step 3: s[1]='e', t[2]='c' → No match! 😅
  i = 1, j = 3

Step 4: s[1]='e', t[3]='d' → No match! 😅
  i = 1, j = 4

Step 5: s[1]='e', t[4]='e' → MATCH! 💘
  i = 2, j = 5
  Found 'e'! Looking for 'c' now!

Step 6: j = 5, loop ends (j >= len(t))! 🏁

i = 2, len(s) = 3
i != len(s) → FALSE! ❌

Final answer: false 💔
We found 'a' and 'e', but 'c' comes BEFORE 'e' in t!
The order is wrong — "aec" is NOT a subsequence! 😢
```

And one more edge case:

```text
s = "", t = "anything"
```

```text
Start: i = 0, j = 0

Loop condition: i < len(s) → 0 < 0 → False!
Loop doesn't even run! 🏁

i == len(s) → 0 == 0 → TRUE! ✅

Final answer: true 🎉
Empty string is a subsequence of everything! 🏆
```

---

## 📊 Complexity

| Approach | Time | Space |
|---|---:|---:|
| 🐢 Brute force (recursion) | `O(2^n)` | `O(n)` |
| 🚀 Two Pointers | `O(n)` | `O(1)` |

### Final takeaway

> **Two pointers walk hand in hand — one scans, one matches, and order tells the story.** ✨

This is a classic example of the **Two Pointer** pattern — when you need to check if one sequence appears in order within another, two pointers are your best friends! The greedy approach of matching early is the secret weapon that makes everything work! 🎯

---

## 🧠 Pattern to Remember

This problem is a great introduction to the **Two Pointer** pattern for sequence matching:

```python
def isSubsequence(s, t):
    i = j = 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1  # ✅ Match found!
        j += 1      # 🚶 Keep scanning!

    return i == len(s)  # 🎉 All matched?
```

The same mental model appears in many problems involving:

- Two Sum II (sorted array) 🔢
- Merge Sorted Arrays 🔀
- Remove Duplicates from Sorted Array ✂️
- Container With Most Water 💧
- 3Sum (triplet finding) 🔺
- Sort Colors (Dutch National Flag) 🎨
- Minimum Window Substring (sliding window cousin) 🪟
- Longest Substring Without Repeating Characters 📏
- Valid Palindrome (two ends) 🔄
- Move Zeroes ➡️
- Intersection of Two Arrays ➗
- Find the Duplicate Number 🔍

Happy coding! 🐍💻🎉
