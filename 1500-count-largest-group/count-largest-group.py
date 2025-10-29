class Solution:
    def countLargestGroup(self, n: int) -> int:
        d=defaultdict(list)
        i=1
        while i<=n:
            su=0
            j=i
            while j>0:
                t=j%10
                su+=t
                j//=10
            d[su].append(i)
            i+=1
        
        ans=0
        tot=0
        for v in d.values():
            if len(v)>ans:
                ans=len(v)
                tot=1
            elif len(v)==ans:
                tot+=1
        
        return tot
            
        