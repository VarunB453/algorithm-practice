# 🔁 LeetCode 206 --- Reverse Linked List

> **Language:** Python 3\
> **Difficulty:** Easy\
> **Topic:** Linked List, Iteration, Pointers

Reverse a singly linked list and return the new head.

## 🧩 Problem intuition

Each node points to the next node. Reversing the list means changing
every `next` pointer so that it points to the previous node instead.

For example:

``` text
Before:  1 → 2 → 3 → 4 → None
After:   4 → 3 → 2 → 1 → None
```

The important challenge is to preserve the rest of the list before
changing a pointer. Otherwise, the unprocessed nodes become unreachable.

## 🐢 Brute-force approach --- use an auxiliary list

### Idea

1.  Traverse the linked list and store every node in a Python list.
2.  Traverse that auxiliary list in reverse order.
3.  Reconnect each node to the preceding node in the reversed order.
4.  Set the original head's `next` pointer to `None` and return the last
    stored node.

This is straightforward, but it stores references to all nodes, so it
requires additional linear space.

### Python 3 solution

``` python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        nodes = []
        current = head

        while current is not None:
            nodes.append(current)
            current = current.next

        for i in range(len(nodes) - 1, 0, -1):
            nodes[i].next = nodes[i - 1]

        nodes[0].next = None
        return nodes[-1]
```

**Complexity**

-   **Time:** `O(n)` --- one traversal to collect nodes and one
    traversal to reconnect them.
-   **Auxiliary space:** `O(n)` --- the `nodes` list stores `n` node
    references.

## 💡 Hints for the optimal solution

Think about these questions before reading the implementation:

1.  Which pointer must be saved before changing `current.next`?
2.  What should the first node point to after reversal?
3.  Which three references are needed to reverse one link?
4.  When should `prev` and `current` move forward?

**Key trick:** save `current.next` first. Then reverse the current link,
and only after that advance to the saved next node.

## ⚡ Optimal approach --- iterative pointer reversal

Maintain three references:

-   `prev_node`: the already-reversed part; initially `None`.
-   `current_node`: the node currently being processed; initially
    `head`.
-   `next_node`: temporarily stores the next unprocessed node.

For each node:

1.  Save the next node.
2.  Point the current node backward to `prev_node`.
3.  Move `prev_node` to the current node.
4.  Move `current_node` to the saved next node.

When `current_node` becomes `None`, `prev_node` is the new head.

### Python 3 --- optimal solution

``` python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        current_node = head

        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        return prev_node
```

### 🎞️ Pointer animation

The following animation traces the pointer updates for
`1 → 2 → 3 → None`.

![Animated pointer reversal](reverse_linked_list_animation.gif)

A compact view of one iteration:

``` text
Before:
prev = None       current = 1 → 2 → 3 → None

Save the next node:
next = 2

Reverse the link:
1 → None

Advance:
prev = 1          current = 2 → 3 → None
```

Repeat the same operations until `current` is `None`. The reversed chain
is then `3 → 2 → 1 → None`.

### Complexity analysis

Let `n` be the number of nodes.

  -----------------------------------------------------------------------
  Measure                 Complexity              Reason
  ----------------------- ----------------------- -----------------------
  Time                    `O(n)`                  Each node is visited
                                                  exactly once.

  Auxiliary space         `O(1)`                  Only a fixed number of
                                                  pointer variables are
                                                  used.
  -----------------------------------------------------------------------

The iterative solution is optimal in asymptotic time because every node
must be visited at least once, and it uses constant auxiliary space.

## 🧠 Interview tips and common mistakes

-   **Do not overwrite the link too early.** Store `current_node.next`
    before assigning a new value to `current_node.next`.
-   **Initialize `prev_node` to `None`.** This makes the original tail
    point to `None` after reversal and correctly terminates the new
    list.
-   **Return `prev_node`, not `head`.** The original tail becomes the
    new head.
-   **Handle an empty list naturally.** If `head` is `None`, the loop is
    skipped and `None` is returned.
-   **Avoid creating new nodes.** The optimal method reverses the
    existing links in place.

## 🏁 Final comparison

  Approach                     Time     Auxiliary space
  ---------------------------- -------- -----------------
  Auxiliary list               `O(n)`   `O(n)`
  Iterative pointer reversal   `O(n)`   `O(1)`

**Takeaway:** when reversing a linked list in place, the three-pointer
pattern---`prev`, `current`, and `next`---is the essential technique. 🔥
