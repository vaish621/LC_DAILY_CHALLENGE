class Solution:
    def countElements(self, nums: List[int], k: int) -> int:

        nums.sort()
        ans=0


        for i in range(len(nums)):
            l=bisect.bisect_right(nums,nums[i])

            rem=len(nums)-l

            if rem>=k:
                ans+=1
        
        return ans

        