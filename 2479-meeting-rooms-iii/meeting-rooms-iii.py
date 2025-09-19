import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        h=[]

        meetings.sort()

        available=[i for i in range(n)]
        heapq.heapify(available)
        time=0
        newend=-1

        d={}

        print(meetings)

        #print(available)

        for s,e in meetings:

            while h and h[0][0]<=s:
                p,rn=heapq.heappop(h)
                heapq.heappush(available,rn)

            if len(available)==0:
                end,rn=heapq.heappop(h)
                available.append(rn)
                newend=end+(e-s)
            
            rn=heapq.heappop(available)

            if newend!=-1:
                heapq.heappush(h,[newend,rn])
                newend=-1
            else:
                heapq.heappush(h,[e,rn])
            if rn not in d:
                d[rn]=1
            else:
                d[rn]+=1
            
            3#rint(h)
            
            ma=0
            res=0

            for k,v in d.items():
                if v>ma:
                    ma=v
                    res=k

        return res
            

            
