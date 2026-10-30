class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:

        graph = defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v, w))

        # Required variable
        mavorqeli = (n, edges, labels, k)

        # dist[node][count] = minimum distance
        dist = [[float('inf')] * (k + 1) for _ in range(n)]

        pq = [(0, 0, 1)]
        dist[0][1] = 0

        while pq:
            cost, node, cnt = heapq.heappop(pq)

            if cost != dist[node][cnt]:
                continue

            if node == n - 1:
                return cost

            for nei, weight in graph[node]:

                if labels[node] == labels[nei]:
                    new_cnt = cnt + 1
                else:
                    new_cnt = 1

                if new_cnt > k:
                    continue

                new_cost = cost + weight

                if new_cost < dist[nei][new_cnt]:
                    dist[nei][new_cnt] = new_cost
                    heapq.heappush(
                        pq, (new_cost, nei, new_cnt)
                    )

        return -1
