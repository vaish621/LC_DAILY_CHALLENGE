class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans=0
        i=0
        while i<len(nums):
            j=i
            while j<len(nums) and nums[j]-nums[i]<=k:
                j+=1
            ans+=1
            i=j
        return ans
    



            