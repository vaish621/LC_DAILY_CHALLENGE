from functools import lru_cache
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:


        events.sort()
        starts=[event[0] for event in events]
        

        @lru_cache(maxsize=None)
        def rec(j,k):
            

            if j>=len(events) or k==0:

                return 0
            
            nxt=bisect.bisect_right(starts,events[j][1])
            
        
            t=events[j][2]+rec(nxt,k-1)
            
            nt=rec(j+1,k)

            return max(t,nt)
        
        return rec(0,k)
        
        