class Solution(object):
    def longestSubsequence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        o=0
        z=0
        c=0
        su=0
        b=-1

        j=len(s)-1

        while j>=0:
            if s[j]=='0':
                z+=1
                b+=1
            else:
                b+=1
                f=pow(2,b)
                if f+su<=k:
                    su+=f
                    c+=1
            j-=1
    
        return z+c