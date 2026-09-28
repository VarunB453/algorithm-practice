class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = curr = nums[0]
        for x in nums[1:]:
            curr = max(x, curr + x)
            best = max(best, curr)
        return best
