class Solution(object):
    def finalElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ma=max(nums)

        ind=nums.index(ma)

        if ind==0 or ind==len(nums)-1:
            return ma
        
        if nums[0]>nums[-1]:
            return nums[0]
        
        return nums[-1]