class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        available = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(available)

        busy = []
        result = []

        time = 0

        for i, duration in enumerate(tasks):
            time = max(time, i)

            if not available:
                time = max(time, busy[0][0])

            while busy and busy[0][0] <= time:
                finish, weight, idx = heapq.heappop(busy)
                heapq.heappush(available, (weight, idx))

            weight, idx = heapq.heappop(available)

            result.append(idx)

            heapq.heappush(
                busy,
                (time + duration, weight, idx)
            )

        return result
