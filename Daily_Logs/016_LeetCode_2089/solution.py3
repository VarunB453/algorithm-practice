class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        smaller = sum(x < target for x in nums)
        equal = sum(x == target for x in nums)

        return list(range(smaller, smaller + equal))
