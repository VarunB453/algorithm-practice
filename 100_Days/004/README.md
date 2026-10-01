# LeetCode 11 — Container With Most Water

> **Python 3 • Two Pointers • Beginner Friendly 🚀**

The goal of **LeetCode 11** is to find two lines that, together with the x-axis, form a container that holds the **most water** 💧

You are given an array `height` where `height[i]` represents the height of a vertical line at position `i`. Choose **two lines** such that the container they form holds the **maximum** amount of water!

A container is **valid** if:

- You pick **two different indices** `i` and `j` (with `i < j`) 🎯
- The **width** is the distance between them: `j - i` 📏
- The **height** is limited by the **shorter** line: `min(height[i], height[j])` 📉
- Water can **spill over the shorter side**, so the taller line doesn't help! 🚰

For example:

```text
Input:  height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: Choose lines at index 1 (height 8) and index 8 (height 7).
             Width = 8 - 1 = 7, Height = min(8, 7) = 7
             Water = 7 × 7 = 49 🎉
```

```text
Input:  height = [1,1]
Output: 1
Explanation: Only two lines! Width = 1, Height = min(1, 1) = 1
             Water = 1 × 1 = 1 💧
```

```text
Input:  height = [4,3,2,1,4]
Output: 16
Explanation: Choose the two lines of height 4 at the ends!
             Width = 4, Height = min(4, 4) = 4
             Water = 4 × 4 = 16 🎊
```

The key observation is wonderfully simple:

- The **widest** container (using the two ends) is a great starting candidate! 📏
- To find a **taller** container, you must move the **shorter** line inward 🎯
- Moving the **taller** line can never help — the height is capped by the shorter one! 📉
- Use **two pointers** — one at each end — and shrink the window intelligently! 🪟

## 🎬 Little Animation

![Animated Two Pointers trace](./11.gif)

The animation shows the **left** and **right** pointers starting at the ends and moving toward each other! 🚶‍♂️🚶‍♀️ Watch how we always move the pointer at the **shorter** line, hoping to find a **taller** one! The water level rises and falls as we hunt for the perfect container! 💃🕺

---

## 🐢 Brute-Force Solution

A straightforward brute-force idea is:

Check **every possible pair** of lines! For each pair `(i, j)` where `i < j`, calculate the water it can hold, and keep track of the maximum! 🔍

### Python 3

```python
class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_water = 0
        n = len(height)

        for i in range(n):
            for j in range(i + 1, n):
                width = j - i
                h = min(height[i], height[j])
                water = width * h
                max_water = max(max_water, water)

        return max_water
```

### Complexity

- **Time:** `O(n²)` ⏳ — We check all `n × (n-1) / 2` pairs! For `n = 10⁵`, that's about **5 billion** operations! 💥
- **Space:** `O(1)` 💾 — Just a few variables, no extra storage needed! ✅

This works, but it's **way too slow** for large inputs! 💥 We're doing a lot of **redundant work** — many pairs can't possibly beat our current best! The two-pointer approach eliminates all that waste! 🎯

---

## 💡 Optimization Tips, Tricks & Hints

### Hint 1 — Start wide, then get smart! 🧠

The **widest** container is formed by the two **end** lines. Start there! 📏 If you move both pointers inward randomly, you'll miss the magic. But if you move **strategically**, you can skip huge chunks of useless pairs! ✨

### Hint 2 — Move the shorter line! 🎯

Here's the golden rule:

- If `height[left] < height[right]` → move `left` pointer **right**! ➡️
- If `height[left] >= height[right]` → move `right` pointer **left**! ⬅️

**Why?** Because the water level is capped by the **shorter** line. Moving the **taller** line can only make things **worse** (less width, same or lower height). But moving the **shorter** line might find a **taller** line that actually helps! 📈

### Hint 3 — Don't second-guess yourself! ⚠️

When you move the shorter pointer, you might worry: "What if the taller line pairs better with something else?" Don't worry! 🤗 That taller line will still be considered when the other pointer eventually moves past it. You're not losing anything — you're just being **efficient**! 🎯

### Trick 🪄

Think of it like **squeezing a water balloon** 🎈:

```text
Two hands hold a water balloon at the ends! 🤲
The water level = the lower hand! 💧
To hold MORE water, you must RAISE the lower hand! ⬆️
If you raise the higher hand, water just spills! 🌊
So always move the LOWER hand inward, hoping for a taller grip! 🎯
```

### Bonus Trick — One-liner with max tracking ✨

```python
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0

        while left < right:
            max_water = max(max_water, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water
```

*(Compact, elegant, and interview-ready! 😄)*

---

## 🚀 Optimal Solution (Two Pointers)

The optimal solution makes **one pass** through the array — each pointer moves at most `n` steps total!

```python
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1  # 🚪 Start at the two ends!
        max_water = 0  # 💧 Our best find so far!

        while left < right:
            width = right - left  # 📏 How far apart are we?
            h = min(height[left], height[right])  # 📉 Limited by the shorter wall!
            water = width * h  # 💧 Area = width × height!
            max_water = max(max_water, water)  # 🏆 Keep the best!

            if height[left] < height[right]:  # 🎯 Left is shorter?
                left += 1  # ➡️ Move left pointer right!
            else:  # 🎯 Right is shorter (or equal)?
                right -= 1  # ⬅️ Move right pointer left!

        return max_water  # 🎉 The maximum water we can hold!
```

