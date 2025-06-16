class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD=10**9+7
        pr=collections.Counter()
        su=collections.Counter(nums)

        ans=0

        for i in range(len(nums)):
            su[nums[i]]-=1
            ans=(ans+pr[nums[i]*2]*su[nums[i]*2])%MOD
            pr[nums[i]]+=1

        return ans