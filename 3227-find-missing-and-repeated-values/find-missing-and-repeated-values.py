class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        ans=[]

        d={}

        t=len(grid)*len(grid[0])

        p=[0]*(t+1)

        for i in grid:
            for j in i:
                if j not in d:
                    d[j]=1
                else:
                    d[j]+=1
                    if len(ans)==0:
                        ans.append(j)
                p[j]=1
        
        for i in range(1,len(p)):
            if p[i]!=1:
                ans.append(i)
        return ans
        