class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        d=defaultdict(list)

        for i,j,k in roads:
            d[i].append([j,k])
            d[j].append([i,k])
        
        self.ma=float('inf')
        vis=[False]*(n+1)
        def rec(i):
         
            vis[i]=True

            for j in d[i]:
                self.ma=min(self.ma,j[1])
                if not vis[j[0]]:
                    rec(j[0])

        
        rec(1)
        return (self.ma)
