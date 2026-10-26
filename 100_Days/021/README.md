# 🚀 LeetCode 383 — Ransom Note (Python 3)

> **Problem:** Determine whether `ransomNote` can be constructed from the characters in `magazine`.
> Each character in `magazine` can be used **at most once**.

---

## 🧩 Intuition

Imagine cutting letters out of a magazine to build a ransom note. ✂️📰  
If the note needs three `a`s, the magazine must contain at least three `a`s. Having the right *kind* of letters is not enough—the **frequency** of each letter matters.

## 🐢 Brute-Force Approach

The submitted solution checks each distinct character and counts its occurrences in both strings:

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        for c in set(ransomNote):
            if magazine.count(c) < ransomNote.count(c):
                return False

        return True
```

### How it works

1. If `ransomNote` is longer than `magazine`, construction is impossible.
2. For each distinct character in `ransomNote`, compare its frequency in both strings.
3. If the magazine has too few copies of any character, return `False`.
4. If every required frequency is available, return `True`.

### Complexity of this approach

Let \(n = \text{len(ransomNote)}\) and \(m = \text{len(magazine)}\).

- **Time:** \(O(nm)\) in the worst case. Each `.count()` scans a string, and the loop can run for up to \(n\) distinct characters.
- **Auxiliary space:** \(O(k)\), where \(k\) is the number of distinct characters in `ransomNote`, for `set(ransomNote)`. With a fixed alphabet, this is \(O(1)\).

> 💡 **Important:** This is a valid frequency-counting solution, but repeatedly calling `.count()` rescans the strings. A frequency table avoids that repeated work.

---

## ⚡ Optimal Approach — Frequency Counting

Count the characters in `magazine`, then consume one count for each character required by `ransomNote`. If a required character is unavailable, construction fails immediately.

### Python 3 solution

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        available = [0] * 26

        for c in magazine:
            available[ord(c) - ord('a')] += 1

        for c in ransomNote:
            index = ord(c) - ord('a')

            if available[index] == 0:
                return False

            available[index] -= 1

        return True
```

### 🎬 Character-count animation

Example:

```text
ransomNote = "aa"
magazine   = "aab"
```

**Step 1 — Count the magazine letters**

```text
Magazine:  a  a  b
Count:     2  1
           a  b
```

**Step 2 — Build the note one character at a time**

```text
Need first 'a':  available a = 2  → use one → 1  ✅
Need second 'a': available a = 1  → use one → 0  ✅
All required letters used successfully! 🎉
Result: True
```

If the note were `"aaa"`, the third `a` would be unavailable, so the result would be `False` ❌.

### Complexity

Let \(n = \text{len(ransomNote)}\) and \(m = \text{len(magazine)}\).

- **Time:** \(O(n + m)\), because each string is traversed at most once.
- **Auxiliary space:** \(O(1)\), because the frequency list always has 26 entries for lowercase English letters.

---

## 🧠 Tips, Tricks & Hints

- **Check lengths first:** If the note is longer than the magazine, return `False` immediately.
- **Think in frequencies:** The problem is about how many times each letter appears, not just whether a letter exists.
- **Consume letters:** Decrease a count when using a character so that no magazine character is reused.
- **Use the constraints:** A 26-element array is efficient when inputs contain only lowercase English letters.
- **Alternative Python shortcut:** `collections.Counter` expresses the same frequency idea clearly, although a fixed-size array has predictable constant auxiliary space for this alphabet.

```python
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not (Counter(ransomNote) - Counter(magazine))
```

For this Counter version, expected time is \(O(n + m)\); auxiliary space is \(O(u)\), where \(u\) is the number of distinct characters stored.

## 🧪 Quick Test Cases

| `ransomNote` | `magazine` | Result | Why? |
|---|---|---|---|
| `"a"` | `"b"` | `False` | Required letter is missing |
| `"aa"` | `"ab"` | `False` | Only one `a` is available |
| `"aa"` | `"aab"` | `True` | Both `a`s are available |
| `""` | `"abc"` | `True` | An empty note needs no letters |

## 🏁 Final Takeaway

The brute-force version is easy to understand, but it repeatedly counts characters. The frequency-array solution counts the magazine once and then consumes letters as needed, improving the worst-case time complexity from **\(O(nm)\)** to **\(O(n+m)\)**.

**Count once. Consume carefully. Build the note!** 📰🔤✨
