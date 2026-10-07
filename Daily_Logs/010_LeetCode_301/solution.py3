class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        ans = set()

        def dfs(i, path, left, right, rem_left, rem_right):
            if i == len(s):
                if left == right and rem_left == 0 and rem_right == 0:
                    ans.add("".join(path))
                return

            ch = s[i]

            if ch == '(':
                # Remove it
                if rem_left > 0:
                    dfs(i + 1, path, left, right, rem_left - 1, rem_right)

                # Keep it
                path.append(ch)
                dfs(i + 1, path, left + 1, right,
                    rem_left, rem_right)
                path.pop()

            elif ch == ')':
                # Remove it
                if rem_right > 0:
                    dfs(i + 1, path, left, right, rem_left, rem_right - 1)

                # Keep it only if valid
                if left > right:
                    path.append(ch)
                    dfs(i + 1, path, left, right + 1,
                        rem_left, rem_right)
                    path.pop()

            else:
                path.append(ch)
                dfs(i + 1, path, left, right, rem_left, rem_right)
                path.pop()

        # Count parentheses that must be removed
        rem_left = rem_right = 0

        for ch in s:
            if ch == '(':
                rem_left += 1
            elif ch == ')':
                if rem_left > 0:
                    rem_left -= 1
                else:
                    rem_right += 1

        dfs(0, [], 0, 0, rem_left, rem_right)

        return list(ans)