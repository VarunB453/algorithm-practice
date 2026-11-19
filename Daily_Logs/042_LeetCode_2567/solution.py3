class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        s0 = s1 = s2 = 10**9 + 1
        l0 = l1 = l2 = 0

        for x in nums:
            if x < s0:
                s0, s1, s2 = x, s0, s1
            elif x < s1:
                s1, s2 = x, s1
            elif x < s2:
                s2 = x

            if x > l0:
                l0, l1, l2 = x, l0, l1
            elif x > l1:
                l1, l2 = x, l1
            elif x > l2:
                l2 = x

        return min(l0 - s2, l2 - s0, l1 - s1)
