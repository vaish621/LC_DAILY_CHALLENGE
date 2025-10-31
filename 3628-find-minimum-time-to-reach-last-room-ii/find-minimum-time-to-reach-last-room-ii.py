class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        h=[]
        heapq.heappush(h,[0,0,0,0])

        visit=set()
        visit.add((0,0))

        res=[[float("inf")]*len(moveTime[0]) for _ in range(len(moveTime))]
        dr=[[0,1],[1,0],[0,-1],[-1,0]]
        res[0][0]=0

        while h:
            time,i,j,move=heapq.heappop(h)
            #print(time,i,j)
            for a,b in dr:
                ni,nj=i+a,j+b
                if ni>=0 and ni<len(moveTime) and nj>=0 and nj<len(moveTime[0]) and (ni,nj) not in visit:
                    ad=max(moveTime[ni][nj],time)
                    if move==0:
                        ad+=1
                    else:
                        ad+=2
                    
                    if ad>res[ni][nj]:
                        continue
                    else:
                        visit.add((ni,nj))
                        res[ni][nj]=ad
                        if move==0:
                            heapq.heappush(h,[ad,ni,nj,1])
                        else:
                            heapq.heappush(h,[ad,ni,nj,0])
        

        return res[len(moveTime)-1][len(moveTime[0])-1]



        