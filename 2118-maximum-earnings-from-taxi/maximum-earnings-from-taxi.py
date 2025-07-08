from functools import lru_cache
class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:


        rides.sort()
        
        start=[ride[0] for ride in rides]

        @lru_cache(None)
        def rec(j):

            if j>=len(rides):
                return 0
            
            nxt=bisect.bisect_left(start,rides[j][1])

            t=(rides[j][1]-rides[j][0]+rides[j][2])+rec(nxt)
            nt=rec(j+1)

            return max(t,nt)
        
        return (rec(0))

        