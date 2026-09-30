class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = []
        depth = 0

        for ch in seq:
            if ch == '(':
                depth += 1
                ans.append(depth & 1)
            else:
                ans.append(depth & 1)
                depth -= 1

        return ans
