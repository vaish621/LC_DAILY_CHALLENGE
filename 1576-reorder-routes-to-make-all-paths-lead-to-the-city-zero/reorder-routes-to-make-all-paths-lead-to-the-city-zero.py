class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        adj=defaultdict(list)

        for u,v in connections:
            adj[u].append([v,True])
            adj[v].append([u,False])
        
        visit=set()

        ans=0

        def dfs(i):
            nonlocal ans
            if i in visit:
                return
            
            visit.add(i)

            for j in adj[i]:
                if j[0] not in visit:
                    if j[1]:
                        ans+=1
                    dfs(j[0])
            
        
        dfs(0)

        

        return ans

        


        