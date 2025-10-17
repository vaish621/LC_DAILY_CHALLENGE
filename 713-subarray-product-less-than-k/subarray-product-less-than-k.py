class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        st=0
        en=0

        
        su=1
        ans=0

        while en<len(nums):
            
            su*=nums[en]

            while st<=en and su>=k:
                su//=nums[st]
                st+=1
            
            
            ans+=en-st+1
            en+=1
        
        return ans


        