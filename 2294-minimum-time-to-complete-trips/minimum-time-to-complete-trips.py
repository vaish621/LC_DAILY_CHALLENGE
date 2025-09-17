class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:

        if len(time)==1:
            return time[0]*totalTrips

        l=1
        r=min(time) * totalTrips

        ans=float("inf")

        while l<=r:
            m=(l+r)//2
            tot=0

            for i in time:
                tot+=(m//i)
            
            if tot>=totalTrips:
                r=m-1
                ans=min(ans,m)
            else:
                l=m+1
        
        return ans if ans!=float("inf") else -1
        