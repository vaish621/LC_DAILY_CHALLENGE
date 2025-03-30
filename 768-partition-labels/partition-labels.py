class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        p=s

        i=0
        seen=[]
        res=[]

        while i<len(s):
            ch=s[i]
            seen.append(s[i])
            ind=p.rfind(ch)
            ans=ind
            j=i+1
            while j<ind:
                if s[j] not in seen:
                    seen.append(s[j])
                    ind1=p.rfind(s[j])
                    ans=max(ans,ind1)
                    ind=ans
                j+=1
        
            res.append(ans-i+1)
            i=ans+1

        return (res)


        