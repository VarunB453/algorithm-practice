# 💎 LeetCode 771: Jewels and Stones — Python 3

> **Pattern:** Hash Set · Membership Testing  
> **Difficulty:** Easy  
> **Goal:** Count how many stones are also jewels. Every character in `stones` represents one stone, and characters in `jewels` identify the types considered valuable. ✨

---

## 🧠 Problem intuition

You are given two strings:

- `jewels`: the characters that represent jewel types.
- `stones`: the characters representing the stones you own.

Return the number of characters in `stones` that also appear in `jewels`.

**Important:** Character matching is case-sensitive. For example, `'a'` and `'A'` are different characters.

### Example

```python
jewels = "aA"
stones = "aAAbbbb"
```

**Output**
```text
3
```

Why? The stones `'a'`, `'A'`, and `'A'` are jewels. The remaining characters are not.

---

## 🐢 1. Brute-force solution

### 💭 Idea

For every stone, scan the entire `jewels` string to see whether the stone matches any jewel character. If a match is found, increase the count.

```python
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0

        for stone in stones:
            for jewel in jewels:
                if stone == jewel:
                    count += 1
                    break

        return count
```

### ⏱️ Complexity

Let `J = len(jewels)` and `S = len(stones)`.

- **Time:** `O(J × S)` in the worst case, because each stone may be compared with every jewel.
- **Auxiliary space:** `O(1)`, because only a counter and loop variables are used.
- **Output space:** `O(1)`, because the answer is a single integer.

This solution is simple and correct, but repeated comparisons make it slower than necessary. 🔍

---

## 💡 2. Optimal solution: use a set

### 🚀 Key insight

A Python `set` stores unique characters and supports average-case `O(1)` membership checks. Convert `jewels` to a set once, then check each stone against it.

### ✨ Python 3 solution

```python
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        return sum(stone in jewel_set for stone in stones)
```

This is the same concise approach as:

```python
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set(jewels)
        return sum(c in s for c in stones)
```

### 🧩 How it works

1. `set(jewels)` builds a set of jewel characters.
2. `stone in jewel_set` evaluates to `True` if the current stone is a jewel, otherwise `False`.
3. In Python, `True` behaves like `1` and `False` like `0` in arithmetic.
4. `sum(...)` adds those results, giving the total number of jewel stones.

### ⏱️ Complexity

Let `J = len(jewels)` and `S = len(stones)`.

- **Time:** `O(J + S)` on average. Building the set takes `O(J)`, then checking all stones takes average `O(S)`.
- **Auxiliary space:** `O(J)` for the set of jewel characters.
- **Output space:** `O(1)` because the method returns one integer.

The set-based solution is optimal for the general approach: each jewel character must be processed to build the lookup structure, and each stone must be checked at least once. 💎

---

## 🎬 3. Mini animation: the jewel detector

Example:

```text
jewels = "aA"
stones = "aAAbbbb"
```

**Frame 1 — Build the jewel set**

```text
jewels:     a   A
             \ /
jewel_set:  { a, A }
```

**Frame 2 — Inspect each stone**

```text
Stone:      a   A   A   b   b   b   b
Is jewel?   ✓   ✓   ✓   ✗   ✗   ✗   ✗
```

**Frame 3 — Count the matches**

```text
✓ + ✓ + ✓ + ✗ + ✗ + ✗ + ✗
1 + 1 + 1 + 0 + 0 + 0 + 0 = 3
```

🎉 **Answer: `3`**

---

## 🧠 Tips, tricks, and hints

- **Hint 1:** Need to ask “Does this character exist in that collection?” Consider a `set`.
- **Hint 2:** Build the lookup structure once. Do not recreate it inside the loop.
- **Hint 3:** `sum(condition for item in items)` is a compact way to count how many items satisfy a condition.
- **Hint 4:** A set automatically removes duplicate jewel characters. This is safe because the task asks whether each stone's character is a jewel, not how many times that character appears in `jewels`.
- **Hint 5:** Do not convert `stones` to a set. Duplicate stones must each count separately.
- **Hint 6:** Matching is case-sensitive: `'a' != 'A'`.

### ⚖️ Quick comparison

| Approach | Time complexity | Auxiliary space | Main idea |
|---|---:|---:|---|
| Brute force | `O(J × S)` | `O(1)` | Compare every stone with every jewel |
| Set-based | `O(J + S)` average | `O(J)` | Fast membership lookup |

---

## 🏁 Final takeaway

The essential pattern is **set + membership test**. Whenever a problem repeatedly asks whether an item belongs to a collection, a set can replace repeated linear searches with average constant-time lookups.

Keep practising, keep spotting patterns, and keep collecting those LeetCode wins! 🌟💻
