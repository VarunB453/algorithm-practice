# 🔄 LeetCode 344 — Reverse String (Python 3)

> Reverse the character array **in-place**. No return value is required.

![Python](https://img.shields.io/badge/Python-3-blue?logo=python)
![LeetCode](https://img.shields.io/badge/LeetCode-344-orange?logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen)

## 🧩 Problem at a Glance

Given a list of characters `s`, reverse the list in-place. The function must modify `s` directly and use **O(1) auxiliary space** for the optimal approach.

**Example**

```text
Input:  s = ["h","e","l","l","o"]
Output:    ["o","l","l","e","h"]
```

## 🐢 1. Brute-Force Approach — Build a Reversed Copy

### 💡 Idea

1. Create a new list containing the characters in reverse order.
2. Copy those characters back into the original list.
3. The original list is modified, but the temporary list requires additional memory.

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        reversed_chars = s[::-1]

        for i in range(len(s)):
            s[i] = reversed_chars[i]
```

### Complexity

- **Time:** `O(n)` — create the reversed copy and write all `n` characters back.
- **Auxiliary space:** `O(n)` — the reversed copy stores `n` characters.

This is straightforward, but it does not meet the constant-extra-space goal.

## 🚀 2. Optimal Approach — Two Pointers

### 💡 Core Insight

Only the characters at the two ends need to be exchanged. Move one pointer from the left and another from the right, swapping their values until the pointers meet or cross.

**Algorithm**

1. Initialize `left = 0` and `right = len(s) - 1`.
2. While `left < right`, swap `s[left]` and `s[right]`.
3. Move `left` one step right and `right` one step left.
4. Stop when the pointers meet or cross.

### ✅ Optimal Python 3 Solution

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
```

### 🎞️ Two-Pointer Animation

The animation shows the swaps for `["h", "e", "l", "l", "o"]`.

![Two-pointer reversal animation](reverse_string_two_pointers.gif)

### 🔍 Dry Run

| Step | `left` | `right` | Array |
|---|---:|---:|---|
| Initial | 0 | 4 | `h e l l o` |
| Swap 1 | 0 | 4 | `o e l l h` |
| Move inward | 1 | 3 | `o e l l h` |
| Swap 2 | 1 | 3 | `o l l e h` |
| Stop | 2 | 2 | `o l l e h` |

At `left == right`, the middle character does not need to move.

### ⏱️ Complexity Analysis

Let `n` be the number of characters in `s`.

- **Time:** `O(n)` — each iteration performs one swap, and there are at most `⌊n / 2⌋` swaps.
- **Auxiliary space:** `O(1)` — only the two pointer variables are used; the input list is modified directly.

<details>
<summary>Why is this optimal? 🏆</summary>

Every character that is not in the correct position must be moved. Reversal pairs the first character with the last, the second with the second-last, and so on. This requires up to `⌊n / 2⌋` swaps, giving linear time, while the two-pointer method uses constant auxiliary space.

</details>

## 🧠 Interview Tips & Tricks

- **Use `left < right`, not `left != right`.** The strict comparison safely stops when the pointers meet or cross.
- **Python tuple assignment swaps in-place:** `s[left], s[right] = s[right], s[left]`.
- **Handle edge cases naturally:** empty lists, one-character lists, and odd-length lists require no special branches.
- **Respect the function contract:** modify `s`; do not return a new list.
- **Avoid slicing in the optimal solution:** `s[::-1]` creates a new list and therefore uses `O(n)` auxiliary space.

## 📌 Final Comparison

| Approach | Time | Auxiliary Space | In-place |
|---|---:|---:|---|
| Reversed copy | `O(n)` | `O(n)` | No |
| Two pointers | `O(n)` | `O(1)` | Yes |

## 🎯 Key Takeaway

**Two pointers + swapping = in-place reversal.**

The optimal solution is concise, linear-time, and constant-space. A useful pattern to remember whenever a problem asks to reverse an array or operate symmetrically from both ends.

---
*Keep solving. Keep learning. One problem at a time! 💻✨*
