class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        tree = [0] * (4 * n)
        lazy = [0] * (4 * n)
        ans = 0
        last = {}

        def update(node, start, end, l, r, val):
            if l > end or r < start:
                return

            if l <= start and end <= r:
                length = end - start + 1
                tree[node] = (tree[node] + 2 * val * tree[node] + length * val * val) % MOD
                lazy[node] += val
                return

            mid = (start + end) // 2
            left = node * 2
            right = left + 1

            push(node, start, end)

            if l <= mid:
                update(left, start, mid, l, r, val)
            if r > mid:
                update(right, mid + 1, end, l, r, val)

            tree[node] = (tree[left] + tree[right]) % MOD

        def push(node, start, end):
            val = lazy[node]
            if val == 0 or start == end:
                return

            mid = (start + end) // 2
            left = node * 2
            right = left + 1

            for child, length in ((left, mid - start + 1),
                                  (right, end - mid)):
                tree[child] = (
                    tree[child] + 2 * val * tree[child]
                    + length * val * val
                ) % MOD
                lazy[child] += val

            lazy[node] = 0

        for i, x in enumerate(nums):
            prev = last.get(x, -1)

            update(1, 0, n - 1, prev + 1, i, 1)

            ans = (ans + tree[1]) % MOD
            last[x] = i

        return ans