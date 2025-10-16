from functools import lru_cache
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:


        @lru_cache(None)
        def rec(i):
            print(i)
            if i>=len(energy):
                return 0
            
            return energy[i]+rec(i+k)
        
        ans=float("-inf")

        for i in range(len(energy)):
            ans=max(ans,rec(i))
        
        return ans


        