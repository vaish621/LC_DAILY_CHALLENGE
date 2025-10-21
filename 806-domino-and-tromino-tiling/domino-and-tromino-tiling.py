from functools import lru_cache
class Solution:
    def numTilings(self, n: int) -> int:

        mod=10**9 + 7

        @lru_cache(None)
        def rec(n):
            if n==1 or n==2:
                return n
            
            if n==3:
                return 5
            
            return ((2*rec(n-1))%mod+rec(n-3)%mod)%mod
        
        return rec(n)
        