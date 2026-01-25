class Solution(object):
    def rotateElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        

        pos=[]

        for i in nums:
            if i>=0:
                pos.append(i)
        

        n=len(pos)
        if n>0:
            k=k%n
            ndp=pos[k:]+pos[:k]
            j=0
            
            ans=[0]*len(nums)

            for i in range(len(nums)):
                if nums[i]>=0:
                    ans[i]=ndp[j]
                    j+=1
                else:
                    ans[i]=nums[i]
            
            return ans
        else:
            return nums


        
        