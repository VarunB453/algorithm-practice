# 🌡️ LeetCode 739 --- Daily Temperatures

```{=html}
<p align="center">
```
`<strong>`{=html}LeetCode · Python 3 · Stack · Monotonic
Stack`</strong>`{=html}`<br/>`{=html} `<em>`{=html}Find how long each
day must wait for a warmer temperature!`</em>`{=html}
```{=html}
</p>
```

------------------------------------------------------------------------

## 📌 Problem Statement

Given an array `temperatures` where `temperatures[i]` represents the
temperature on the `i-th` day, return an array `answer` such that:

-   `answer[i]` is the number of days to wait after day `i` to get a
    warmer temperature.
-   If there is no future day with a warmer temperature,
    `answer[i] = 0`.

**Important:** A warmer temperature must be strictly greater, not equal.

### Example

``` text
Input:  temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]
```

**Explanation:**

-   Day 0: `74 > 73` → wait `1` day.
-   Day 1: `75 > 74` → wait `1` day.
-   Day 2: `76 > 75` → wait `4` days.
-   Day 3: `72 > 71` → wait `2` days.
-   Day 4: `72 > 69` → wait `1` day.
-   Day 5: `76 > 72` → wait `1` day.
-   Days 6 and 7: no warmer future day exists → `0`.

------------------------------------------------------------------------

## 🐢 1. Brute-Force Approach

### 💡 Intuition

For every day, look at all the days that come after it until a warmer
temperature is found.

1.  Start from the current day `i`.
2.  Check each future day `j`.
3.  If `temperatures[j] > temperatures[i]`, store `j - i` and stop
    searching.
4.  If no warmer day exists, leave the answer as `0`.

### Python 3 --- Brute Force

``` python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n

        for i in range(n):
            for j in range(i + 1, n):
                if temperatures[j] > temperatures[i]:
                    ans[i] = j - i
                    break

        return ans
```

### Complexity Analysis

  -----------------------------------------------------------------------
  Complexity              Value                   Reason
  ----------------------- ----------------------- -----------------------
  Time                    `O(n²)`                 Each day may scan all
                                                  subsequent days.

  Space                   `O(n)`                  The output array
                                                  requires `n` elements;
                                                  auxiliary space is
                                                  `O(1)`.
  -----------------------------------------------------------------------

⚠️ **Limitation:** In the worst case, many days scan almost the entire
remaining array. This can lead to a Time Limit Exceeded (TLE) result for
large inputs.

------------------------------------------------------------------------

## 💡 2. Hints to Reach the Optimal Solution

Instead of repeatedly searching the future, consider what happens when a
warmer temperature appears.

**Hint 1 --- Think backwards about unresolved days**

A day remains unresolved until a warmer temperature is encountered.

**Hint 2 --- Store indices, not temperatures**

Why indices? Because the answer requires the distance between two days:

``` python
wait_days = current_index - previous_index
```

**Hint 3 --- Maintain a decreasing stack**

Keep indices whose corresponding temperatures are in decreasing order
from the bottom of the stack to the top.

**Hint 4 --- Resolve multiple days at once**

When the current temperature is warmer than the temperature at the top
index, that earlier day has found its next warmer day.

``` python
while stack and temperatures[i] > temperatures[stack[-1]]:
    j = stack.pop()
    ans[j] = i - j
```

✨ One warmer day can resolve several previous days!

------------------------------------------------------------------------

## 🚀 3. Optimal Approach --- Monotonic Decreasing Stack

### Core Intuition

Use a stack to store indices of days that have not yet found a warmer
future temperature.

The stack maintains this invariant:

> Temperatures corresponding to the stored indices are in strictly
> decreasing order from bottom to top.

For every current index `i`:

1.  While the stack is not empty and the current temperature is warmer
    than the temperature at the top index:
    -   Pop the previous index `j`.
    -   Calculate the waiting period: `i - j`.
    -   Store it in `ans[j]`.
2.  Push the current index onto the stack.
3.  Continue until every day has been processed.

Any indices remaining in the stack have no warmer future day. Their
answers correctly remain `0`.

### Python 3 --- Optimal Solution

``` python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                ans[j] = i - j

            stack.append(i)

        return ans
```

### 🔍 Understanding the Important Lines

  -----------------------------------------------------------------------
  Code                                Purpose
  ----------------------------------- -----------------------------------
  `ans = [0] * n`                     Initializes all answers to zero.

  `stack = []`                        Stores indices of unresolved days.

  `while stack and ...`               Checks whether the current day
                                      resolves previous days.

  `j = stack.pop()`                   Removes a resolved day.

  `ans[j] = i - j`                    Calculates the number of days to
                                      wait.

  `stack.append(i)`                   Adds the current unresolved day.
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 🎬 4. Animated Walkthrough

