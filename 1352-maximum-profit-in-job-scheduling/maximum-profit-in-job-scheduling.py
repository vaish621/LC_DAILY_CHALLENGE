import bisect
from functools import lru_cache
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        jobs=sorted(zip(startTime,endTime,profit))
        start=[job[0] for job in jobs]


        @lru_cache(None)
        def dfs(i):
            if i>=len(start):
                return 0
            
            sk=dfs(i+1)

            s,e,p=jobs[i]
            nxt=bisect.bisect_left(start,e)
            t=p+dfs(nxt)

            return max(sk,t)
        
        return dfs(0)