class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:

        st=0
        en=0
        ans=0
        mask=0

        

        while en<len(nums):

            while st<=en and mask&nums[en]!=0:
                mask=mask^nums[st]
                st+=1
            
            mask=mask|nums[en]
            ans=max(ans,en-st+1)
            en+=1
        
        return ans