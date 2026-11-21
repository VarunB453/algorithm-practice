class Solution(object):
    def removeDuplicates(self, nums):
        left = 0
        for rigth in range(1, len(nums)):
            if nums[rigth] != nums[left]:
               left = left + 1
            nums[left] = nums[rigth]
        return left +1
        
# 2nd Approch
# class Solution(object):
#     def removeDuplicates(self, nums):
#         if not nums:
#             return 0

#         i = 0
#         for j in range(1, len(nums)):
#             if nums[i] != nums[j]:
#                 i += 1
#                 nums[i] = nums[j]

#         return i + 1
