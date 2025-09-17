class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:

        ans=float("inf")

        if n==1 and len(quantities)==1:
            return quantities[0]

        l=1
        r=max(quantities)

        while l<=r:
            m=(l+r)//2
            #print("m",m)
            res=0
            tot=0
            check=[]
            for i in quantities:
                tot+=(i//m)
                rem=i-m*(i//m)
                if rem>0:
                    tot+=1
                k=max(m,rem)
                check.append(k)
            
            if tot<=n:
                r=m-1
                ans=min(check)
            else:
                l=m+1
        
        return ans
            

        