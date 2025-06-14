from collections import deque
from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        if source == target:
            return 0

        d = {}
        for i in range(len(routes)):
            for stop in routes[i]:
                if stop not in d:
                    d[stop] = []
                d[stop].append(i)

        if source not in d or target not in d:
            return -1

        q = deque()
        vis = [False] * len(routes)

        for v in d[source]:
            q.append(v)
            vis[v] = True

        b = 1
        while q:
            for _ in range(len(q)):
                ind = q.popleft()
                for stop in routes[ind]:
                    if stop == target:
                        return b
                    for bs in d[stop]:
                        if not vis[bs]:
                            vis[bs] = True
                            q.append(bs)
            b += 1

        return -1
