# 82. Remove Duplicates from Sorted List II 🔗

> **LeetCode · Python 3**\
> Remove every value that occurs more than once. Keep only values that
> appear exactly once.

## 🧩 Problem at a glance

Given the head of a **sorted linked list**, delete all nodes that have
duplicate numbers, leaving only distinct numbers from the original list.
Return the head of the modified list.

**Example**

``` text
Input:  1 → 2 → 3 → 3 → 4 → 4 → 5
Output: 1 → 2 → 5
```

The important distinction: this is not the version that keeps one copy
of each value. If a value appears more than once, **all nodes containing
that value must be removed**.

------------------------------------------------------------------------

## 🐢 Brute-force approach: count each value

### 💡 Idea

For every node, scan the entire linked list and count how many times its
value occurs. Keep the node only when its value appears exactly once.

Because the list is sorted, equal values are adjacent. Nevertheless,
this deliberately simple approach checks the full list for each node,
making the cost easy to understand.

### Python 3

``` python
class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        tail = dummy
        curr = head

        while curr:
            count = 0
            scan = head

            while scan:
                if scan.val == curr.val:
                    count += 1
                scan = scan.next

            if count == 1:
                tail.next = ListNode(curr.val)
                tail = tail.next

            curr = curr.next

        tail.next = None
        return dummy.next
```

### Complexity

-   **Time:** (O(n\^2)) --- each of the (n) nodes triggers a full scan.
-   **Auxiliary space:** (O(1)), excluding the newly constructed output
    list.
-   **Output space:** (O(n)) in the worst case, when every value is
    unique.

This is useful as a baseline, but repeatedly scanning the list is
unnecessary.

------------------------------------------------------------------------

## 🚀 Optimal approach: one-pass pointer manipulation

### 💡 Key observations

1.  The list is sorted, so duplicate values always form a **contiguous
    run**.
2.  A `dummy` node placed before `head` makes it possible to remove
    duplicates at the beginning without a special case.
3.  `prev` always points to the last node confirmed to be unique.
4.  `curr` examines the current run.
5.  If `curr` and `curr.next` have the same value, advance `curr` until
    the entire run has been skipped, then connect `prev.next` to the
    first different value.
6.  Otherwise, the current node is unique: move both pointers forward
    appropriately.

### Python 3 --- optimal solution

``` python
class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr:
            if curr.next and curr.val == curr.next.val:
                val = curr.val

                while curr and curr.val == val:
                    curr = curr.next

                prev.next = curr
            else:
                prev = curr
                curr = curr.next

        return dummy.next
```

### 🔍 Pointer walkthrough

Input:

``` text
dummy → 1 → 2 → 3 → 3 → 4 → 4 → 5
         ↑
       curr
prev = dummy
```

-   **1:** No adjacent duplicate. Keep it; advance `prev` and `curr`.
-   **2:** No adjacent duplicate. Keep it; advance `prev` and `curr`.
-   **3 → 3:** A duplicate run is detected. Skip both `3` nodes, then
    set `prev.next` to `4`.
-   **4 → 4:** Skip both `4` nodes, then set `prev.next` to `5`.
-   **5:** It is unique. Keep it and finish.

Final list:

``` text
dummy → 1 → 2 → 5
```

### 🎞️ Animated pointer walkthrough

The animation shows the duplicate runs being bypassed and the retained
nodes being linked together.

![Animated walkthrough of LeetCode
82](82.gif)

### Complexity analysis

Let (n) be the number of nodes in the linked list.

  ------------------------------------------------------------------------
  Metric                                  Complexity Reason
  --------------------- ---------------------------- ---------------------
  **Time**                                    (O(n)) Each node is visited
                                                     and advanced past at
                                                     most once.

  **Auxiliary space**                         (O(1)) Only `dummy`, `prev`,
                                                     `curr`, and `val` are
                                                     used.
  ------------------------------------------------------------------------

This is optimal: every node may need to be inspected, so the time
complexity cannot be better than (O(n)) in the general case.

------------------------------------------------------------------------

## 🧠 Interview tips and common pitfalls

-   **Use a dummy node.** It handles duplicate values at the head
    uniformly.
-   **Skip the complete duplicate run.** Removing only one duplicate
    node is incorrect for this problem.
-   **Do not advance `prev` when deleting.** It must remain at the last
    confirmed unique node so it can reconnect to the next candidate.
-   **Check `curr.next` before comparing.** This prevents accessing a
    missing next node.
-   **Preserve the sorted-list insight.** Adjacent equality is
    sufficient to detect a duplicate run; a hash map is not required.
-   **Return `dummy.next`, not `head`.** The original head may itself
    have been removed.

### ⚠️ Edge cases to test

  Input               Expected output
  ------------------- -----------------
  `[]`                `[]`
  `[1]`               `[1]`
  `[1, 1]`            `[]`
  `[1, 2, 2]`         `[1]`
  `[1, 1, 2]`         `[2]`
  `[1, 2, 3]`         `[1, 2, 3]`
  `[1, 2, 2, 3, 3]`   `[1]`
  `[1, 1, 2, 3, 3]`   `[2]`

------------------------------------------------------------------------

## 🏁 Final takeaway

The optimal solution uses a **dummy node and two pointers** to remove
complete duplicate runs in a single traversal.

-   Brute force: (O(n\^2)) time.
-   Optimal: **(O(n)) time and (O(1)) auxiliary space**.

The central technique is to keep `prev` fixed while `curr` skips an
entire duplicate group. Once the group is bypassed, `prev.next = curr`
reconnects the list cleanly.

**Keep the unique nodes. Skip the duplicate groups. Ship the optimal
solution!** 🚀
