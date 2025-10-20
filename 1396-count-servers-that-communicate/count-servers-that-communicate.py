class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ones = []

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    ones.append([i, j])

        visit = set()

        def dfs(i):
            visit.add(i)
            r, c = ones[i]
            for j in range(len(ones)):
                if j not in visit and (ones[j][0] == r or ones[j][1] == c):
                    dfs(j)

        ans = 0
        for i in range(len(ones)):
            if i not in visit:
                prev = len(visit)
                dfs(i)
                if len(visit) - prev > 1:
                    ans += len(visit) - prev

        return ans
