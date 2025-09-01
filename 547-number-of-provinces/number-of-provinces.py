from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        output=set()
        adj={}

        for i in range(len(isConnected)):
            adj[i+1] = isConnected[i]

        def dfs(s, cycle):
            if s in cycle:
                return
            cycle.add(s)
            output.add(s)
            for j in range(len(adj[s])):
                if j+1 != s and adj[s][j] == 1:  
                    dfs(j+1, cycle)

        ans = 0
        for i in range(len(isConnected)):
            if (i+1) not in output:
                cycle=set()
                dfs(i+1, cycle)
                ans += 1

        return ans
