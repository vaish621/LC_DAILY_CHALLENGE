class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def expand(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        ans=""
        for i in range(len(s)):

            ans1=expand(i,i)
            ans2=expand(i,i+1)

            if len(ans1)>len(ans):
                ans=ans1
            
            if len(ans2)>len(ans):
                ans=ans2
        
        return ans

        