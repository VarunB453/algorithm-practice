<div align="center">

# 🎯 LeetCode 15 — 3Sum

### 🐍 Python 3 | From Brute Force to Two Pointers

**Find all unique triplets whose sum is zero. One problem, two approaches, and a smarter way to search!**

![LeetCode](https://img.shields.io/badge/LeetCode-15-orange?logo=leetcode&logoColor=white)
![Language](https://img.shields.io/badge/Language-Python%203-blue?logo=python&logoColor=white)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)
![Technique](https://img.shields.io/badge/Technique-Sorting%20%2B%20Two%20Pointers-success)

</div>

---

## 🧩 Problem Statement

Given an integer array `nums`, return **all unique triplets** `[nums[i], nums[j], nums[k]]` such that:

- `i`, `j`, and `k` are distinct indices.
- `nums[i] + nums[j] + nums[k] == 0`.
- The answer must not contain duplicate triplets.

**Example**

```text
Input:  nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]
```

The order of triplets in the output does not matter.

## 🐢 Approach 1: Brute Force

### 💡 Idea

Check every possible combination of three different indices. Whenever their values sum to zero, add the triplet to the answer if it has not already been included.

### Python 3 solution

```python
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = set()

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.add(tuple(sorted(
                            [nums[i], nums[j], nums[k]]
                        )))

        return [list(triplet) for triplet in result]
```

### 🔍 How it works

1. The three nested loops enumerate every index combination with `i < j < k`.
2. The sum is checked against zero.
3. Sorting each valid triplet and storing it as a tuple lets a set remove duplicate triplets.
4. Convert the set of tuples into the required list-of-lists output.

### ⏱️ Complexity

- **Time:** \(O(n^3)\) triplet checks, plus the cost of storing and hashing valid triplets. The simple upper-bound analysis is commonly stated as **\(O(n^3)\)**, assuming set operations take expected constant time.
- **Auxiliary space:** Up to \(O(u)\) for the set of unique triplets, where \(u\) is the number of unique results. The returned output also occupies space.

> ⚠️ **Why improve it?** Three nested loops become expensive as the input grows. Sorting once enables a more efficient search.

---

## 🧠 Optimization clues

Before reading the optimal solution, consider these questions:

- **Can sorting help?** After sorting, the values are in increasing order.
- **What does the sum tell us?** If the sum is too small, move the left pointer right to increase it. If it is too large, move the right pointer left to decrease it.
- **How can duplicates be avoided?** Skip repeated fixed values, then skip repeated left and right values after finding a valid triplet.
- **When can the outer loop stop early?** If the fixed value is positive, every value to its right is also positive, so a zero sum is impossible.

These observations lead to the **sorting + two-pointer** technique.

## 🚀 Approach 2: Optimal Solution — Sorting + Two Pointers

### 💡 Core idea

Sort the array. Fix one value at index `i`, then use two pointers to find pairs in the remaining suffix whose sum is `-nums[i]`.

### Python 3 solution

```python
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):
            # All later values are >= nums[i].
            # If nums[i] is positive, a zero sum is impossible.
            if nums[i] > 0:
                break

            # Avoid repeating the same fixed value.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([
                        nums[i], nums[left], nums[right]
                    ])
                    left += 1
                    right -= 1

                    # Skip duplicate pair values.
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    # The sum is too small: increase it.
                    left += 1
                else:
                    # The sum is too large: decrease it.
                    right -= 1

        return result
```

### 🧭 Step-by-step walkthrough

Use the example:

```text
nums = [-1, 0, 1, 2, -1, -4]
```

**1. Sort the array**

```text
[-4, -1, -1, 0, 1, 2]
```

**2. Fix `nums[i] = -4`**

```text
i = -4, left = -1, right = 2
sum = -4 + (-1) + 2 = -3
```

The sum is too small, so move `left` to the right. The remaining pairs cannot compensate for `-4`, so this fixed value produces no solution.

**3. Fix the first `-1`**

```text
[-4, -1, -1, 0, 1, 2]
      i   L           R
```

- `-1 + (-1) + 2 = 0` → record `[-1, -1, 2]`.
- Move both pointers inward.
- `-1 + 0 + 1 = 0` → record `[-1, 0, 1]`.
- Skip repeated values so the same triplet is not added again.

**4. Finish the scan**

When `i` reaches a positive value, stop: all values from that position onward are positive, so no zero-sum triplet can be formed.

### 🎞️ Pointer animation (frame-by-frame)

The following frames show the key pointer movements for the fixed value `-1`. Read them in order; `i` stays fixed while `L` and `R` move inward.

<details>
<summary>▶️ Frame 1 — Start the search</summary>

```text
Values:  -4   -1   -1    0    1    2
              i    L              R

Sum = -1 + -1 + 2 = 0
Action: Record [-1, -1, 2], then move L right and R left.
```

</details>

<details>
<summary>▶️ Frame 2 — Check the next pair</summary>

```text
Values:  -4   -1   -1    0    1    2
              i         L    R

Sum = -1 + 0 + 1 = 0
Action: Record [-1, 0, 1], then move both pointers inward.
```

</details>

<details>
<summary>▶️ Frame 3 — Finish this fixed value</summary>

```text
Values:  -4   -1   -1    0    1    2
              i              L/R

Action: The pointers meet; this scan is complete.
```

</details>

> 🎬 This is a text-based, step-by-step animation: expand each frame to follow the search. It illustrates the pointer state transitions without requiring JavaScript or an external animation file.

---

## 🧰 Why the optimal solution works

### 1. Sorting enables directional movement

For a fixed `nums[i]`, the left and right pointers point to the smallest and largest remaining values.

- If `total < 0`, the sum must increase. Moving `left` right is the useful direction.
- If `total > 0`, the sum must decrease. Moving `right` left is the useful direction.
- If `total == 0`, a valid triplet has been found.

Because the array is sorted, each pointer movement safely eliminates pairs that cannot produce the target for the current pointer configuration.

### 2. Duplicate skipping preserves uniqueness

- **Fixed value:** `if i > 0 and nums[i] == nums[i - 1]: continue`
- **Left value:** after a match, skip values equal to the previous left value.
- **Right value:** after a match, skip values equal to the next right value.

This avoids generating the same value-triplet multiple times.

### 3. Early termination saves work

Once `nums[i] > 0`, all values to its right are positive or equal to a positive number. Their sum cannot be zero, so the outer loop can stop.

## 📊 Complexity comparison

Let `n` be the length of `nums`, and `u` the number of unique triplets returned.

| Approach | Time complexity | Extra space (excluding output) |
|---|---:|---:|
| Brute force | \(O(n^3)\) expected, with set de-duplication | \(O(u)\) for stored results |
| Sorting + two pointers | \(O(n^2)\) after sorting; sorting is \(O(n \log n)\) | \(O(1)\) auxiliary space beyond the output, depending on the sorting implementation |

**Important:** The optimal implementation sorts `nums` in place, so it mutates the input list. Python's sorting implementation may use additional temporary memory; therefore, \(O(1)\) describes the conventional auxiliary-space analysis for the two-pointer scan, not a strict guarantee about Python's sort.

## 🧠 Interview tips and common pitfalls

- Do not return every matching index combination: the task requires unique **value-triplets**.
- Do not forget `left < right`; the three selected indices must be distinct.
- Skip duplicates after a match, not before checking whether a valid pair exists.
- The fixed-value duplicate check belongs before the two-pointer scan.
- Sorting changes the input list. If the original order must be preserved, work on a copy: `nums = sorted(nums)`.
- The output order is not important, but each triplet should be in non-decreasing order.

## 🧪 Edge cases to test

| Input | Expected output |
|---|---|
| `[]` | `[]` |
| `[0]` | `[]` |
| `[0, 0, 0]` | `[[0, 0, 0]]` |
| `[0, 0, 0, 0]` | `[[0, 0, 0]]` |
| `[1, 2, -2, -1]` | `[]` |
| `[-1, 0, 1, 2, -1, -4]` | `[[-1, -1, 2], [-1, 0, 1]]` (order may vary) |

## 🏁 Final takeaway

The key transformation is:

**Three nested loops → sort + fix one value + two pointers.**

This reduces the search from cubic time to **\(O(n^2)\)** while duplicate skipping ensures that each valid triplet appears only once.

<div align="center">

### 🌟 Sort smart. Move with purpose. Skip duplicates. 🌟

*Happy LeetCoding!*

</div>
