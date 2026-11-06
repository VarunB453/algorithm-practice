class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:

        logs.sort(key=lambda a: a[1])

        sorted_queries = sorted(
            [(q, i) for i, q in enumerate(queries)]
        )

        freq = defaultdict(int)
        ans = [0] * len(queries)

        left = right = 0

        for q, idx in sorted_queries:
            while right < len(logs) and logs[right][1] <= q:
                server, time = logs[right]
                freq[server] += 1
                right += 1

            while left < right and logs[left][1] < q - x:
                server, time = logs[left]
                freq[server] -= 1

                if freq[server] == 0:
                    del freq[server]

                left += 1

            ans[idx] = n - len(freq)

        return ans
