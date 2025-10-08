import bisect

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:

        full={}
        ans=[-1]*len(rains)
        free=[]

        for i in range(len(rains)):
            if rains[i]!=0:
                if rains[i] in full:
                    t=bisect.bisect_right(free,full[rains[i]])
                    if t==len(free):
                        return []
                    ind=free[t]
                    free.pop(t)
                    ans[ind]=rains[i]
                full[rains[i]]=i
            else:
                bisect.insort(free,i)
                ans[i]=1
        
        return ans
