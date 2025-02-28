from functools import lru_cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        
        @lru_cache(None)
        def rec(i,j):
            if i==len(s1) and j==len(s2):
                return True
            
            if i<len(s1) and s1[i]==s3[i+j] and rec(i+1,j):
                return True
            
            if j<len(s2) and s2[j]==s3[i+j] and rec(i,j+1):
                return True
            
            return False
        
        if len(s1)+len(s2)!=len(s3):
            return False
        return rec(0,0)
        