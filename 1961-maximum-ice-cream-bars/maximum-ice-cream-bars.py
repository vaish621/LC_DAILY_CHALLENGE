class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        c=collections.Counter(costs)

        s=dict(sorted(c.items()))

        ans=0

        #print(s)

        for k,v in s.items():
            if coins-(k*v)>=0:
                coins-=(k*v)
                ans+=v
            else:
                while coins-k>=0 and v>0:
                    coins-=k
                    v-=1
                    ans+=1
            
        
        return ans
        