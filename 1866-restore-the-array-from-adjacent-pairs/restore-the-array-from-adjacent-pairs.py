from collections import defaultdict

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for u, v in adjacentPairs:
            adj[u].append(v)
            adj[v].append(u)

        
        start = None
        for k, v in adj.items():
            if len(v) == 1:
                start = k
                break

        ans = []
        visited = set()

        def dfs(node, parent):
            ans.append(node)
            for nei in adj[node]:
                if nei != parent:
                    dfs(nei, node)

        dfs(start, -1)
        return ans
