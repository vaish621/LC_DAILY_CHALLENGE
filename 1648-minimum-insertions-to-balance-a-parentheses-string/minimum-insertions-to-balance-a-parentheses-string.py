class Solution:
    def minInsertions(self, s: str) -> int:

        need=0
        ans=0

        for i in s:
            if i=='(':
                need+=2

                if need%2!=0:
                    ans+=1
                    need-=1
            else:
                need-=1
                if need<0:
                    ans+=1
                    need=1
        
        return ans+need

        