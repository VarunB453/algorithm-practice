::: {align="center"}
# 🔁 LeetCode 141 --- Linked List Cycle

### 🐍 Python 3 \| Hash Set vs. Floyd's Tortoise and Hare

*Detect the loop. Keep the pointers moving. Find the elegant solution!*
:::

------------------------------------------------------------------------

## 🎯 Problem Statement

Given the `head` of a linked list, determine whether the linked list
contains a cycle.

A cycle exists if some node in the list can be reached again by
continuously following the `next` pointer. Internally, `pos` is used to
indicate the index of the node that the tail connects to; `pos` is not
passed as an argument.

Return:

-   `True` if the linked list contains a cycle.
-   `False` if the linked list terminates at `None`.

------------------------------------------------------------------------

## 💡 Approach 1: Visited Set (Straightforward / Brute-Force-Style)

### 🧠 Intuition

As the list is traversed, store every visited node in a set.

-   If the current node is already in the set, that node has been
    visited before. A cycle is present.
-   Otherwise, add the node to the set and move to the next node.
-   If traversal reaches `None`, the list has no cycle.

**Important:** Store the node objects themselves, not their values.
Different nodes may contain the same value.

### 🧩 Python 3 --- Visited Set

``` python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()

        while head:
            if head in visited:
                return True

            visited.add(head)
            head = head.next

        return False
```

### ⏱️ Complexity Analysis

Let `n` be the number of distinct nodes reachable from `head`.

  ------------------------------------------------------------------------
  Complexity                                    Cost Explanation
  --------------------- ---------------------------- ---------------------
  Time                                        `O(n)` Each distinct node is
                                                     visited at most once
                                                     before a repeat is
                                                     detected or `None` is
                                                     reached.

  Space                                       `O(n)` The set stores up to
                                                     `n` node references.
  ------------------------------------------------------------------------

### ✅ When Is This Useful?

The visited-set approach is intuitive and easy to implement. It is a
good starting point when learning cycle detection, but it requires
additional memory.

------------------------------------------------------------------------

## 🚀 Approach 2: Floyd's Cycle Detection (Optimal)

### 🧠 Core Idea --- Tortoise and Hare 🐢🐇

Use two pointers that move at different speeds:

-   **Slow pointer (`slow`)** moves one node at a time.
-   **Fast pointer (`fast`)** moves two nodes at a time.

There are two possible outcomes:

1.  **No cycle:** The fast pointer reaches `None` (or `fast.next` is
    `None`).
2.  **Cycle exists:** The fast pointer eventually catches up with the
    slow pointer, so `slow == fast`.

Why does this work? If a cycle exists, both pointers eventually enter
it. Inside the cycle, the fast pointer gains one node on the slow
pointer during each iteration. Since the cycle is finite, the fast
pointer must eventually meet the slow pointer.

### 🧩 Python 3 --- Optimal Solution

``` python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
```

### 🎬 Pointer Animation

Consider this linked list:

``` text
1 → 2 → 3 → 4 → 5
        ↑       ↓
        └───────┘
```

The cycle is: `3 → 4 → 5 → 3`.

Each row below represents one iteration. The arrows show the positions
after both pointers move.

     Step   Slow 🐢   Fast 🐇 Result
  ------- --------- --------- --------------------------------
    Start         1         1 Both begin at the head.
        1         2         3 Fast moves two steps.
        2         3         5 Both are now inside the cycle.
        3         4         4 They meet --- cycle detected!

``` text
                 ┌───────────────┐
                 ↓               │
1 → 2 → [3] → 4 → 5
        🐢       🐇

After step 1:
1 → 2 → [3] → 4 → 5
    🐢       🐇

After step 2:
1 → 2 → 3 → 4 → [5]
        🐢       🐇

After step 3:
1 → 2 → 3 → [4] → 5
            🐢🐇
            🎉 MEET!
```

The table is the authoritative pointer trace; the diagram is a
conceptual illustration of the movement.

### ⏱️ Complexity Analysis

  ------------------------------------------------------------------------
  Complexity                                    Cost Explanation
  --------------------- ---------------------------- ---------------------
  Time                                        `O(n)` The fast pointer
                                                     advances two nodes
                                                     per iteration;
                                                     traversal is linear
                                                     in the number of
                                                     nodes before
                                                     termination or a
                                                     meeting.

  Space                                       `O(1)` Only two pointers are
                                                     used; no collection
                                                     grows with the input.
  ------------------------------------------------------------------------

`<badge>`{=html}Optimal`</badge>`{=html} Floyd's algorithm achieves
linear time and constant auxiliary space.

------------------------------------------------------------------------

## 🧠 Interview Tips & Tricks

1.  **Check `fast` and `fast.next` in the loop condition.** This
    prevents attempting to move beyond the end of a non-cyclic list.
2.  **Move before comparing.** Compare the pointers after advancing
    them. If both start at `head`, an immediate comparison would always
    report equality.
3.  **Use node identity, not node values.** Two different nodes can hold
    identical values and do not necessarily form a cycle.
4.  **Remember the speed difference.** The fast pointer moves two steps
    and the slow pointer moves one. Their relative speed inside a cycle
    is one node per iteration.
5.  **Do not confuse this problem with finding the cycle's entry
    point.** LeetCode 141 only asks whether a cycle exists. Finding its
    entry point is a related problem (LeetCode 142).

### 🔍 Quick Hint Ladder

-   Hint 1: What would happen if a node were visited twice?
-   Hint 2: Can two pointers traverse the list at different speeds?
-   Hint 3: If the fast pointer catches the slow pointer, what does that
    imply?

------------------------------------------------------------------------

## ⚖️ Approach Comparison

  Feature                         Visited Set               Floyd's Algorithm
  ---------------------- -------------------- -------------------------------
  Time                                 `O(n)`                          `O(n)`
  Auxiliary space                      `O(n)`                          `O(1)`
  Implementation                       Simple         Slightly more reasoning
  Extra data structure                    Set                            None
  Recommended              Learning / clarity   Interviews / optimal solution

## 🏁 Final Takeaway

The visited-set method detects a repeated node by remembering the nodes
already seen. Floyd's Tortoise and Hare detects a cycle through pointer
movement alone.

**For an optimal LeetCode 141 solution, use Floyd's Cycle Detection:
`O(n)` time and `O(1)` auxiliary space.**

::: {align="center"}
### 🌟 Keep learning. Keep debugging. Keep solving! 💻
:::
