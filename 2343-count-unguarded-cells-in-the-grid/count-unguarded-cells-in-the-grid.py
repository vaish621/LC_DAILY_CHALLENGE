class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:

        grid=[[0]*n for _ in range(m)]

        wall=set()

        for st,en in walls:
            wall.add((st,en))
        
        guard=set()

        for st,en in guards:
            guard.add((st,en))

        def marking(i,j):
            
            #right row
            en=j+1
            while en<n:
                if (i,en) in guard or (i,en) in wall:
                    break
                grid[i][en]=1
                en+=1
            
            #left row

            en=j-1
            while en>=0:
                if (i,en) in guard or (i,en) in wall:
                    break
                grid[i][en]=1
                en-=1
            
            #top col

            en=i-1

            while en>=0:
                if (en,j) in guard or (en,j) in wall:
                    break
                grid[en][j]=1
                en-=1
            
            #bot col
            en=i+1
            while en<m:
                if (en,j) in guard or (en,j) in wall:
                    break
                grid[en][j]=1
                en+=1
        

        for st,en in guards:
            marking(st,en)
            grid[st][en]=2
        
        for st,en in walls:
            grid[st][en]=-1
        
        ans=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    ans+=1

        return ans
            
            
                
                

            
           

