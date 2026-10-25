# 🔍 LeetCode 217: Contains Duplicate — Python 3

> **Pattern:** Hash Set · **Difficulty:** Easy  
> **Goal:** Return `True` if any value appears at least twice; otherwise return `False`. 🚀

---

## 🎯 Problem intuition

Given an integer list `nums`, determine whether the list contains a duplicate.

**Example 1**

```python
nums = [1, 2, 3, 1]
# Output: True
```

The number `1` appears twice, so a duplicate exists.

**Example 2**

```python
nums = [1, 2, 3, 4]
# Output: False
```

Every value appears only once.

**Example 3**

```python
nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
# Output: True
```

---

## 🐢 1. Brute-force solution

A direct method compares every number with the numbers that come after it. If any pair matches, return `True`.

```python
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True

        return False
```

### Complexity

- **Time:** `O(n²)` in the worst case, because many pairs may need to be compared.
- **Auxiliary space:** `O(1)`, because the algorithm uses only a few variables.
- **Best case:** `O(1)` when a duplicate is found immediately.

This approach is easy to understand, but checking every pair becomes expensive for large lists.

---

## 💡 2. Optimal solution: use a set

Python's `set` stores unique values. When a value appears more than once in `nums`, the set removes the repeated occurrence.

The provided one-liner compares the list's length with the set's length:

```python
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
```

### 🧠 Why does it work?

- `len(nums)` counts **every element**, including duplicates.
- `len(set(nums))` counts **distinct values only**.
- If the lengths differ, at least one duplicate must exist.

For example:

```python
nums = [1, 2, 3, 1]

len(nums)       # 4
len(set(nums))  # 3

4 != 3          # True 🎉
```

### ⏱️ Complexity analysis

Let `n` be the number of elements in `nums`.

| Metric | Complexity | Explanation |
|---|---:|---|
| Time | **`O(n)` average** | Building the set takes linear time on average. |
| Auxiliary space | **`O(n)`** | The set can store up to `n` distinct values. |
| Worst-case time | Typically described as `O(n²)` under pathological hash-collision assumptions | Ordinary interview analysis uses the average-case `O(n)` bound for Python sets. |

**Why is this optimal for the usual interview solution?** It avoids the quadratic pair-by-pair comparison and uses Python's built-in hash set for efficient membership and uniqueness handling. It is a concise, idiomatic solution.

---

## 🎬 3. Mini animation: watch duplicates disappear

Start with the list:

```text
nums = [1, 2, 3, 1]
```

**Frame 1 — begin with an empty set**

```text
List: [1, 2, 3, 1]
Set:  {}
```

**Frame 2 — keep the first `1`**

```text
List: [1, 2, 3, 1]
Set:  {1}
```

**Frame 3 — add `2` and `3`**

```text
List: [1, 2, 3, 1]
Set:  {1, 2, 3}
```

**Frame 4 — the repeated `1` adds no new unique value**

```text
List length: 4
Set length:  3
              ↓
          4 != 3
              ↓
       containsDuplicate = True 🎉
```

The animation illustrates the key idea: the list preserves repeated elements, while the set represents only distinct values.

---

## ⚡ 4. Tips, tricks, and interview hints

- **Hint 1 — Ask what a duplicate changes.** A duplicate increases the list length but does not increase the number of distinct values.
- **Hint 2 — Think of a hash set.** Sets are designed to keep unique items and support efficient average-case operations.
- **Hint 3 — Use the length comparison.** `len(nums) != len(set(nums))` expresses the entire check in one line.
- **Hint 4 — Return early when scanning.** If using a set-based loop, return `True` as soon as a value is already present.
- **Hint 5 — Remember the space trade-off.** The set uses extra memory to improve time complexity.
- **Hint 6 — Test boundary cases.** Empty lists and one-element lists contain no duplicates; repeated values such as `[7, 7]` do.

### Alternative optimal-style implementation

This version checks values as they arrive and can stop as soon as it finds a duplicate:

```python
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
```

**Complexity:** `O(n)` average time and `O(n)` auxiliary space. This version may stop early, whereas `len(nums) != len(set(nums))` constructs the set from the entire list.

---

## 🧪 Quick test checklist

- [ ] `[]` → `False`
- [ ] `[1]` → `False`
- [ ] `[1, 2, 3, 4]` → `False`
- [ ] `[1, 2, 3, 1]` → `True`
- [ ] `[7, 7]` → `True`
- [ ] `[-1, 0, -1]` → `True`

---

## 🏁 Takeaway

The brute-force approach compares pairs and takes **`O(n²)` time** in the worst case. The set-based solution is the clean, efficient choice for typical interview constraints: **`O(n)` average time** and **`O(n)` auxiliary space**.

One line, one set, one duplicate check. Happy coding! 🐍✨
