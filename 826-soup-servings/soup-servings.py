from functools import lru_cache
class Solution:
    def soupServings(self, n: int) -> float:

        if n>4800:
            return 1.0

        i=math.ceil(n/25)
        j=i

        @lru_cache(None)
        def calculate(i,j):

            if i<=0 and j<=0:
                return 0.5
            elif i<=0:
                return 1.0
            elif j<=0:
                return 0.0
            
            ans=0.25*(calculate(i-4,j)+calculate(i-2,j-2)+calculate(i-1,j-3)+calculate(i-3,j-1))

            return ans
        
        res=calculate(i,j)
        
        return res

        