### Why this is optimal

Each pointer moves **at most `n` steps**:

- **Total iterations:** At most `n - 1` — the pointers start `n - 1` apart and always move closer! 📏
- **Each iteration:** One comparison, one area calculation, one pointer move — all `O(1)`! ⚡
- **No backtracking:** Once a pointer moves, it never comes back! The greedy choice is **provably correct**! 🎯

The two-pointer strategy works because:

- We **never miss** the optimal pair — if the optimal pair is `(i, j)`, we'll reach it! ✅
- We **skip** pairs that can't possibly be better — saving massive time! ⏩
- It's a beautiful example of **greedy + two pointers** working together! 🤝

We check each line at most once from each side — that's the power of the **Two Pointers**! 🎯✨

---

## 🔎 Dry Run

For:

```text
height = [1,8,6,2,5,4,8,3,7]
```

The trace produces:

```text
Start: left=0 (h=1), right=8 (h=7)
  width=8, h=min(1,7)=1, water=8×1=8    max=8    🚶 left moves (1<7)

left=1 (h=8), right=8 (h=7)
  width=7, h=min(8,7)=7, water=7×7=49   max=49   🏆 NEW BEST!
  🚶 right moves (8>=7)

left=1 (h=8), right=7 (h=3)
  width=6, h=min(8,3)=3, water=6×3=18   max=49   🚶 right moves (8>=3)

left=1 (h=8), right=6 (h=8)
  width=5, h=min(8,8)=8, water=5×8=40   max=49   🚶 right moves (8>=8)

left=1 (h=8), right=5 (h=4)
  width=4, h=min(8,4)=4, water=4×4=16   max=49   🚶 right moves (8>=4)

left=1 (h=8), right=4 (h=5)
  width=3, h=min(8,5)=5, water=3×5=15   max=49   🚶 right moves (8>=5)

left=1 (h=8), right=3 (h=2)
  width=2, h=min(8,2)=2, water=2×2=4    max=49   🚶 right moves (8>=2)

left=1 (h=8), right=2 (h=6)
  width=1, h=min(8,6)=6, water=1×6=6    max=49   🚶 right moves (8>=6)

left == right! Done! 🎉
Return 49 ✅
```

For a smaller example:

```text
height = [1,2,1]
```

```text
Start: left=0 (h=1), right=2 (h=1)
  width=2, h=min(1,1)=1, water=2×1=2    max=2    🚶 right moves (1>=1)

left=0 (h=1), right=1 (h=2)
  width=1, h=min(1,2)=1, water=1×1=1    max=2    🚶 left moves (1<2)

left == right! Done! 🎉
Return 2 ✅

The widest container (ends) was the best! 🎯
```

And one more where tall lines win:

```text
height = [4,3,2,1,4]
```

```text
Start: left=0 (h=4), right=4 (h=4)
  width=4, h=min(4,4)=4, water=4×4=16   max=16   🏆 Perfect match!
  🚶 right moves (4>=4)

left=0 (h=4), right=3 (h=1)
  width=3, h=min(4,1)=1, water=3×1=3    max=16   🚶 right moves (4>=1)

left=0 (h=4), right=2 (h=2)
  width=2, h=min(4,2)=2, water=2×2=4    max=16   🚶 right moves (4>=2)

left=0 (h=4), right=1 (h=3)
  width=1, h=min(4,3)=3, water=1×3=3    max=16   🚶 right moves (4>=3)

left == right! Done! 🎉
Return 16 ✅

Two tall towers at the ends = maximum water! 🏰💧
```

---

## 📊 Complexity

| Approach | Time | Space |
|---|---:|---:|
| 🐢 Brute force (all pairs) | `O(n²)` | `O(1)` |
| 🚀 Two Pointers | `O(n)` | `O(1)` |

### Final takeaway

> **Start wide, move the shorter line, and let the two pointers dance toward each other.** ✨

This is a classic example of the **Two Pointers** pattern — when you need to find a pair with a specific property, starting from the ends and moving inward can eliminate the need to check every pair! 🎯

---

## 🧠 Pattern to Remember

This problem is a great introduction to the **Two Pointers** pattern:

```python
def maxArea(height):
    left, right = 0, len(height) - 1
    max_water = 0
    while left < right:
        max_water = max(max_water, (right - left) * min(height[left], height[right]))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water
```

The same mental model appears in many problems involving:

- Finding pairs with a specific sum (Two Sum II) 🎯
- Sorting and searching in sorted arrays 🔍
- Removing duplicates in-place 🧹
- Merging sorted arrays 🤝
- Finding the longest substring with at most K distinct characters 📏
- Palindrome checking (move pointers from both ends) 🔄
- Trapping Rain Water (harder cousin! 🌧️)

Happy coding! 🐍💻🎉
