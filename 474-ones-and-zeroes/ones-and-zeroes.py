from functools import lru_cache
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        @lru_cache(None)
        def rec(i,o,z):
            if i>=len(strs) or (o==0 and z==0):
                return 0
            

            nt=rec(i+1,o,z)
            #take
            o1=strs[i].count('1')
            z1=strs[i].count('0')
            take=float("-inf")

            if o>=o1 and z>=z1:
                take=1+rec(i+1,o-o1,z-z1)
            
            return max(take,nt)
        

        return rec(0,n,m)


        