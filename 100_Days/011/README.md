# 💧 LeetCode 42 — Trapping Rain Water

### 🏔️ Two Pointers • Brute Force → Optimal • Python

> 🌊 **Goal:** Given an array of heights, calculate how much rain water can be trapped between the bars.

---

# 🧠 Problem

You are given an array `height` where each element represents the height of a vertical bar.

After it rains, water can collect between taller bars.

### 🌧️ Example

```text
height = [4, 2, 0, 3, 2, 5]

                 🧱
                 🧱
🧱💧💧🧱💧🧱
🧱💧💧🧱💧🧱
🧱🧱💧🧱🧱🧱
🧱🧱💧🧱🧱🧱
────────────────────
  4  2  0  3  2  5

💧 Total Water = 9
```

The key idea is:

> 💡 Water above a bar depends on the **shorter boundary** on its left and right.

---

# 🐢 Brute Force Solution

## 💭 Idea

For every position `i`:

1. Find the tallest bar on the **left**.
2. Find the tallest bar on the **right**.
3. The water above `i` is:

```text
water[i] = min(left_max, right_max) - height[i]
```

If the result is negative, no water can be stored there.

### 🧮 Formula

```text
water[i] = max(
    0,
    min(max(height[0:i]), max(height[i+1:n])) - height[i]
)
```

### 🐌 Python

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        n = len(height)

        for i in range(n):
            left_max = 0
            right_max = 0

            # Tallest bar on the left
            for j in range(i):
                left_max = max(left_max, height[j])

            # Tallest bar on the right
            for j in range(i + 1, n):
                right_max = max(right_max, height[j])

            water += max(0, min(left_max, right_max) - height[i])

        return water
```

---

# ⏱️ Brute Force Complexity

```text
Time  : O(n²) 🐢
Space : O(1)  ✨
```

Why `O(n²)`?

For every bar, we scan to the left and right again.

```text
n bars
 ↓
each bar scans ~n bars
 ↓
O(n × n)
 ↓
O(n²)
```

It works, but we can do much better! 🚀

---

# 🧠 Optimization — The Big Hint

Instead of repeatedly searching for:

```text
⬅️ left_max
➡️ right_max
```

we can maintain them while moving through the array.

### 🔥 Key Observation

At any position:

```text
Water = min(left_max, right_max) - height[i]
```

But here's the magic ✨:

If

```text
height[left] <= height[right]
```

then the **left side is the limiting boundary**.

So we can safely process the left side.

Similarly:

```text
height[right] < height[left]
```

means the **right side is the limiting boundary**.

🎯 This leads directly to the **Two Pointer** solution.

---

# 💡 Optimal Strategy — Two Pointers

Use two pointers:

```text
left  → ➡️
right ← ⬅️
```

And maintain:

```text
left_max
right_max
water
```

### 🚀 Rules

```text
If height[left] <= height[right]:
    process left
    move left forward

Else:
    process right
    move right backward
```

Why?

Because the shorter side determines how much water can be trapped.

---

# 🎬 Two Pointer Animation

### Example

```text
height = [4, 2, 0, 3, 2, 5]

Step 1
        L                 R
        ↓                 ↓
       [4,  2,  0,  3,  2,  5]

       4 <= 5
       👈 Process LEFT

       left_max = 4
```

```text
Step 2

           L              R
           ↓              ↓
       [4,  2,  0,  3,  2,  5]

       2 <= 5
       💧 Water += 4 - 2 = 2

       water = 2
```

```text
Step 3

              L           R
              ↓           ↓
       [4,  2,  0,  3,  2,  5]

       0 <= 5
       💧 Water += 4 - 0 = 4

       water = 6
```

```text
Step 4

                 L        R
                 ↓        ↓
       [4,  2,  0,  3,  2,  5]

       3 <= 5
       💧 Water += 4 - 3 = 1

       water = 7
```

```text
Step 5

                    L     R
                    ↓     ↓
       [4,  2,  0,  3,  2,  5]

       2 <= 5
       💧 Water += 4 - 2 = 2

       water = 9 🎉
```

### 🏆 Final Answer

```text
💧💧💧💧💧💧💧💧💧

Total = 9 units
```

---

# 🏎️ Optimal Solution

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        left_max = 0
        right_max = 0
        water = 0

        while left < right:
            if height[left] <= height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]

                left += 1

            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]

                right -= 1

        return water
```

---

# 🔍 Why Does This Work?

Imagine water trapped at a bar:

