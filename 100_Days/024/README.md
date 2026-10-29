<div align="center">

# 🚀 LeetCode 128 — Longest Consecutive Sequence

### 🐍 Python 3 | Hash Set | Arrays | Interview Preparation

**Find the longest streak of consecutive integers — without sorting!**

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange)
![Language](https://img.shields.io/badge/Language-Python%203-blue?logo=python&logoColor=white)
![Time](https://img.shields.io/badge/Optimal%20Time-O(n)-brightgreen)
![Space](https://img.shields.io/badge/Space-O(n)-blue)

</div>

---

## 🧭 Problem Statement

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

The algorithm must run in **O(n) time**.

**Example 1**

```text
Input:  nums = [100, 4, 200, 1, 3, 2]
Output: 4
```

Explanation: The longest consecutive sequence is `[1, 2, 3, 4]`, so the answer is `4`.

**Example 2**

```text
Input:  nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
Output: 9
```

Explanation: The longest consecutive sequence is `[0, 1, 2, 3, 4, 5, 6, 7, 8]`, so the answer is `9`.

**Example 3**

```text
Input:  nums = [1, 0, 1, 2]
Output: 3
```

Explanation: Duplicate values do not increase the sequence length. The longest sequence is `[0, 1, 2]`.

---

## 💡 Approach 1: Brute Force

### Idea

For every number, repeatedly search for the next consecutive number (`n + 1`, `n + 2`, and so on) in the input array. Count how long the sequence continues, then keep the maximum length.

### Python 3 solution

```python
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        for n in nums:
            length = 1
            next_num = n + 1

            while next_num in nums:
                length += 1
                next_num += 1

            longest = max(longest, length)

        return longest
```

### 🎞️ Brute-force walkthrough

For `nums = [1, 3, 2, 4]`:

```text
Start at 1
   |
   v
Is 2 present?  YES
   |
   v
Is 3 present?  YES
   |
   v
Is 4 present?  YES
   |
   v
Is 5 present?  NO
   |
   v
Sequence length = 4
```

The algorithm repeats this process for every element, including elements that belong to a sequence already counted.

### Complexity

- **Time:** `O(n²)` in the worst case. Each membership test (`next_num in nums`) scans the list and can take `O(n)`, repeated across up to `n` starting elements.
- **Auxiliary space:** `O(1)` excluding the input.

### ⚠️ Why improve it?

Repeated linear membership checks are expensive. Also, starting from every element repeats work for the same sequence. A hash set can make membership checks average `O(1)` and help us skip numbers that are not sequence beginnings.

---

## 🏆 Approach 2: Optimal — Hash Set

### Key insight

A number is the **start of a consecutive sequence** only if its predecessor (`n - 1`) is absent from the set.

For example, in `{1, 2, 3, 4}`:

- `1` is a sequence start because `0` is absent.
- `2` is not a start because `1` exists.
- `3` is not a start because `2` exists.
- `4` is not a start because `3` exists.

Therefore, expand a sequence only when its starting number is found. This prevents repeatedly counting the same streak.

### 🧠 Hints and interview tips

1. **Use a set:** `set(nums)` removes duplicates and provides average `O(1)` membership checks.
2. **Look backward first:** Only begin counting when `n - 1 not in numset`.
3. **Count forward:** Keep checking `n + 1`, `n + 2`, and so on.
4. **Update the maximum:** Compare each sequence length with `longest`.
5. **Do not sort:** Sorting would typically take `O(n log n)`, which misses the required `O(n)` time bound.
6. **Handle edge cases:** An empty input returns `0`; duplicates do not extend a sequence.

### ✅ Optimal Python 3 solution

```python
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for n in numset:
            # Only process the beginning of a sequence.
            if n - 1 not in numset:
                length = 1

                # Extend the sequence while the next number exists.
                while n + length in numset:
                    length += 1

                longest = max(longest, length)

        return longest
```

This is the same core algorithm as your submitted solution. The set both removes duplicates and supports efficient membership checks.

---

## 🎬 Animation: How the optimal solution works

Example: `nums = [100, 4, 200, 1, 3, 2]`

### Frame 1 — Build the set

```text
Input: [100, 4, 200, 1, 3, 2]

Hash set:
{100, 4, 200, 1, 3, 2}

longest = 0
```

### Frame 2 — Skip numbers inside a sequence

The set's iteration order is not guaranteed, but the result is the same regardless of order.

```text
Check n = 4:
3 exists → not a sequence start → skip

Check n = 3:
2 exists → not a sequence start → skip

Check n = 2:
1 exists → not a sequence start → skip
```

### Frame 3 — Find the start at 1

```text
Check n = 1:
0 does not exist → sequence start!

1 → 2 → 3 → 4 → 5
    ✓   ✓   ✓   ✗

length = 4
longest = max(0, 4) = 4
```

### Frame 4 — Check the remaining starts

```text
n = 100:
99 is absent → start of a sequence
101 is absent → length = 1
longest = max(4, 1) = 4

n = 200:
199 is absent → start of a sequence
201 is absent → length = 1
longest = max(4, 1) = 4
```

### Final frame — Return the answer

```text
Longest sequence: 1 → 2 → 3 → 4

Answer = 4 🎉
```

---

## 🔍 Complexity analysis

Let `n` be the number of elements in `nums`.

| Operation | Time complexity | Auxiliary space |
|---|---:|---:|
| Build `numset = set(nums)` | `O(n)` average | `O(n)` |
| Iterate over the set | `O(n)` | `O(1)` |
| Expand sequences | `O(n)` total average | `O(1)` |
| **Overall** | **`O(n)` average** | **`O(n)`** |

**Why is sequence expansion linear overall?**

Although the `while` loop is nested inside the `for` loop, the algorithm expands only from sequence beginnings. Each distinct number belongs to one consecutive sequence and is reached by forward expansion at most once. Therefore, the total number of successful membership checks across all expansions is `O(n)`, not `O(n²)`.

Hash-set membership is `O(1)` on average; pathological hash collisions can affect theoretical worst-case behavior. The standard LeetCode complexity analysis is **`O(n)` average time and `O(n)` space**.

---

## ⚖️ Brute force vs. optimal

| Feature | Brute force | Hash set |
|---|---|---|
| Data structure | Input list | Set |
| Sequence starts | Every input element | Only elements with no predecessor |
| Membership check | `O(n)` average for a list | `O(1)` average for a set |
| Overall time | `O(n²)` worst case | `O(n)` average |
| Auxiliary space | `O(1)` | `O(n)` |
| Meets required linear-time target? | No | Yes |

---

## 🧪 Edge cases to remember

| Input | Output | Reason |
|---|---:|---|
| `[]` | `0` | No elements exist |
| `[5]` | `1` | One element forms a sequence of length one |
| `[2, 2, 2]` | `1` | Duplicates are removed by the set |
| `[1, 2, 0, 1]` | `3` | Longest sequence is `0, 1, 2` |
| `[9, 1, 4, 7, 3, -1, 0, 5, 8, -2, 6]` | `7` | Longest sequence is `-2` through `4` |

---

## 🧠 Interview takeaway

The key is not merely using a set. It is **using the predecessor check to identify sequence beginnings**.

- Convert the input into a set.
- Ignore values that have a predecessor.
- Expand only from sequence starts.
- Track the maximum sequence length.

This avoids sorting and prevents repeated sequence scans, achieving **`O(n)` average time with `O(n)` auxiliary space**.

<div align="center">

### Keep solving. Keep learning. Keep improving. 🚀

**LeetCode 128 · Longest Consecutive Sequence · Python 3**

</div>