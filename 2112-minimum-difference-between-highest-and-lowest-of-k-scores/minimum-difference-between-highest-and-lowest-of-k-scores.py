class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        nums.sort()

        i=0

        ans=float("inf")

        while i+k-1<len(nums):
            if nums[i+k-1]-nums[i]<ans:
                ans=nums[i+k-1]-nums[i]
            i+=1
        
        return (ans)