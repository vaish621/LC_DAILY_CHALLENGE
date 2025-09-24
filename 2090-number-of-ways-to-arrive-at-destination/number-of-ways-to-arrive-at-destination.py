class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:


        graph=defaultdict(list)

        MOD = 10**9 + 7

        for u,v,w in roads:
            graph[u].append([v,w])
            graph[v].append([u,w])

        pq=[]

        
        dist=[float("inf")]*n

        dist[0]=0

        ways=[0]*n

        ways[0]=1


        heapq.heappush(pq,[0,0])


        while pq:
            cost,node=heapq.heappop(pq)

            if cost>dist[node]:
                continue

            for j in graph[node]:
                if dist[node]+j[1]<dist[j[0]]:
                    dist[j[0]]=dist[node]+j[1]
                    ways[j[0]]=ways[node]
                    heapq.heappush(pq,[dist[j[0]],j[0]])
                elif dist[node]+j[1]==dist[j[0]]:
                    ways[j[0]]=(ways[j[0]]+ways[node])% MOD
        
        return ways[n-1]% MOD

