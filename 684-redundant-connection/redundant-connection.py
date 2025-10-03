class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        def dfs(i,par,cycle,adj):
            
            cycle.add(i)

            for j in adj[i]:
                if j==par:
                    continue
                
                if j not in cycle:
                    if dfs(j,i,cycle,adj):
                        return True
                else:
                    return True
            
            return False
        
        adj=defaultdict(list)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

            cycle=set()

            if dfs(u,-1,cycle,adj):
                return [u,v]
        
        return []
        