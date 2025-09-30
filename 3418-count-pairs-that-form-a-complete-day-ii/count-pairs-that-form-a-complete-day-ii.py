class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:

        d=defaultdict(int)

        for i in hours:
            d[i%24]+=1
        
        ans=0
        
        ans+=(d[0]*(d[0]-1))//2
        ans+=(d[12]*(d[12]-1))//2

        for i in range(1,12):
            ans+=d[i]*d[24-i]
        
        return ans