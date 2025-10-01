class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:

        cnt=[0]*26
        mod=pow(10,9)+7

        for i in s:
            cnt[ord(i)-ord('a')]+=1

        while t>0:
            tmp=[0]*26
            for i in range(26):
                if cnt[i]>0:
                    if i==25:
                        tmp[0]+=(cnt[i])%mod
                        tmp[1]+=cnt[i]%mod
                    else:
                        tmp[i+1]+=cnt[i]%mod
            cnt=tmp
            t-=1
        
        return sum(cnt)%mod