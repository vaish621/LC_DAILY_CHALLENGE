class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:

        parent=[i for i in range(n)]
        rank=[0]*n

        def find(x):
            if x!=parent[x]:
                parent[x]=find(parent[x])
            return parent[x]
        
        def union(x,y):
            px,py=find(x),find(y)
            if px==py:
                return
            
            if rank[px]<rank[py]:
                parent[px]=py
            elif rank[py]<rank[px]:
                parent[py]=px
            else:
                parent[px]=py
                rank[py]+=1
        
        for u,v,w in edges:
            union(u,v)
        
        comp_and = defaultdict(lambda: (1<<31)-1)

        for u,v,w in edges:
            par=find(u)
            comp_and[par]&=w
        
        ans=[]
        #print(parent)
        for u,v in query:
            if find(u)==find(v):
                ans.append(comp_and[find(u)])
            else:
                ans.append(-1)
            
        return ans

            
            
        