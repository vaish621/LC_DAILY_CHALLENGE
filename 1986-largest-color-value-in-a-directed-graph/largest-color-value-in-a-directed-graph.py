class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:

        adj=defaultdict(list)

        for u,v in edges:
            adj[u].append(v)

        dp=[[0]*26 for _ in range(len(colors))]
        self.cycle=False

        visit=[0]*len(colors)

        def dfs(i):
            if visit[i]==1:
                self.cycle=True
                return [0]*26
            
            if visit[i]==2:
                return dp[i]
            
            visit[i]=1

            for j in adj[i]:
                res=dfs(j)
                for c in range(26):
                    dp[i][c]=max(dp[i][c],res[c])
            
            visit[i]=2
            dp[i][ord(colors[i])-ord('a')]+=1
            return dp[i]

        ans=0
        for i in range(len(colors)):
            if visit[i]==0:
                dfs(i)
            ans=max(ans,max(dp[i]))
        
        if self.cycle:
            return -1
        return ans
        