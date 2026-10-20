
class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        pref_max = [0] * (n + 1)
        for i in range(n):
            pref_max[i + 1] = max(pref_max[i], nums[i])


        suff_min = [float('inf')] * (n + 1)
        for i in range(n - 1, -1, -1):
            suff_min[i] = min(suff_min[i + 1], nums[i])



        drop = [0] * n
        for i in range(1, n):
            drop[i] = drop[i - 1] + (nums[i - 1] > nums[i])

        ans = 0

       
        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True

            for l in range(0, n, k):
                r = l + k - 1


                descents = drop[r] - drop[l]

                if nums[r] > nums[l]:
                    descents += 1

                if descents > 1:
                    valid = False
                    break
                if pref_max[l] > suff_min[l]:
                    valid = False
                    break

            if valid:
                ans += k

        return ans
