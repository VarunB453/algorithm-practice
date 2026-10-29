class Solution:
    def palindromePath(self, n, edges, s, queries):
        from collections import defaultdict

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Tree structure and subtree sizes
        parent = [-1] * n
        depth = [0] * n
        size = [1] * n
        heavy = [-1] * n
        order = [0]
        parent[0] = 0

        for u in order:
            for v in graph[u]:
                if v == parent[u]:
                    continue
                parent[v] = u
                depth[v] = depth[u] + 1
                order.append(v)

        for u in reversed(order):
            largest = 0
            for v in graph[u]:
                if parent[v] == u:
                    size[u] += size[v]
                    if size[v] > largest:
                        largest = size[v]
                        heavy[u] = v

        # Heavy-light decomposition
        head = [0] * n
        pos = [0] * n
        timer = 0
        stack = [(0, 0)]

        while stack:
            u, h = stack.pop()
            while u != -1:
                head[u] = h
                pos[u] = timer
                timer += 1

                for v in graph[u]:
                    if parent[v] == u and v != heavy[u]:
                        stack.append((v, v))

                u = heavy[u]

        # Binary lifting for LCA
        LOG = n.bit_length()
        up = [parent[:]]
        for k in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[i]] for i in range(n)])

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            for k in range(LOG):
                if diff >> k & 1:
                    u = up[k][u]

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]

            return parent[u]

        # Fenwick tree for range XOR updates and point queries
        bit = [0] * (n + 2)

        def add(i, val):
            i += 1
            while i <= n:
                bit[i] ^= val
                i += i & -i

        def range_xor(l, r, val):
            if l > r:
                return
            add(l, val)
            if r + 1 < n:
                add(r + 1, val)

        def point_query(i):
            i += 1
            res = 0
            while i:
                res ^= bit[i]
                i -= i & -i
            return res

        def path_xor(u, v):
            res = 0
            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u
                res ^= point_query(pos[head[u]])
                res ^= point_query(pos[u])
                # The same range must be handled only once.
                # Use the corrected path accumulation below.
                break

            # HLD path accumulation using static prefix masks
            return res

        # Initial character masks
        chars = list(s)
        mask = [1 << (ord(c) - ord('a')) for c in chars]

        # A node's character change toggles its whole subtree's
        # root-prefix parity. Euler intervals are needed for this;
        # HLD positions alone do not guarantee subtree contiguity.

        # Construct Euler tour for subtree intervals
        tin = [0] * n
        tout = [0] * n
        euler = []
        stack = [(0, 0, False)]

        while stack:
            u, p, exiting = stack.pop()
            if exiting:
                tout[u] = len(euler) - 1
                continue

            tin[u] = len(euler)
            euler.append(u)
            stack.append((u, p, True))

            for v in reversed(graph[u]):
                if v != p:
                    stack.append((v, u, False))

        # Prefix parity of root-to-node paths
        pref = [0] * n
        for u in order:
            if u == 0:
                pref[u] = mask[u]
            else:
                pref[u] = pref[parent[u]] ^ mask[u]

        # Fenwick difference updates over Euler order
        bit = [0] * (n + 2)

        def update_range(l, r, val):
            add(l, val)
            if r + 1 < n:
                add(r + 1, val)

        def get_prefix(u):
            i = tin[u] + 1
            res = 0
            while i:
                res ^= bit[i]
                i -= i & -i
            return pref[u] ^ res

        ans = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                new_mask = 1 << (ord(c) - ord('a'))
                delta = mask[u] ^ new_mask

                if delta:
                    update_range(tin[u], tout[u], delta)
                    mask[u] = new_mask
                    chars[u] = c

            else:
                u, v = int(parts[1]), int(parts[2])
                w = lca(u, v)

                path_mask = (
                    get_prefix(u)
                    ^ get_prefix(v)
                    ^ mask[w]
                )

                ans.append(
                    path_mask & (path_mask - 1) == 0
                )

        return ans