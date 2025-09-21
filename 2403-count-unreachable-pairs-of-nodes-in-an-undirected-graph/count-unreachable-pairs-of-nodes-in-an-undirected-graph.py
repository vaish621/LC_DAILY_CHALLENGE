from functools import lru_cache
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:


        adj=defaultdict(list)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit=set()
        
       
        def dfs(i):
            q=deque()
            q.append(i)
            visit.add(i)
            size=1

            while q:
                t=q.popleft()
                for k in adj[t]:
                    if k not in visit :
                        q.append(k)
                        visit.add(k)
                        size+=1
            return size
        
        visit=set()
        visited=0
        ans=0
        res=0

        for i in range(n):
            if i not in visit:
                ans=dfs(i)
                visited+=ans
                res+=ans*(n-visited)


        return res

        