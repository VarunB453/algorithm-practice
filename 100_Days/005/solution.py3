class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans = nums[0]

        for x in nums:
            if abs(x) < abs(ans) or (abs(x) == abs(ans) and x > ans):
                ans = x

        return ans