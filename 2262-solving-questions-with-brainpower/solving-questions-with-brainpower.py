from functools import lru_cache
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        @lru_cache(None)
        def rec(i):
            if i>=len(questions):
                return 0
            
            t=0
            nt=0
            t+=questions[i][0]+rec(i+questions[i][1]+1)
            nt+=rec(i+1)

            return max(t,nt)
        
        return (rec(0))
        