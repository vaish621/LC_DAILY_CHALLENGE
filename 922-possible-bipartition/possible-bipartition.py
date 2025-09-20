class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        adj=defaultdict(list)

        for u,v in dislikes:
            adj[u].append(v)
            adj[v].append(u)


        color=[-1]*(n+1)

        def bfs(i):
            q=deque()

            q.append(i)

            color[i]=1

            while q:
                t=q.popleft()
                for j in adj[t]:
                    if j!=t:
                        if color[t]==color[j]:
                            return False
                        elif color[j]==-1:
                            color[j]=1-color[t]
                            q.append(j)

            return True
        
        for i in range(1,n+1):
            if color[i]==-1:
                if not bfs(i):
                    return False
        
        return True




        