The following animation illustrates how indices enter the stack, how
warmer temperatures resolve earlier days, and how the answer array gets
updated.

```{=html}
<p align="center">
```
`<img 739.gif" alt="Animated monotonic stack walkthrough for Daily Temperatures" width="800"/>`{=html}
```{=html}
</p>
```
### Step-by-Step Dry Run

Input:

``` text
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
```

    Day `i`   Temperature Operation                 Stack (bottom → top)
  --------- ------------- ------------------------- ----------------------
          0            73 Push 0                    `[0]`
          1            74 Resolve 0; push 1         `[1]`
          2            75 Resolve 1; push 2         `[2]`
          3            71 Push 3                    `[2, 3]`
          4            69 Push 4                    `[2, 3, 4]`
          5            72 Resolve 4 and 3; push 5   `[2, 5]`
          6            76 Resolve 5 and 2; push 6   `[6]`
          7            73 Push 7                    `[6, 7]`

Final answer:

``` text
[1, 1, 4, 2, 1, 1, 0, 0]
```

**Notice:** The stack contains indices, not temperature values. This
makes calculating the waiting period straightforward.

------------------------------------------------------------------------

## ⏱️ 5. Complexity Analysis --- Optimal Solution

  -----------------------------------------------------------------------
  Complexity              Value                   Explanation
  ----------------------- ----------------------- -----------------------
  Time                    `O(n)`                  Every index is pushed
                                                  once and popped at most
                                                  once.

  Auxiliary Space         `O(n)`                  The monotonic stack can
                                                  hold up to `n` indices.

  Output Space            `O(n)`                  The answer array
                                                  contains `n` elements.
  -----------------------------------------------------------------------

### Why Is the Time Complexity O(n), Not O(n²)?

Although the solution contains a nested `while` loop, it does not
repeatedly process the same elements.

-   Every index is pushed onto the stack exactly once.
-   Every index can be popped from the stack at most once.
-   Therefore, the total number of push and pop operations is bounded by
    `2n`.

Hence:

``` text
Total operations = O(n)
```

This is an example of **amortized analysis**.

------------------------------------------------------------------------

## 🧠 6. Interview Tips & Tricks

### Recognize the Monotonic Stack Pattern

Consider a monotonic stack whenever a problem asks for:

-   Next greater element.
-   Next smaller element.
-   Previous greater or smaller element.
-   The nearest element satisfying a comparison.
-   Waiting distance until a condition is satisfied.

### Key Observations

1.  Store indices when the final answer requires distances or positions.
2.  Use a `while` loop because one element can resolve multiple previous
    elements.
3.  Use strict `>` because the problem requires a strictly warmer
    temperature.
4.  Initialize the result with zeros to handle days without a warmer
    future temperature.
5.  Process from left to right because the current temperature can
    resolve previous unresolved days.

### Common Mistakes to Avoid

  -----------------------------------------------------------------------
  Mistake                             Correction
  ----------------------------------- -----------------------------------
  Storing temperatures instead of     Store indices to calculate
  indices                             distance.

  Using `>=` instead of `>`           Equal temperatures are not warmer.

  Using `if` instead of `while`       Multiple previous days may be
                                      resolved.

  Forgetting the default zero         Unresolved days must return zero.

  Reversing the subtraction           Use `i - j`, not `j - i`.
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 🏁 7. Final Takeaways

```{=html}
<details>
```
```{=html}
<summary>
```
`<strong>`{=html}Click to reveal the key learning
points`</strong>`{=html}
```{=html}
</summary>
```
-   **Pattern:** Next Greater Element.
-   **Data Structure:** Monotonic Decreasing Stack.
-   **Traversal:** Left to right.
-   **Stack stores:** Indices of unresolved days.
-   **Comparison:** `temperatures[i] > temperatures[stack[-1]]`.
-   **Optimal Time:** `O(n)`.
-   **Auxiliary Space:** `O(n)`.

The key optimization is avoiding repeated future searches. Each day is
processed only a constant number of times through stack operations.

```{=html}
</details>
```
### 🌟 Final Verdict

  Approach               Time   Auxiliary Space
  ----------------- --------- -----------------
  Brute Force         `O(n²)`            `O(1)`
  Monotonic Stack      `O(n)`            `O(n)`

**Remember:** When a current element resolves the next greater element
for previous unresolved indices, a monotonic stack is often the right
tool.

------------------------------------------------------------------------

```{=html}
<p align="center">
```
`<strong>`{=html}🚀 Keep Practising. Keep Optimizing. Keep Solving!
💻`</strong>`{=html}`<br/>`{=html} `<em>`{=html}One problem at a time,
one pattern at a time.`</em>`{=html}
```{=html}
</p>
```
