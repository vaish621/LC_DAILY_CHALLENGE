from collections import defaultdict

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)

        n = len(colors)
        visit = [0] * n   # 0 = unvisited, 1 = visiting, 2 = done
        dp = [[0] * 26 for _ in range(n)]
        self.cycle = False

        def dfs(i):
            if visit[i] == 1:  # cycle found
                self.cycle = True
                return [0] * 26
            if visit[i] == 2:  # already computed
                return dp[i]

            visit[i] = 1
            for nei in adj[i]:
                res = dfs(nei)
                for c in range(26):
                    dp[i][c] = max(dp[i][c], res[c])

            dp[i][ord(colors[i]) - ord('a')] += 1
            visit[i] = 2
            return dp[i]

        ans = -1
        for i in range(n):
            if visit[i] == 0:
                dfs(i)
            ans = max(ans, max(dp[i]))

        if self.cycle:
            return -1
        return ans
