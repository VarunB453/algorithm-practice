<div align="center">

# 🚀 LeetCode 121 — Best Time to Buy and Sell Stock 📈

### 💰 Buy low, sell high, and maximize your profit!

![LeetCode](https://img.shields.io/badge/LeetCode-121-orange?logo=leetcode)
![Language](https://img.shields.io/badge/Language-Python%203-blue?logo=python)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen)

**Goal:** Find the maximum profit from one buy and one sell. You must buy before you sell!

</div>

---

## 🧩 Problem in Simple Words

You are given an array `prices`, where `prices[i]` is the stock price on day `i`.

Choose **one day to buy** and a **later day to sell** to earn the highest possible profit. If no profit is possible, return `0`.

### 🧪 Example

```text
Input:  prices = [7, 1, 5, 3, 6, 4]
Output: 5
```

✨ Buy at **1** and sell later at **6**.

```text
Profit = Selling Price - Buying Price
       = 6 - 1
       = 5
```

---

## 🐢 1. Brute-Force Solution

💡 **Idea:** Try every possible pair of days. For each buying day, check every later selling day and keep the best profit.

```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)

        for buy in range(n):
            for sell in range(buy + 1, n):
                profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, profit)

        return max_profit
```

### ⏱️ Complexity

- **Time:** `O(n²)` — checks all possible buy/sell pairs.
- **Space:** `O(1)` — uses a fixed number of extra variables.

⚠️ **Why improve it?** Checking every pair gets slow when the input is large.

---

## 🧠 2. Hints to Find the Optimal Solution

Try these clues before looking at the code! 👀

1. 🤔 Do you really need to remember every earlier price?
2. 📉 While moving through the list, keep track of the **lowest price seen so far**.
3. 💵 At each price, ask: “If I sell today, what profit could I make?”
4. 🏆 Keep the best profit seen so far.
5. 🚫 If every possible profit is negative, the answer should stay `0`.

### 🎯 Key Trick

You only need two values:

- `min_price` — the cheapest price seen so far.
- `max_profit` — the largest profit found so far.

---

## ⚡ 3. Optimal Solution — One Pass

```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit
```

### 🔍 How It Works

- Initialize `min_price` to infinity so the first price becomes the minimum.
- For each price, update the lowest price seen so far.
- Calculate the profit using the current price and the lowest price.
- Update `max_profit` if this profit is better.
- Return the best profit found.

### ⏱️ Complexity

| Complexity | Result | Why? |
|---|---|---|
| **Time** | `O(n)` | Each price is visited once. |
| **Space** | `O(1)` | Only two tracking variables are needed. |

✅ **Optimal:** A single pass is linear time, and the algorithm uses constant extra space.

---

## 🎬 4. Step-by-Step Animation

Watch the algorithm scan each price from left to right. The lowest price and best profit update as it goes.

```text
Prices:     [7,  1,  5,  3,  6,  4]
             ↓   ↓   ↓   ↓   ↓   ↓

Day 1:  price = 7  | min_price = 7 | max_profit = 0
        📍 Start tracking the cheapest price.

Day 2:  price = 1  | min_price = 1 | max_profit = 0
        📉 Found a cheaper buying opportunity!

Day 3:  price = 5  | min_price = 1 | max_profit = 4
        💵 Potential profit: 5 - 1 = 4

Day 4:  price = 3  | min_price = 1 | max_profit = 4
        🔎 Profit today is 3 - 1 = 2, so keep 4.

Day 5:  price = 6  | min_price = 1 | max_profit = 5
        🎉 New best profit: 6 - 1 = 5!

Day 6:  price = 4  | min_price = 1 | max_profit = 5
        ✅ Best profit stays 5.

Final Answer: 5 🏆
```

### 🌀 Visual Flow

```text
       Start
         |
         v
  Read current price
         |
         v
 Update minimum price
         |
         v
 Calculate today's profit
         |
         v
 Update maximum profit
         |
         v
   More prices? ---- No ----> Return max_profit 🎉
         |
        Yes
         |
         └----------> Read next price
```

---

## 🧠 Tips & Tricks to Remember

- 📉 **Minimum first:** Track the cheapest price encountered so far.
- 💰 **Sell later:** The current price is the selling price; the minimum must come from the current day or an earlier day.
- 🛑 **No profit is okay:** Start `max_profit` at `0`, so decreasing prices return `0`.
- 🔁 **One loop is enough:** You do not need nested loops for the optimal solution.
- 🧩 **Update as you go:** Keep only the information needed for future decisions.

### 🚫 Common Mistake

Do not calculate profit from a future minimum price. The buying day must come before or on the current day, and selling happens later. Updating `min_price` before calculating profit is safe here because it can only produce a zero profit when the current price is the new minimum.

---

## 🏁 Final Comparison

| Approach | Time | Extra Space |
|---|---:|---:|
| 🐢 Brute force | `O(n²)` | `O(1)` |
| ⚡ Optimal one-pass | `O(n)` | `O(1)` |

<div align="center">

### 🌟 Keep practicing — every problem makes you stronger! 💪

**Remember:** Find the lowest price so far, calculate today's profit, and keep the best one. 📈

</div>
