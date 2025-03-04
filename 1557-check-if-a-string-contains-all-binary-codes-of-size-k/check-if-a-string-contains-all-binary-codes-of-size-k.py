from functools import lru_cache
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:

        st=set()

        
        i=0
        for i in range(len(s)-1):
            t=s[i:i+k]
            if len(t)==k:
                st.add(t)
        
        if k==1:
            t=s[i+1:len(s)]
            if len(t)==k:
                st.add(t)
        if len(st)==pow(2,k):
            return True
        else:
            return False