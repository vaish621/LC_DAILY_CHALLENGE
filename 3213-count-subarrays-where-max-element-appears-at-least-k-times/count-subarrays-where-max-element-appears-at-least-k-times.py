class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        ma=max(nums)
        st=0
        en=0
        ans=0
        co=0

        while en<len(nums):
            if nums[en]==ma:
                co+=1
            
            while st<=en and co>=k:
                ans+=len(nums)-en
                if nums[st]==ma:
                    co-=1
                st+=1
            
            en+=1
        
        return ans
        