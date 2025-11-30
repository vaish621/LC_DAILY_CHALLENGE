class Solution:
    def maxDistinct(self, s: str) -> int:

        seen=set()
        ans=0

        for i in range(len(s)):
            if s[i] not in seen:
                seen.add(s[i])
                ans+=1
        
        if ans==0:
            return 1
        
        return ans
        