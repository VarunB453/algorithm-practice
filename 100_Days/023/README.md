# 🧠 LeetCode 169 — Majority Element

<p align="center">
  <strong>LeetCode · Python 3 · Easy</strong><br>
  🔎 Count smartly. Cancel pairs. Find the majority!
</p>

---

## 📌 Problem Statement

Given an array `nums` of size `n`, return the **majority element**.

The majority element is the element that appears **more than** `⌊n / 2⌋` times. You may assume that the majority element always exists.

**Example**

```text
Input:  nums = [2,2,1,1,1,2,2]
Output: 2
```

Here, `2` appears four times in an array of length seven, and `4 > ⌊7 / 2⌋`.

---

## 🐢 1. Brute-Force Solution

### 💡 Idea

For every value, count how many times it appears. The first value whose frequency is greater than `n // 2` is the answer.

### 🧑‍💻 Python 3

```python
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        for num in nums:
            if nums.count(num) > n // 2:
                return num
```

### ⏱️ Complexity

- **Time:** `O(n²)` in the worst case. `nums.count(num)` takes `O(n)` and may be called for each element.
- **Auxiliary space:** `O(1)` — no additional data structure proportional to the input is created.

### ⚠️ Why improve it?

Repeatedly counting the same values wastes work. A frequency dictionary can reduce the expected time to `O(n)`, but it uses `O(n)` extra space. The next method achieves **linear time and constant auxiliary space**.

---

## 🚀 2. Optimal Solution — Boyer–Moore Voting Algorithm

### 💡 Core Insight

The majority element appears more than half the time. Imagine pairing each occurrence of a different value with one occurrence of the majority element. Since the majority has more occurrences than all other values combined, it cannot be completely cancelled.

The algorithm maintains:

- `candidate`: the current potential majority element.
- `count`: the candidate's balance.
- When `count == 0`, select the current number as the new candidate.
- If the current number equals the candidate, increment `count`; otherwise, decrement it.

### 🧑‍💻 Python 3 — Your Solution

```python
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate
```

### 🔍 Dry Run

Input: `nums = [2, 2, 1, 1, 1, 2, 2]`

| Step | Current number | Candidate | Count | Action |
|---:|---:|---:|---:|---|
| 1 | `2` | `2` | `1` | Start candidate |
| 2 | `2` | `2` | `2` | Match: increment |
| 3 | `1` | `2` | `1` | Different: decrement |
| 4 | `1` | `2` | `0` | Different: decrement |
| 5 | `1` | `1` | `1` | Reset candidate, then increment |
| 6 | `2` | `1` | `0` | Different: decrement |
| 7 | `2` | `2` | `1` | Reset candidate, then increment |

**Result: `2`**

### 🎞️ Step-by-Step “Animation”

Follow the candidate balance as the array is processed:

```text
Read 2  → Candidate: 2  | Count: 1   🟦
Read 2  → Candidate: 2  | Count: 2   🟦🟦
Read 1  → Candidate: 2  | Count: 1   🟦
Read 1  → Candidate: 2  | Count: 0   ⚖️ Cancelled
Read 1  → Candidate: 1  | Count: 1   🟨
Read 2  → Candidate: 1  | Count: 0   ⚖️ Cancelled
Read 2  → Candidate: 2  | Count: 1   🟦

Final candidate → 2 🎯
```

Each different value cancels one unit of the current candidate's balance. When the balance reaches zero, the next number starts a new candidate balance.

> **Important:** The final candidate is guaranteed to be the majority element because the problem guarantees that a majority exists. If that guarantee were absent, a second pass would be needed to verify the candidate's frequency.

### ⏱️ Complexity

- **Time:** `O(n)` — each element is processed once.
- **Auxiliary space:** `O(1)` — only `candidate` and `count` are maintained.

---

## 🧰 Interview Tips, Tricks & Hints

- **Hint 1:** A majority element occurs more than all other elements combined.
- **Hint 2:** Think about cancelling two different values. Can all copies of the majority be cancelled?
- **Hint 3:** Track only a candidate and its balance instead of storing every frequency.
- **Python tip:** `nums.count(x)` is `O(n)`. Calling it inside a loop can make a solution `O(n²)`.
- **Boundary condition:** Reset the candidate when `count == 0`, before comparing the current value.
- **Common mistake:** Use `count == 0`, not `count < 0`; the balance is maintained at zero or above by this procedure.
- **Complexity target:** Aim for `O(n)` time and `O(1)` auxiliary space.

---

## 🆚 Quick Comparison

| Approach | Time | Auxiliary space | Notes |
|---|---:|---:|---|
| Brute force with `count()` | `O(n²)` | `O(1)` | Simple, but repeats work |
| Frequency dictionary | `O(n)` expected | `O(n)` | Easy to reason about |
| **Boyer–Moore Voting** | **`O(n)`** | **`O(1)`** | **Optimal for this problem** |

---

## ✅ Final Takeaway

The Boyer–Moore Voting Algorithm solves **Majority Element** by keeping a candidate and cancelling out different values. Since the majority occurs more than half the time, it survives this cancellation process.

**Remember:** one pass, two variables, `O(n)` time, and `O(1)` auxiliary space. 🏆

---

<p align="center">
  ⭐ Keep practising · Recognize the pattern · Optimize with confidence ⭐
</p>
