# 🚀 LeetCode 228 — Summary Ranges (Python 3)

> **Goal:** Convert a sorted array of unique integers into the smallest set of consecutive ranges.  
> **Problem:** [LeetCode 228 — Summary Ranges](https://leetcode.com/problems/summary-ranges/)  
> **Language:** Python 3

---

## 🧠 Intuition

Walk through the array from left to right. Each number begins a new range unless the next number is exactly one greater. Keep extending the current range while consecutive numbers continue, then record either a single number or a range such as `2->5`.

Because the input is already sorted, there is no need to sort it or use extra data structures.

## 🐢 Brute-Force Approach

A straightforward approach starts at each unprocessed number and checks forward to find the end of its consecutive run. This is effectively the same scan used by the optimal solution for this problem: every element is visited only a constant number of times.

A genuinely less efficient alternative would repeatedly search ahead from each starting point without remembering the current position. That can revisit elements and take **O(n²)** time in the worst case, while offering no benefit.

### Brute-force-style Python 3

```python
from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i = 0

        while i < len(nums):
            start = nums[i]
            j = i

            # Scan forward to find the end of this consecutive range.
            while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
                j += 1

            if start == nums[j]:
                res.append(str(start))
            else:
                res.append(f"{start}->{nums[j]}")

            i = j + 1

        return res
```

**Complexity:** `O(n)` time and `O(1)` auxiliary space, excluding the output. This scan is already asymptotically optimal; there is no need to force a slower algorithm.

## 💡 Optimal Approach: One-Pass Scan

### Key idea

1. Set `start` to the first number in the current range.
2. Move `i` forward while the next number equals the current number plus one.
3. If the range contains one number, append that number as a string.
4. Otherwise, append it as `start->end`.
5. Continue from the next unprocessed number.

### ✨ Optimal Python 3 Solution

```python
from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i = 0

        while i < len(nums):
            start = nums[i]

            while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
                i += 1

            if start == nums[i]:
                res.append(str(start))
            else:
                res.append(f"{start}->{nums[i]}")

            i += 1

        return res
```

## 🎬 Animation: Follow the Pointer!

Example: `nums = [0, 1, 2, 4, 5, 7]`

```text
Step 1: Start at 0
        [0, 1, 2, 4, 5, 7]
         ^
        0 → 1 → 2 are consecutive
        Record: "0->2"

Step 2: Continue at 4
        [0, 1, 2, 4, 5, 7]
                  ^
        4 → 5 are consecutive; 7 breaks the run
        Record: "4->5"

Step 3: Continue at 7
        [0, 1, 2, 4, 5, 7]
                        ^
        No consecutive next value
        Record: "7"

Final answer: ["0->2", "4->5", "7"] 🎉
```

### 🧭 Pointer movement at a glance

```text
0 ──▶ 1 ──▶ 2   |   4 ──▶ 5   |   7
└──── "0->2" ───┘   └ "4->5" ┘     "7"
```

The pointer only moves forward. Once a number has been processed, it is never revisited.

## ⏱️ Complexity Analysis

Let `n = len(nums)` and `r` be the number of ranges in the output.

- **Time Complexity: `O(n)`** — each element is visited at most a constant number of times.
- **Auxiliary Space: `O(1)`** — only a few variables are used, excluding the result list.
- **Output Space: `O(r)`** — the result contains one string per range; formatting those strings also requires storage.

## 🧪 Quick Examples

| Input | Output |
|---|---|
| `[0, 1, 2, 4, 5, 7]` | `["0->2", "4->5", "7"]` |
| `[0, 2, 3, 4, 6, 8, 9]` | `["0", "2->4", "6", "8->9"]` |
| `[]` | `[]` |
| `[-1]` | `["-1"]` |

## 🏆 Tips, Tricks & Interview Hints

- **Use the sorted property.** Consecutive values appear next to one another, so a single scan is sufficient.
- **Check the boundary first.** `i + 1 < len(nums)` prevents indexing beyond the array.
- **Compare adjacent values.** `nums[i + 1] == nums[i] + 1` is the exact condition for extending a range.
- **Handle singletons.** When `start == nums[i]`, output only the number, not `x->x`.
- **Advance past the completed range.** The final `i += 1` moves to the next unprocessed element.
- **Do not sort.** LeetCode guarantees the input is sorted; sorting would add unnecessary `O(n log n)` time.
- **Empty input is naturally handled.** The loop never runs, so the answer is `[]`.

## ✅ Final Takeaway

The optimal solution is a clean **one-pass, `O(n)` scan** with constant auxiliary space. Each consecutive run becomes one output string, making the approach efficient, readable, and interview-friendly. Keep moving forward, close each range, and let the pointer do the work! 🚀

---
**Happy coding!** 💻✨
