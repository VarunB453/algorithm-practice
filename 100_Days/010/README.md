# LeetCode 238 — Product of Array Except Self

> **Python 3 • Prefix + Suffix Products • Beginner Friendly 🚀**

The goal of **LeetCode 238** is to return an array where each position contains the product of **every number except the number at that position**! 🧩✨

We need to solve it **without using division** and in **O(n)** time. 🎯

---

## 🧠 Understanding the Problem

Given an integer array `nums`, return an array `answer` such that:

```text
answer[i] = product of every nums[j] where j != i
```

For example:

```text
Input:  nums = [1, 2, 3, 4]

Output: [24, 12, 8, 6]
```

Why?

```text
index 0 → 2 × 3 × 4 = 24
index 1 → 1 × 3 × 4 = 12
index 2 → 1 × 2 × 4 = 8
index 3 → 1 × 2 × 3 = 6
```

🎯 We need to calculate all of these efficiently!

---

## 🚫 Important Constraint

A tempting solution is:

```text
product of everything
        ÷
nums[i]
```

But the problem says:

> ❌ **Do not use division.**

There is also a tricky case with zeros:

```text
[1, 2, 0, 4]
```

So we need another idea. 💡

---

# 🐢 Brute-Force Solution

The most straightforward approach is:

> For every index, multiply every other element. 🔄

For example:

```text
nums = [1, 2, 3, 4]

For index 0:
2 × 3 × 4 = 24

For index 1:
1 × 3 × 4 = 12

For index 2:
1 × 2 × 4 = 8

For index 3:
1 × 2 × 3 = 6
```

### Python 3

```python
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n

        for i in range(n):
            product = 1

            for j in range(n):
                if i != j:
                    product *= nums[j]

            answer[i] = product

        return answer
```

### Why is this slow? 🐢

For every element, we scan the entire array again.

If there are `n` elements:

```text
n elements
   ×
n work for each element
   ↓
O(n²)
```

### Complexity

- **Time:** `O(n²)` ⏳
- **Space:** `O(n)` 💾 for the output array

It works, but we can do MUCH better! 🚀

---

# 💡 Optimization Tips, Tricks & Hints

## Hint 1 — Split the product! ✂️

For every index `i`:

```text
answer[i]

= product of everything on the LEFT
  ×
  product of everything on the RIGHT
```

For:

```text
[1, 2, 3, 4]
```

At index `2`:

```text
[1, 2] | [3] | [4]
         ↑
       index 2

left  = 1 × 2 = 2
right = 4

answer[2] = 2 × 4 = 8
```

🎯 This is the key observation!

---

## Hint 2 — Think Prefix + Suffix! 🧠

We can calculate:

```text
PREFIX → product of everything before i
SUFFIX → product of everything after i
```

Then:

```text
answer[i] = prefix[i] × suffix[i]
```

✨ We don't actually need two arrays.

We can store the prefix product directly inside `answer`.

---

## Hint 3 — First Pass: Prefix Products ⬅️

For:

```text
nums = [1, 2, 3, 4]
```

Build:

```text
answer = [1, 1, 2, 6]
```

Animation:

```text
Start:
answer = [1, 1, 1, 1]

i = 0
prefix = 1
answer[0] = 1
prefix *= 1

        ↓

[1, 1, 1, 1]

i = 1
answer[1] = 1
prefix *= 2

        ↓

[1, 1, 1, 1]

i = 2
answer[2] = 1 × 2 = 2
prefix *= 3

        ↓

[1, 1, 2, 1]

i = 3
answer[3] = 1 × 2 × 3 = 6

        ↓

[1, 1, 2, 6] 🎯
```

Notice:

```text
answer[i] = product of everything LEFT of i
```

---

## Hint 4 — Second Pass: Suffix Products ➡️

Now scan from right to left.

For:

```text
nums = [1, 2, 3, 4]
```

We maintain:

```text
suffix = product of everything RIGHT of i
```

At each position:

```text
answer[i] *= suffix
```

Then update:

```text
suffix *= nums[i]
```

✨ This gives us the final answer!

---

# 🎬 The Big Animation

Let's visualize the whole algorithm:

```text
nums:
[ 1   2   3   4 ]
  ↑

PREFIX PASS ⬅️

i = 0
left product = 1

[ 1   2   3   4 ]
  ↑
answer = [1, 1, 1, 1]

        ↓

i = 1
left product = 1

[ 1   2   3   4 ]
      ↑
answer = [1, 1, 1, 1]

        ↓

i = 2
left product = 1 × 2 = 2

[ 1   2   3   4 ]
          ↑
answer = [1, 1, 2, 1]

        ↓

i = 3
left product = 1 × 2 × 3 = 6

[ 1   2   3   4 ]
              ↑
answer = [1, 1, 2, 6]


              ⬇️

SUFFIX PASS ➡️

Start from the RIGHT:

[ 1   2   3   4 ]
              ↑
suffix = 1

answer[3] = 6 × 1 = 6
suffix = 4

        ↓

[ 1   2   3   4 ]
          ↑
answer[2] = 2 × 4 = 8
suffix = 4 × 3 = 12

        ↓

[ 1   2   3   4 ]
      ↑
answer[1] = 1 × 12 = 12
suffix = 12 × 2 = 24

        ↓

[ 1   2   3   4 ]
  ↑
answer[0] = 1 × 24 = 24

        🎉

FINAL ANSWER:

[ 24   12   8   6 ]
```

