class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:

        prev=float("-inf")
        ans=0
        nums.sort()
        for i in range(len(nums)):
            if prev<nums[i]-k:
                prev=nums[i]-k
                ans+=1
            elif prev<nums[i]+k:
                prev+=1
                ans+=1
        
        return ans
        