class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac , atl= set(),set()

        r,c=len(heights),len(heights[0])

        def dfs(r,c,vis,prev):

            if (r,c) in vis or r<0 or r>=len(heights) or c<0 or c>=len(heights[0]) or heights[r][c]<prev:
                return
            
            vis.add((r,c))

            dfs(r+1,c,vis,heights[r][c])
            dfs(r,c+1,vis,heights[r][c])
            dfs(r-1,c,vis,heights[r][c])
            dfs(r,c-1,vis,heights[r][c])
        
        for i in range(r):
            dfs(i,0,pac,heights[i][0])
            dfs(i,c-1,atl,heights[i][c-1])
        
        for i in range(c):
            dfs(0,i,pac,heights[0][i])
            dfs(r-1,i,atl,heights[r-1][i])
        
        res=[]

        for i in range(r):
            for j in range(c):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])
        
        return res

            

            


        