---

# 🚀 Optimal Solution — Prefix + Suffix

Here is the clean Python 3 solution:

```python
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n

        # Prefix products
        prefix = 1

        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Suffix products
        suffix = 1

        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
```

---

# 🔎 Dry Run

Let's use:

```text
nums = [1, 2, 3, 4]
```

### Step 1️⃣ — Prefix Pass

```text
prefix = 1

i = 0:
answer[0] = 1
prefix = 1

i = 1:
answer[1] = 1
prefix = 2

i = 2:
answer[2] = 2
prefix = 6

i = 3:
answer[3] = 6
prefix = 24
```

Now:

```text
answer = [1, 1, 2, 6]
```

🎯 Each position contains the product of everything to its left!

---

### Step 2️⃣ — Suffix Pass

Start:

```text
suffix = 1
```

Move right → left:

```text
i = 3:

answer[3] = 6 × 1
          = 6

suffix = 1 × 4
       = 4
```

Then:

```text
i = 2:

answer[2] = 2 × 4
          = 8

suffix = 4 × 3
       = 12
```

Then:

```text
i = 1:

answer[1] = 1 × 12
          = 12

suffix = 12 × 2
       = 24
```

Finally:

```text
i = 0:

answer[0] = 1 × 24
          = 24
```

🎉 Final result:

```text
[24, 12, 8, 6]
```

---

# 🧠 Why the Optimal Solution Works

The magic is that every answer is:

```text
LEFT PRODUCT × RIGHT PRODUCT
```

For example, at index `2`:

```text
nums = [1, 2, 3, 4]
             ↑

LEFT:
1 × 2 = 2

RIGHT:
4

ANSWER:
2 × 4 = 8
```

So:

```text
answer[i]
    =
product before i
    ×
product after i
```

The first loop builds the **left product**.

The second loop builds the **right product**.

Together:

```text
PREFIX + SUFFIX
       ↓
   🎯 ANSWER
```

---

# 🎯 Why We Don't Need Extra Arrays

A beginner solution might create:

```text
prefix[]
suffix[]
answer[]
```

That works, but it uses extra memory.

Instead, we put the prefix products directly into:

```python
answer
```

Then we multiply the suffix product into the same array.

So we only need:

```text
answer[]
prefix
suffix
```

✨ That's why the extra auxiliary space is `O(1)`.

---

# ⚡ Zero Handling

A beautiful advantage of this approach is that **we don't need special zero logic**. 🎉

Example:

```text
nums = [1, 2, 0, 4]
```

The algorithm naturally produces:

```text
[0, 0, 8, 0]
```

Because:

```text
index 0 → 2 × 0 × 4 = 0
index 1 → 1 × 0 × 4 = 0
index 2 → 1 × 2 × 4 = 8
index 3 → 1 × 2 × 0 = 0
```

No division. No special cases. 🚀

---

# 📊 Complexity

Let:

```text
n = length of nums
```

| Approach | Time | Extra Space |
|---|---:|---:|
| 🐢 Brute Force | `O(n²)` | `O(1)`* |
| 🚀 Prefix + Suffix | `O(n)` | `O(1)`* |

`*` The output array is not counted as extra space.

### Optimal Complexity

- **Time:** `O(n)` ⏱️
- **Extra Space:** `O(1)` 💾
- **Output Space:** `O(n)` for the returned array

Why `O(n)` time?

```text
First pass  → O(n)
Second pass → O(n)

O(n) + O(n)
    ↓
  O(n)
```

🎉 We visit the array only twice!

---

# 🐢 Brute Force vs 🚀 Optimal

```text
🐢 BRUTE FORCE

For every index
      ↓
Scan the whole array
      ↓
Calculate product
      ↓
Repeat...

O(n²) 😵‍💫
```

Versus:

```text
🚀 OPTIMAL

LEFT → RIGHT
    ↓
Build prefix products
    ↓
RIGHT → LEFT
    ↓
Multiply suffix products
    ↓
🎯 Final answer

O(n) ⚡
```

---

# 🧩 Pattern to Remember

LeetCode 238 is a classic example of:

```text
PREFIX + SUFFIX
```

Whenever you see a problem involving:

```text
Everything BEFORE me
+
Everything AFTER me
```

💡 Think:

```text
⬅️ PREFIX
+
➡️ SUFFIX
```

This pattern is extremely useful in array problems! 🧠✨

---

# 🏆 Final Takeaway

The most important idea is:

> **Don't calculate each answer from scratch. Build the left products once, then multiply the right products once.** 🎯

Remember these three superpowers:

```text
⬅️ PREFIX PRODUCTS
➡️ SUFFIX PRODUCTS
⚡ O(n) TIME
```

And the biggest trick:

```text
✨ Use the output array to store prefix products.
✨ Reuse it during the suffix pass.
✨ No division required!
```

---

# 🎉 Happy Coding!

```text
        ⬅️ PREFIX
           |
           ↓
     [ 1  1  2  6 ]
           |
           ↓
       ➡️ SUFFIX
           |
           ↓
     [24 12  8  6]
           |
           ↓
          🎯
       SUCCESS!
          🎉
```

**Think in prefixes, scan with purpose, and keep coding! 😄🐍💻🚀**
