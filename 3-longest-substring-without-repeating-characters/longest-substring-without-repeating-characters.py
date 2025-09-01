class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        d={}

        i=0
        j=0
        ans=0

        while(i<len(s)):
            if s[i] not in d:
                d[s[i]]=1
            else:
                d[s[i]]+=1
            
            if(i-j+1)==len(d):
                ans=max(ans,i-j+1)
            else:
                while(j<=i and (i-j+1)!=len(d)):
                    d[s[j]]-=1
                    if d[s[j]]==0:
                        del d[s[j]]
                    j+=1
                ans=max(ans,i-j+1)
            i+=1
        
        return ans

        