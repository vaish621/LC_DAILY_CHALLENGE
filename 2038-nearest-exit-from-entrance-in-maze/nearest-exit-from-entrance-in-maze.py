class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        q=deque()

        q.append([entrance[0],entrance[1]])

        visit=set()

        visit.add((entrance[0],entrance[1]))

        steps=0

        while q:
            for _ in range(len(q)):
                i,j=q.popleft()

                if [i,j]!=entrance and (i in [0,len(maze)-1] or j in [0,len(maze[0])-1]):
                    return steps

                for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                    ni,nj=i+dr,j+dc

                    if (ni>=0 and ni<len(maze)) and (nj>=0 and nj<len(maze[0])):
                        if maze[ni][nj]=='.' and (ni,nj) not in visit:
                            q.append([ni,nj])
                            visit.add((ni,nj))
            steps+=1
        
        return -1


        