```text
       🧱           🧱
       🧱💧💧💧💧💧🧱
       🧱💧🧱💧💧💧🧱
       🧱🧱🧱🧱🧱🧱🧱
```

The amount of water depends on:

```text
shorter boundary - current height
```

So:

```text
water = min(left_max, right_max) - height[i]
```

The two-pointer trick avoids explicitly calculating both boundaries for every index.

### 🧠 Golden Rule

> ⭐ **Always process the side with the smaller current height.**

```text
height[left] <= height[right]
          ↓
     process LEFT

height[right] < height[left]
          ↓
     process RIGHT
```

That is the heart ❤️ of the optimal solution.

---

# 🧩 Dry Run

For:

```text
[4, 2, 0, 3, 2, 5]
```

| Step | Left | Right | Left Max | Right Max | Water |
|------|------|-------|----------|-----------|-------|
| 1 | 0 | 5 | 4 | 0 | 0 |
| 2 | 1 | 5 | 4 | 0 | 2 |
| 3 | 2 | 5 | 4 | 0 | 6 |
| 4 | 3 | 5 | 4 | 0 | 7 |
| 5 | 4 | 5 | 4 | 0 | 9 |

🎉 **Answer = 9**

---

# ⚡ Complexity

### 🐢 Brute Force

```text
Time  : O(n²)
Space : O(1)
```

### 🚀 Two Pointer

```text
Time  : O(n)    ⚡
Space : O(1)    🧠
```

### 📊 Performance

```text
Brute Force   O(n²)
      🐢
      │
      │
      ▼
      ┌───────────────────────┐
      │       Searching       │
      │    again and again    │
      └───────────────────────┘

Two Pointer   O(n)
      🚀
      │
      ▼
      ┌───────────────────────┐
      │   One pass through    │
      │       the array       │
      └───────────────────────┘
```

---

# 🧠 Interview Tips & Tricks

### 💡 Tip 1 — Think About Boundaries

Whenever you see:

```text
🏔️  valleys  🏔️
```

ask:

> "What limits the amount of water?"

Usually, the **smaller boundary**.

---

### 💡 Tip 2 — Remember the Formula

```text
💧 Water = min(left_max, right_max) - height[i]
```

This formula is the foundation of almost every solution.

---

### 💡 Tip 3 — Recognize Two Pointers

When you see:

```text
➡️                         ⬅️
left                     right
```

and the answer depends on information from both ends, consider **Two Pointers**.

---

### 💡 Tip 4 — Avoid Extra Arrays When Possible

A common optimization is to precompute:

```text
left_max[]
right_max[]
```

That gives:

```text
Time  : O(n)
Space : O(n)
```

But the two-pointer method goes one step further:

```text
Time  : O(n)
Space : O(1) 🚀
```

---

# 🏆 Pattern Recognition

This problem is a classic example of:

```text
🧠 Array
   +
🎯 Two Pointers
   +
📈 Running Maximum
   =
💧 Trapping Rain Water
```

When practicing LeetCode, remember the pattern rather than memorizing the code.

---

# 📝 Quick Revision

Before an interview, remember just these 5 things:

```text
1️⃣ left = 0
2️⃣ right = n - 1

3️⃣ Track:
   left_max
   right_max

4️⃣ Process the smaller side

5️⃣ Add:
   max_boundary - current_height
```

### 🔥 One-Line Memory Trick

> **"Smaller side moves, bigger side waits."** 🧠⚡

---

# 🎯 Final Takeaway

```text
Brute Force
   ↓
For every bar, search left + right
   ↓
O(n²) 🐢

Optimization
   ↓
Maintain left_max + right_max
   ↓
Use two pointers
   ↓
O(n) 🚀
   ↓
O(1) Space ✨
```

🌧️ Rain may fall...

💧 Water may trap...

🧠 But with Two Pointers...

# 🚀 YOU TRAP IT IN O(n)! 🚀

---

## ⭐ LeetCode Pattern

```text
Problem : Trapping Rain Water
Number  : 42
Pattern : Two Pointers
Level   : Hard 🔥

Brute Force : O(n²) / O(1)
Optimal     : O(n)  / O(1) 🚀
```

---

### 💙 Happy LeetCoding!

```text
        ☁️
     🌧️ 🌧️ 🌧️
   💧💧💧💧💧💧
  🧱   🧱   🧱
  🧱💧💧💧💧🧱
  🧱🧱🧱🧱🧱🧱

Keep coding. Keep learning. Keep growing. 🌱🚀
```
