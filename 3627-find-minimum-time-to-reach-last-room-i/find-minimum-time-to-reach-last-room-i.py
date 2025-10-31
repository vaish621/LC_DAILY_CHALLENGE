class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        
        h=[]
        visit=set()
        heapq.heappush(h,[0,0,0])
        res=[]
        visit.add((0,0))
        for i in range(len(moveTime)):
            add=[float("inf")]*len(moveTime[0])
            res.append(add)
        dr=[[1,0],[0,1],[-1,0],[0,-1]]
        res[0][0]=0

        while h:
            time,i,j=heapq.heappop(h)
            for a,b in dr:
                ni,nj=i+a,j+b
                if ni>=0 and ni<len(moveTime) and nj>=0 and nj<len(moveTime[0]) and (ni,nj) not in visit:
                    visit.add((ni,nj))
                    ad=max(moveTime[ni][nj],time)
                    if ad+1>res[ni][nj]:
                        continue
                    else:
                        res[ni][nj]=ad+1
                        heapq.heappush(h,[ad+1,ni,nj])
        
        return res[len(moveTime)-1][len(moveTime[0])-1]
            
            
           
        
        