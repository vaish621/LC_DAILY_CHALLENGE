from functools import lru_cache
import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        adj=defaultdict(list)

        for i in range(len(edges)):

            adj[edges[i][0]].append([edges[i][1],succProb[i]])
            adj[edges[i][1]].append([edges[i][0],succProb[i]])
        
        probs=[0]*n

        probs[start_node]=1.0

        h=[]

        heapq.heappush(h,[-1.0,start_node])

        while h:
            cost,i=heapq.heappop(h)
            
            cost=-cost

            if i==end_node:
                return cost
            
            for nei,pro in adj[i]:
                ne=cost*pro
                if probs[nei]<ne:
                    probs[nei]=ne
                    heapq.heappush(h,[-ne,nei])
        
        return 0