# 🧱 LeetCode 155 --- Min Stack

> **Difficulty:** Medium\
> **Topic:** Stack · Design · Auxiliary Data Structure\
> **Language:** Python 3

A stack that does more than stack things! 🚀\
`MinStack` supports the usual stack operations and can return the
**minimum element in constant time**.

------------------------------------------------------------------------

## 🎯 Problem at a Glance

Design a stack that supports:

  Operation     Description                    Required Time
  ------------- ---------------------------- ---------------
  `push(val)`   Push `val` onto the stack               O(1)
  `pop()`       Remove the top element                  O(1)
  `top()`       Return the top element                  O(1)
  `getMin()`    Return the minimum element              O(1)

All operations must run in **O(1) time**.

------------------------------------------------------------------------

## 🐢 1. Brute-Force Approach --- Scan the Stack

### 💡 Idea

Use one normal stack.

-   `push()` appends an element.
-   `pop()` removes the top element.
-   `top()` returns the last element.
-   `getMin()` scans the entire stack and finds the smallest value.

This approach is simple, but `getMin()` takes linear time because every
element may need to be inspected.

### Python 3 --- Brute Force

``` python
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
```

### ⏱️ Complexity Analysis

  Operation      Time Complexity
  ------------ -----------------
  `push()`                  O(1)
  `pop()`                   O(1)
  `top()`                   O(1)
  `getMin()`                O(n)

-   **Auxiliary space:** O(1), excluding the stack itself.
-   **Total space:** O(n) for the stored elements.

⚠️ **Why it is not optimal:** `getMin()` must scan up to all `n`
elements. The problem requires every operation, including `getMin()`, to
be O(1).

------------------------------------------------------------------------

## 🧠 2. Optimal Approach --- Two Stacks

### 💡 Core Insight

Maintain **two stacks**:

1.  `stack` stores every value pushed into the MinStack.
2.  `minStack` stores the minimum value at each corresponding depth.

Whenever a value is pushed, also push the smaller of: - the new value,
and - the current minimum.

That means the top of `minStack` is always the minimum of the current
`stack`.

### 🔍 How the Minimum Stack Evolves

Suppose the following values are pushed: `-2`, `0`, `-3`.

  Operation    `stack`         `minStack`         Current minimum
  ------------ --------------- ---------------- -----------------
  `push(-2)`   `[-2]`          `[-2]`                          -2
  `push(0)`    `[-2, 0]`       `[-2, -2]`                      -2
  `push(-3)`   `[-2, 0, -3]`   `[-2, -2, -3]`                  -3
  `pop()`      `[-2, 0]`       `[-2, -2]`                      -2

Notice what happens after `pop()`: the previous minimum is immediately
available at the top of `minStack`. No scan is required. ✨

### 🎞️ Operation Animation (Step-by-Step)

The following trace illustrates the two stacks as values arrive and
leave.

``` text
Push -2
  stack:     [-2]
  minStack:  [-2]       minimum = -2

Push  0
  stack:     [-2,  0]
  minStack:  [-2, -2]   minimum = -2

Push -3
  stack:     [-2,  0, -3]
  minStack:  [-2, -2, -3]
                         minimum = -3

Pop
  stack:     [-2,  0]
  minStack:  [-2, -2]   minimum = -2
```

**Visual rule:** each push adds one entry to both stacks; each pop
removes one entry from both stacks. Their sizes therefore remain
synchronized.

### 🧩 Python 3 --- Optimal Solution

``` python
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(
                min(val, self.minStack[-1])
            )

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
```

------------------------------------------------------------------------

## ⚙️ 3. Optimal Solution --- Complexity

Let `n` be the number of elements currently stored in the stack.

  Operation      Time Complexity Reason
  ------------ ----------------- ----------------------------------------------
  `push()`                  O(1) Append to each stack; one minimum comparison
  `pop()`                   O(1) Pop once from each stack
  `top()`                   O(1) Read the final element of `stack`
  `getMin()`                O(1) Read the final element of `minStack`

-   **Auxiliary space:** O(n) for `minStack`.
-   **Total space:** O(n) for both stacks.

The optimal approach trades additional memory for constant-time minimum
retrieval.

------------------------------------------------------------------------

## 💡 4. Tips, Tricks & Interview Hints

-   **Think beyond one stack:** When a stack operation needs historical
    information, an auxiliary stack can preserve that information.
-   **Store the minimum at every depth:** `minStack[i]` represents the
    minimum among `stack[0]` through `stack[i]`.
-   **Keep both stacks synchronized:** Every successful `push()` and
    `pop()` must affect both stacks.
-   **Handle duplicate minimums:** Push the current minimum even when it
    is repeated. This ensures that popping one occurrence does not lose
    another occurrence of the same minimum.
-   **Use the top, not a scan:** `minStack[-1]` gives the current
    minimum directly.
-   **Know the trade-off:** The brute-force approach uses less auxiliary
    memory but has O(n) `getMin()`; the two-stack approach uses O(n)
    auxiliary memory and makes every operation O(1).

### 🧪 Quick Duplicate Check

``` text
push(2)  -> stack = [2],       minStack = [2]
push(2)  -> stack = [2, 2],    minStack = [2, 2]
pop()    -> stack = [2],       minStack = [2]
getMin() -> 2
```

Keeping duplicate minimums in `minStack` is essential.

------------------------------------------------------------------------

## 🏁 5. Final Takeaway

The key to **LeetCode 155 --- Min Stack** is maintaining the current
minimum as part of the stack state rather than recalculating it when
requested.

-   🐢 **Brute force:** one stack; `getMin()` is O(n).
-   🚀 **Optimal:** two synchronized stacks; all operations are O(1).
-   🧠 **Core pattern:** auxiliary stack for maintaining useful state
    over time.

**Remember:** if the minimum must be available instantly, keep track of
it while pushing---not when `getMin()` is called. 🎉
