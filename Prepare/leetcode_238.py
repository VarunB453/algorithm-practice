class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        m = len(nums)
        ans = [1] * m
        for i in range (1, m):
            ans[i] = ans[i-1] * nums[i-1]

        product = 1

        for i in range(m-1, -1, -1):
            ans[i] *= product
            product *= nums[i]

        return ans
        
