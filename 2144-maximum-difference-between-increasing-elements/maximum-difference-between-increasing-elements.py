class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans=-1
        mi=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>mi:
                ans=max(ans,nums[i]-mi)
            else:
                mi=nums[i]
        return ans