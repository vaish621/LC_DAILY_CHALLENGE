class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:

        i=0
        ans=0

        while i<len(nums):
            if nums[i]==0:
                co=0
                while i<len(nums) and nums[i]==0:
                    co+=1
                    i+=1
                ans+=((co)*(co+1))//2
            else:
                i+=1
        
        return (ans)

        