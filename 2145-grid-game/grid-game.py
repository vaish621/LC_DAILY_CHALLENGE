class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        
        firstrowremsum=sum(grid[0])
        secondrowremsum=0

        minimizedrobot2sum=float("inf")

        for i in range(0,len(grid[0])):

            firstrowremsum-=grid[0][i]
            choose=max(firstrowremsum,secondrowremsum)

            minimizedrobot2sum=min(minimizedrobot2sum,choose)
            secondrowremsum+=grid[1][i]
        
        return minimizedrobot2sum


        