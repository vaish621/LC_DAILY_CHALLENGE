from functools import lru_cache
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:

        MOD = 10**9 + 7

        @lru_cache(None)
        def rec(days):
            if days==1:
                return 1
            
            result=0

            for i in range(days-forget+1,days-delay+1):
                if i>0:
                    result=(result+rec(i))%MOD
            
            return result
        
        tot=0

        for i in range(n-forget+1,n+1):
            if i>0:
                tot=(tot+rec(i))%MOD
        
        return tot
        