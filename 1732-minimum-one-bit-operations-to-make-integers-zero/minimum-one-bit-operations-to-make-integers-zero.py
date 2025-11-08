from functools import lru_cache
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:


        @lru_cache(None)
        def rec(n):
            print(n)
            if n==0:
                return 0
            
            k=n.bit_length()-1

            return (1<< (k + 1)) - 1 - rec(n ^ (1 << k))
        
        return rec(n)
        