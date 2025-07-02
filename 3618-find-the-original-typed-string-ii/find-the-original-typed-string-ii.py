class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        ff=[]
        i=0

        while i<len(word):
            ch=word[i]
            c=1
            i+=1
            while i<len(word) and word[i]==ch:
                i+=1
                c+=1
            ff.append(c)
        
        n=len(ff)
        M=10**9+7
        P=1

        for f in ff:
            P=(P*f)%M

        if n>=k:
            return P

        dp=[[0]*(k+2) for _ in range(n+1)]

        for c in range(k):
            dp[n][c]=1

        for i in range(n-1,-1,-1):
            pre=[0]*(k+2)

            for h in range(1,k+1):
                pre[h]=(pre[h-1]+dp[i+1][h-1])%M

            for c in range(k):
                l=c+1
                r=c+ff[i]
                if r>=k:
                    r=k-1
                if l<=r:
                    dp[i][c]=(pre[r+1]-pre[l]+M)%M

        return (P-dp[0][0]+M)%M
