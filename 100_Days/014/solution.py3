class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted((w / q, q) for q, w in zip(quality, wage))

        max_heap = []
        quality_sum = 0
        ans = float('inf')

        for ratio, q in workers:
            heapq.heappush(max_heap, -q)
            quality_sum += q

            if len(max_heap) > k:
                quality_sum += heapq.heappop(max_heap)

            if len(max_heap) == k:
                ans = min(ans, quality_sum * ratio)

        return ans