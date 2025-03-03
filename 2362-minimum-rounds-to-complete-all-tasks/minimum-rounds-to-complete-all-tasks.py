from collections import Counter
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:

        co=Counter(tasks)
        ans=0

        for k in co:
            if co[k]==1:
                return -1
            else:
                if co[k]==2:
                    ans+=1
                else:
                    t=co[k]//3
                    s=co[k]-(t*3)
                    if s==1:
                        t-=1
                        co[k]=co[k]-(t*3)
                        ans+=t
                        f=co[k]//2
                        ans+=f
                    else:
                        ans+=t
                        if s==2:
                            ans+=1
        return (ans)