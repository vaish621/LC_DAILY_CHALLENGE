class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:

        dp=[]
        ans=0

        for i in range(0,k):
            v=[1]*len(nums)
            dp.append(v)
        
        for i in range(len(nums)):
            for j in range(0,i):
                t=(nums[i]+nums[j])%k
                dp[t][i]=max(dp[t][i],dp[t][j]+1)
                ans=max(ans,dp[t][i])
        
        print(ans)
        return ans
        
        