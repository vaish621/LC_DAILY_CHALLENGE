class Solution:
    def partitionString(self, s: str) -> int:

        lastseen=[-1]*26

        start=0
        ans=1

        for i in range(len(s)):
            if lastseen[ord(s[i])-ord('a')]==-1:
                lastseen[ord(s[i])-ord('a')]=i
            else:
                if lastseen[ord(s[i])-ord('a')]>=start:
                    ans+=1
                    start=i
                    lastseen[ord(s[i])-ord('a')]=i
                else:
                    lastseen[ord(s[i])-ord('a')]=i
            #print(lastseen)
        
        return ans

        