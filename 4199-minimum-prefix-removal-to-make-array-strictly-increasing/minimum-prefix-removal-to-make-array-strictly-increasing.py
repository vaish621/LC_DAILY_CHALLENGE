class Solution(object):
    def minimumPrefixLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i=len(nums)-1
        le=1

        
        while i-1>=0 and nums[i]>nums[i-1]:
            le+=1
            i-=1
        
        return len(nums)-le
