
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        
        m=len(str1)
        n=len(str2)

        dp = [[""] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                if str1[i]==str2[j]:
                    dp[i+1][j+1]=dp[i][j]+str1[i]
                else:
                    dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1],key=len)


        lcs=dp[m][n]
        i=0
        j=0
        ans=''
        for ch in lcs:

            while i<len(str1) and str1[i]!=ch:
                ans+=str1[i]
                i+=1
            
            while(j<len(str2) and str2[j]!=ch):
                ans+=str2[j]
                j+=1
            
            
            ans+=ch
            i+=1
            j+=1

            #print(ans)
        
        ans+=str1[i:]+str2[j:]
        return (ans)

        