class Solution(object):
    def absDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        
        a=0

        i=0

        while i<k:
            a+=nums[i]
            i+=1
        
        i=len(nums)-1
        cnt=0
        b=0

        while cnt<k:
            b+=nums[i]
            i-=1
            cnt+=1
        
        return abs(a-b)
