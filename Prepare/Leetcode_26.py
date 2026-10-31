class Solution(object):
    def removeDuplicates(self, nums):
        left = 0
        for rigth in range(1, len(nums)):
            if nums[rigth] != nums[left]:
               left = left + 1
            nums[left] = nums[rigth]
        return left +1
        
