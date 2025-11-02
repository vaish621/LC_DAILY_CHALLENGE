from functools import lru_cache
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:

        res1=[0]*(len(edges1)+1)

        adj1=defaultdict(list)

        for u,v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)
        
        res2=[0]*(len(edges2)+1)

        adj2=defaultdict(list)

        for u,v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)
        
        def even_count(adj,n):
            color=[-1]*n
            q=deque()
            q.append(0)
            color[0]=0

            while q:
                node=q.popleft()
                for j in adj[node]:
                    if color[j]==-1:
                        color[j]=1-color[node]
                        q.append(j)
            c0=color.count(0)
            c1=n-c0
            return [c0 if color[i]==0 else c1 for i in range(len(color))]

        res1=even_count(adj1,len(edges1)+1)
        res2=even_count(adj2,len(edges2)+1)
        count=max(res2)

        for i in range(len(res1)):
            res1[i]+=count
        
        return res1

