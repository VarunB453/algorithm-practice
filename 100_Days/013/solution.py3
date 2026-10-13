class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        @lru_cache(None)
        def dfs(r, c):
            best = 1

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < m and 0 <= nc < n
                        and matrix[nr][nc] > matrix[r][c]):
                    best = max(best, 1 + dfs(nr, nc))

            return best

        return max(
            dfs(r, c)
            for r in range(m)
            for c in range(n)
        )
