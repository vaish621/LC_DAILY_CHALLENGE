class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:

        mod=pow(10,9)+7

        c=collections.Counter(deliciousness)
        ma=max(deliciousness)

        visit=set()
        ans=0

        
        for k,v in c.items():
            for j in range(0,22):
                p=pow(2,j)
                if p>k:
                    sub=p-k
                
                    if sub in c and sub==k:
                        if k==0:
                            continue
                        if (k,k) not in visit and c[k]!=1:
                            visit.add((k,k))
                            val=c[sub]
                            ans+=((val*(val-1))//2)%mod
                            #print(ans)
                    elif sub in c:
                        p1=c[k]
                        p2=c[sub]
                        if (sub,k) not in visit:
                            visit.add((k,sub))
                            ans+=(p1*p2)%mod
                else:
                    if p>2*ma:
                        break

                

                
        return ans
                



            