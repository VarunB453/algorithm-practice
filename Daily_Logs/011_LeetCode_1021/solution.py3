class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        balance = 0

        for ch in s:
            if ch == '(':
                balance += 1
                if balance > 1:
                    ans.append(ch)
            else:
                balance -= 1
                if balance > 0:
                    ans.append(ch)

        return ''.join(ans)
