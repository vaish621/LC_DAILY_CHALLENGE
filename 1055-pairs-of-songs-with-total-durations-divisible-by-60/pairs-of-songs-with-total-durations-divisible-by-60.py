class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        d=defaultdict(int)

        for i in time:
            d[i%60]+=1
        
        ans=0

        ans+=((d[0]*(d[0]-1))//2)
        
        ans+=(d[30]*(d[30]-1))//2

        for i in range(1,30):
            ans+=d[i]*d[60-i]
        
        return ans
        