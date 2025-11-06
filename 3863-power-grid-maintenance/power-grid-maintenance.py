
class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:

        parent=[i for i in range(c+1)]
        rank=[0]*(c+1)

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
                parent[py]=px
                rank[px]+=1
            
            return

        for u,v in connections:
            union(u,v)
        
        heaps=defaultdict(list)

        for i in range(1,c+1):
            heaps[find(i)].append(i)
        
        for root in heaps:
            heapq.heapify(heaps[root])
        
        ans=[]
        offline=set()
        
        for u,v in queries:
            if u==1:
                if v in offline:
                    par=find(v)
                    h=heaps[par]
                    while h and h[0] in offline:
                        heapq.heappop(h)
                    if h:
                        ans.append(h[0])
                    else:
                        ans.append(-1)
                else:
                    ans.append(v)
            else:
                offline.add(v)
        
        return ans
                    

        
        