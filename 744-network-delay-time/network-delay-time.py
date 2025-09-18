
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        d = defaultdict(list)

        for u, v, w in times:
            d[u].append([v, w])
        
        h = []
        heapq.heappush(h, [0, k])   
        visit = set()
        ans = 0

        while h:
            pa, node = heapq.heappop(h)
            if node in visit:
                continue
            visit.add(node)
            ans = max(ans, pa)
            
            for nei, wt in d[node]:
                if nei not in visit:
                    heapq.heappush(h, [pa + wt, nei])
        
        return ans if len(visit) == n else -1
