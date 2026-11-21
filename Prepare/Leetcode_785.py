class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        odd = [0] * len(graph)

        def bfs(i):
            if odd[i]:
               return True

            q = deque([i])
            
            odd[i] = -1
            while q:
                i = q.popleft()
                for neg in graph[i]:
                    if odd[i]  == odd[neg]:
                        return False
                    elif not odd[neg]:
                        q.append(neg)
                        odd [neg] = -1*odd[i]
            return True

        for i in range(len(graph)):
            if not bfs(i):
                return False
        return True
