class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        h=[]

        heapq.heappush(h,[grid[0][0],0,0])
        d=sorted((q,i) for i,q in enumerate(queries))
        points=0
        ans=[0]*len(queries)
        visit=set()
        visit.add((0,0))

        for q,ind in d:
            while h and h[0][0]<q:
                cost,i,j=heapq.heappop(h)
                points+=1
                for dr,dc in [[-1,0],[1,0],[0,1],[0,-1]]:
                    tc,tm=i+dr,j+dc
                    if 0<=tc<len(grid) and 0<=tm<len(grid[0]) and (tc,tm) not in visit:
                        visit.add((tc,tm))
                        heapq.heappush(h,[grid[tc][tm],tc,tm])
            
            
            ans[ind]=points
        
        return ans



        