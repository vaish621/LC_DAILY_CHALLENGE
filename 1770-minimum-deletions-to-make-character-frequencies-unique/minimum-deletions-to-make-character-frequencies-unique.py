class Solution:
    def minDeletions(self, s: str) -> int:

        c=collections.Counter(s)

        v=list(c.values())

        v.sort()

        ans=0

        for i in range(len(v)-1):
            if v[i]==v[i+1] and (v[i]!=-1 and v[i+1]!=-1):
                ne=v[i]
                co=0
                while ne in v:
                    ne-=1
                    co+=1
                if ne<0:
                    ans+=v[i]
                    v[i]=-1
                else:
                    ans+=co
                    v[i]=ne
        
        return ans

        