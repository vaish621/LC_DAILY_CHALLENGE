class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        graph={i:[] for i in range(n)}

        if n==1:
            return [0]

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        leaves=deque()
        edgecnt={}

        for u,v in graph.items():
            if len(v)==1:
                leaves.append(u)
            edgecnt[u]=len(v)
        

        while leaves:
            if n<=2:
                return list(leaves)
            for i in range(len(leaves)):
                node=leaves.popleft()
                n-=1
                for nei in graph[node]:
                    edgecnt[nei]-=1
                    if edgecnt[nei]==1:
                        leaves.append(nei)

        
        