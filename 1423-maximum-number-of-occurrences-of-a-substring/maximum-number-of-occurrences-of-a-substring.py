class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        d={}

        def rec(i):

            if i>len(s)-minSize:
                return
            
            su=s[i:i+minSize]

            if len(set(su))<=maxLetters:
                if su not in d:
                    d[su]=1
                else:
                    d[su]+=1
            rec(i+1)
        
        rec(0)
        if len(d)==0:
            return 0
        m=max(d.values())
        return m

        