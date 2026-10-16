# 🎯 LeetCode 857 — Minimum Cost to Hire K Workers

![LeetCode](https://img.shields.io/badge/LeetCode-857-orange?logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)
![Language](https://img.shields.io/badge/Language-Python%203-blue?logo=python)
![Algorithm](https://img.shields.io/badge/Algorithm-Greedy%20%2B%20Heap-success)

> 💡 **Goal:** Hire exactly `k` workers at the minimum possible total cost while paying every hired worker according to the same wage-to-quality ratio.

---

## 📌 Problem Summary

You are given two arrays:

- `quality[i]`: the quality of worker `i`.
- `wage[i]`: the minimum wage worker `i` is willing to accept.
- `k`: the exact number of workers to hire.

Every selected worker must be paid at least their minimum wage, and all selected workers must receive the same amount per unit of quality.

Return the minimum total cost to hire exactly `k` workers.

---

## 🧠 The Key Insight

For each worker, calculate their minimum wage-to-quality ratio:

\[
r_i = \frac{wage[i]}{quality[i]}
\]

If the selected group is paid using a common ratio `r`, the total cost is:

\[
\text{Cost} = r \times \sum \text{quality of selected workers}
\]

The common ratio must be at least the largest ratio among the selected workers. Therefore, when workers are sorted by ratio, the current worker's ratio can be used as the common ratio for a candidate group.

✨ **Greedy idea:** For each possible common ratio, keep the `k` smallest qualities among the workers considered so far. Smaller total quality means a smaller total payment at that ratio.

---

## 🐢 Brute-Force Approach

### 💭 Idea

Try every possible group of exactly `k` workers:

1. Generate each combination of `k` workers.
2. Find the maximum wage-to-quality ratio in that group.
3. Multiply that ratio by the sum of the group's qualities.
4. Return the minimum cost across all groups.

### 🧪 Brute-Force Code

```python
from itertools import combinations
from typing import List

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        ans = float('inf')

        for group in combinations(range(n), k):
            ratio = max(wage[i] / quality[i] for i in group)
            total_quality = sum(quality[i] for i in group)
            cost = ratio * total_quality
            ans = min(ans, cost)

        return ans
```

### ⏱️ Brute-Force Complexity

- **Time:** `O(C(n, k) * k)` — each of the `C(n, k)` groups takes `O(k)` work to evaluate.
- **Extra space:** `O(k)` for the current combination, excluding implementation details of the combinations iterator.

⚠️ **Why is it slow?** The number of possible groups grows combinatorially. This method is useful for understanding the problem, but it is not suitable for large inputs.

---

## 🚀 Optimal Approach: Sorting + Max Heap

### 🔍 Step-by-Step Strategy

1. **Sort workers by ratio.** Store each worker as `(wage / quality, quality)`, sorted by increasing ratio.
2. **Use a max heap of qualities.** Python's `heapq` is a min heap, so push `-quality` to make the largest quality removable.
3. **Track the quality sum.** Add each worker's quality to `quality_sum`.
4. **Keep only `k` workers.** If the heap grows beyond `k`, remove the largest quality. Because heap values are negative, adding the popped value subtracts that quality from the sum.
5. **Calculate candidate costs.** Whenever the heap contains exactly `k` workers, calculate `quality_sum * ratio`.
6. **Keep the minimum.** Return the smallest candidate cost found.

### 🎬 Animation: How the Heap Changes

Imagine the workers have already been sorted by their wage-to-quality ratio. For each new worker, the heap keeps the `k` smallest qualities seen so far.

Example qualities in sorted-ratio order: `10, 20, 5`, with `k = 2`.

```text
Step 1: Add quality 10
Heap qualities: [10]
Workers kept:   1 / 2
Cost candidate: not yet (need k workers)

             ↓ Add quality 20

Step 2: Add quality 20
Heap qualities: [10, 20]
Workers kept:   2 / 2
Cost candidate: (10 + 20) × current ratio

             ↓ Add quality 5

Step 3: Add quality 5
Temporary qualities: [10, 20, 5]
Heap size exceeds k, so remove the largest quality: 20

After removal:
Heap qualities: [5, 10]
Workers kept:   2 / 2
Cost candidate: (5 + 10) × current ratio
```

🏁 **Result:** At each ratio, the heap gives the smallest total quality possible among the workers processed so far. The algorithm compares the candidate costs and keeps the minimum.

> Note: The animation illustrates the heap's selection logic. The actual heap stores negative qualities, and each candidate uses the current worker's ratio.

---

## ✅ Optimal Python 3 Solution

```python
import heapq
from typing import List

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted((w / q, q) for q, w in zip(quality, wage))

        max_heap = []
        quality_sum = 0
        ans = float('inf')

        for ratio, q in workers:
            heapq.heappush(max_heap, -q)
            quality_sum += q

            if len(max_heap) > k:
                quality_sum += heapq.heappop(max_heap)

            if len(max_heap) == k:
                ans = min(ans, quality_sum * ratio)

        return ans
```

---

## ⏱️ Complexity Analysis

Let `n` be the number of workers and `k` be the number to hire.

| Operation | Time Complexity |
|---|---:|
| Build worker ratio pairs | `O(n)` |
| Sort workers by ratio | `O(n log n)` |
| Heap insertions and removals | `O(n log k)` |
| Evaluate candidate costs | `O(n)` |
| **Overall** | **`O(n log n)`** |

- **Time complexity:** `O(n log n)`, dominated by sorting.
- **Auxiliary space complexity:** `O(n)` for the sorted worker list, plus `O(k)` for the heap. Overall, this is `O(n)`.

---

## 💎 Tips, Tricks & Hints

- 🧮 **Think in ratios, not individual wages.** The highest ratio in a chosen group determines the common payment ratio.
- 📈 **Sort by `wage / quality`.** This lets the current ratio act as the candidate group's common ratio.
- 🏋️ **Remove the largest quality.** For a fixed ratio, the smallest total quality produces the smallest cost.
- 🐍 **Simulate a max heap with negative values.** `heapq` is a min heap, so `-q` makes the largest original quality appear first when popped.
- ➕ **Update the sum carefully.** Since the popped heap value is negative, `quality_sum += heapq.heappop(max_heap)` subtracts the removed worker's positive quality.
- 🎯 **Evaluate only when heap size equals `k`.** A candidate group must contain exactly `k` workers.
- ⚠️ **Do not use the current ratio before sorting.** The greedy argument depends on processing ratios in ascending order.
- 🧠 **Remember the formula:** `cost = current_ratio * quality_sum`.

---

## 🧾 Quick Revision

```text
Sort workers by wage / quality
            ↓
Add each quality to a max heap
            ↓
If heap size > k, remove largest quality
            ↓
If heap size == k:
    cost = current ratio × quality sum
            ↓
Return the minimum candidate cost
```

### 📚 Concepts Used

- Greedy Algorithm
- Sorting
- Priority Queue / Heap
- Ratio-Based Optimization

### 🏁 Final Takeaway

The brute-force method checks every possible group, which becomes too expensive as the input grows. The optimal solution sorts workers by wage-to-quality ratio and uses a max heap to maintain the `k` smallest qualities. This reduces the time complexity to **`O(n log n)`** while preserving the minimum-cost result.

Happy coding, and keep building those algorithmic instincts! 🎉
