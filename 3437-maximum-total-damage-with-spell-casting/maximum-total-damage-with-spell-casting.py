import bisect
from functools import lru_cache
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        power.sort()

        c=collections.Counter(power)

        @lru_cache(None)
        def rec(i):
            if i==len(power):
                return 0
            
            skip=rec(i+1)
            
            
            nxt=bisect.bisect_right(power,power[i]+2)

            take=(power[i]*c[power[i]])+rec(nxt)

            return max(take,skip)
        
        return (rec(0))


        