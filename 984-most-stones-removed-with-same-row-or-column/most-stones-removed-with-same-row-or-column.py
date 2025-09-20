class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        visit=set()


        def dfs(i):
            visit.add(i)
            r=stones[i][0]
            c=stones[i][1]


            for j in range(len(stones)):
                if j not in visit and (stones[j][0]==r or stones[j][1]==c):
                    dfs(j)
        
        g=0
        for i in range(len(stones)):
            if i not in visit:
                visit.add(i)
                dfs(i)
                g+=1
        
        return len(stones)-g


        