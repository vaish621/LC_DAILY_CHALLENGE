class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        adj=defaultdict(list)

        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)

        parent=[i for i in range(n)]
        rank=[0]*n

        if len(connections)<n-1:
            return -1

        def find(x):
            if x==parent[x]:
                return x
            parent[x]=find(parent[x])
            return parent[x]

        
        def union(x,y):
            px,py=find(x),find(y)

            if px==py:
                return
            elif rank[px]>rank[py]:
                parent[py]=px
            elif rank[py]>rank[px]:
                parent[px]=py
            else:
                parent[px]=py
                rank[py]+=1
        
        for u,v in adj.items():
            for j in v:
                union(u,j)
            

        
        s=set(find(i) for i in range(n))

        return len(s)-1
        