class Solution:
    def maxDepth(self, s: str) -> int:
        depth = ans = 0
        for ch in s:
            if ch == '(':
                depth += 1
                ans = max(ans, depth)
            elif ch == ')':
                depth -= 1
        return ans
