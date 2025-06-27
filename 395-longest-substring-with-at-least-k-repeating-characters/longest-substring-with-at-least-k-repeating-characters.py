class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        d={}

        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        
        for ke,v in d.items():
            if v<k:
                return max(self.longestSubstring(sub,k) for sub in s.split(ke))
                    #print(t)
        
        return len(s)