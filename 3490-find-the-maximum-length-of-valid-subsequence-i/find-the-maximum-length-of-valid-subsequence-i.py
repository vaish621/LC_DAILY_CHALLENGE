class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        v=0
        m=0

        for j in nums:
            if j%2==0:
                v+=1
            else:
                m+=1
        
        b=nums[0]%2
        a=1

        for j in range(1,len(nums)):
            c=nums[j]%2
            if c!=b:
                a+=1
                b=c
        
        return max(a,max(m,v))
