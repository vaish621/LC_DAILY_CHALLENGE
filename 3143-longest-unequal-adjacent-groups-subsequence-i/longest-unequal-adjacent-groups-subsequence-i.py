from functools import lru_cache
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:

        @lru_cache(None)
        def rec(i,prev):
            if i==len(words):
                return []
            
            skip=rec(i+1,prev)

            
            if prev==-1 or groups[prev]!=groups[i]:
                take=[words[i]]+rec(i+1,i)
                if len(take)>len(skip):
                    skip=take
            
            return skip
        
        return rec(0,-1)


        