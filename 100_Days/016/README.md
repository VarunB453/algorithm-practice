# 🚀 LeetCode 56 — Merge Intervals (Python 3)

> Merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input.

**Problem:** [LeetCode 56 — Merge Intervals](https://leetcode.com/problems/merge-intervals/)  
**Topic:** Arrays · Sorting · Greedy  
**Language:** Python 3

---

## 🌟 Intuition

Imagine each interval as a time slot on a calendar. If two slots overlap, combine them into one larger slot. Sorting by the starting point puts intervals in an order that makes this easy: after sorting, only the **last interval in the result** can overlap with the current interval.

For example:

```text
Input:  [[1,3], [2,6], [8,10], [15,18]]
Output: [[1,6], [8,10], [15,18]]
```

The intervals `[1,3]` and `[2,6]` overlap, so they merge into `[1,6]`. The remaining intervals do not overlap.

## 🐢 1. Brute-Force Approach

A straightforward approach repeatedly compares intervals and merges any overlapping pair. After a merge, scan again because the enlarged interval might overlap with another interval. Continue until a complete pass makes no changes.

Two intervals `[a, b]` and `[c, d]` overlap when:

```python
a <= d and c <= b
```

A merged interval becomes:

```python
[min(a, c), max(b, d)]
```

### Brute-force reference implementation

```python
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = [interval[:] for interval in intervals]
        changed = True

        while changed:
            changed = False
            merged = []
            used = [False] * len(intervals)

            for i in range(len(intervals)):
                if used[i]:
                    continue

                current_start, current_end = intervals[i]

                for j in range(i + 1, len(intervals)):
                    if used[j]:
                        continue

                    other_start, other_end = intervals[j]

                    if current_start <= other_end and other_start <= current_end:
                        current_start = min(current_start, other_start)
                        current_end = max(current_end, other_end)
                        used[j] = True
                        changed = True

                merged.append([current_start, current_end])

            intervals = merged

        return sorted(intervals, key=lambda x: x[0])
```

### Complexity

- **Time:** \(O(n^3)\) in this repeated-scan implementation in the worst case, since multiple passes may be needed and each pass compares pairs.
- **Auxiliary space:** \(O(n)\) for the temporary lists, excluding the input copy; the copied intervals themselves require \(O(n)\).

This solution is useful for understanding the overlap condition, but it is unnecessarily complicated and slow. Sorting followed by one linear scan is preferable.

---

## ⚡ 2. Optimal Approach — Sort + Greedy Merge

### Key insight

1. Sort intervals by their starting values.
2. If the result is empty, add the current interval.
3. Otherwise, compare the current start with the end of the last merged interval.
4. If `start <= result[-1][1]`, the intervals overlap (touching endpoints count as overlap for this problem). Extend the previous interval's end with `max(previous_end, end)`.
5. If they do not overlap, append the current interval as a new interval.

### ✅ Python 3 solution

```python
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []

        for start, end in intervals:
            if result and start <= result[-1][1]:
                result[-1][1] = max(result[-1][1], end)
            else:
                result.append([start, end])

        return result
```

### ⏱️ Complexity analysis

Let \(n\) be the number of intervals.

| Resource | Complexity | Reason |
|---|---:|---|
| Time | **\(O(n \log n)\)** | Sorting dominates; the merge scan is \(O(n)\). |
| Auxiliary space | **\(O(1)\)** excluding the output and sorting implementation details | The scan uses constant extra variables, and sorting is in place in Python. |
| Output space | **\(O(n)\)** | In the worst case, every interval remains separate. |

**Python note:** Python's `list.sort()` sorts the input list in place. The returned result is a separate list. If counting Python's internal Timsort workspace, sorting can use up to \(O(n)\) auxiliary space, so a conservative total auxiliary-space statement is **\(O(n)\)**.

---

## 🎬 3. Merge Animation (Step by Step)

Example input:

```text
[[1,3], [2,6], [8,10], [15,18]]
```

First, sort by start:

```text
[1,3]  [2,6]  [8,10]  [15,18]
```

<details>
<summary>▶️ Frame 1 — Start with [1,3]</summary>

```text
Result: [[1,3]]
         └── first interval
```

There is no previous interval, so add `[1,3]`.
</details>

<details>
<summary>▶️ Frame 2 — Merge [2,6]</summary>

```text
Current: [2,6]
Last:    [1,3]

2 <= 3  ✅ overlap!
Merge:   [1, max(3,6)] = [1,6]

Result: [[1,6]]
```

</details>

<details>
<summary>▶️ Frame 3 — Process [8,10]</summary>

```text
Current start: 8
Last end:      6

8 <= 6  ❌ no overlap

Result: [[1,6], [8,10]]
```

Add a new interval.
</details>

<details>
<summary>▶️ Frame 4 — Process [15,18]</summary>

```text
Current start: 15
Last end:      10

15 <= 10  ❌ no overlap

Result: [[1,6], [8,10], [15,18]]
```

🎉 Final answer reached!
</details>

### Visual timeline

```text
Input:    [---1---3]
              [---2------6]       [8---10]             [15---18]

Merged:   [-------1------6]       [8---10]             [15---18]
```

The brackets are illustrative; the numeric endpoints determine overlap.

---

## 🧠 Tips, Tricks & Interview Hints

- **Sort by start, not end.** This makes the current interval's start easy to compare with the end of the most recently merged interval.
- **Use `<=`, not `<`.** Under the problem's definition, `[1,4]` and `[4,5]` merge into `[1,5]`.
- **Use `max()` for the end.** Nested intervals can occur. For example, `[1,10]` followed by `[2,3]` must remain `[1,10]`, not shrink to `[1,3]`.
- **Only compare with the last result interval.** Sorting guarantees that earlier intervals cannot become newly relevant once the latest merged interval has been handled.
- **Mutability matters.** `intervals.sort(...)` modifies the input list. If the original input must be preserved, use `sorted(intervals, key=lambda x: x[0])`.
- **Empty input works naturally.** If `intervals` is empty, the loop does not run and the result is `[]`.
- **State the invariant in interviews.** After every iteration, `result` contains sorted, pairwise non-overlapping intervals representing all processed intervals.

## 🧪 Edge Cases to Test

| Input | Expected output |
|---|---|
| `[]` | `[]` |
| `[[1,4],[4,5]]` | `[[1,5]]` |
| `[[1,10],[2,3]]` | `[[1,10]]` |
| `[[1,2],[3,4]]` | `[[1,2],[3,4]]` |
| `[[1,4],[0,2],[3,5]]` | `[[0,5]]` |
| `[[1,4]]` | `[[1,4]]` |

## 🏁 Final Takeaway

**Sort first, then merge in one pass.** Sorting establishes the order; the greedy scan decides whether to extend the latest interval or start a new one.

**Optimal time:** \(O(n \log n)\)  
**Auxiliary space:** \(O(1)\) for the scan, excluding sorting workspace and output; conservatively \(O(n)\) including Python sorting workspace.  
**Output space:** \(O(n)\)

Keep calm, sort smart, and merge on! 🎯
