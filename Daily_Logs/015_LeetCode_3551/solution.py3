class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(x):
            return sum(map(int, str(x)))

        arr = sorted(nums, key=lambda x: (digit_sum(x), x))
        pos = {v: i for i, v in enumerate(arr)}

        n = len(nums)
        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or pos[nums[i]] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = pos[nums[j]]
                cycle_size += 1

            swaps += cycle_size - 1

        return swaps