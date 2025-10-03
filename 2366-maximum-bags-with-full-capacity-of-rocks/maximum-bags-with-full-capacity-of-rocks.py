class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:

        diff=[]

        for u,v in zip(capacity,rocks):
            diff.append(u-v)
        
        diff.sort()

        ans=0
        for i in diff:
            if i==0:
                ans+=1
            else:
                if additionalRocks-i>=0:
                    additionalRocks-=i
                    ans+=1
        
        return ans

        