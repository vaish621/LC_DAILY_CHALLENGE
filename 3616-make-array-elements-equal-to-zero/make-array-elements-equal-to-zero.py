class Solution:
    def countValidSelections(self, nums: List[int]) -> int:

        
        pr=[0]*len(nums)
        pr[0]=nums[0]

        for i in range(1,len(nums)):
            pr[i]=pr[i-1]+nums[i]
        
        suf=[0]*len(nums)
        suf[-1]=nums[-1]

        for i in range(len(nums)-2,-1,-1):
            suf[i]=suf[i+1]+nums[i]
        
        ans=0
        
        for i in range(len(nums)):
            if nums[i]==0:
                left=pr[i]
                right=suf[i]

                if left==right:
                    ans+=2
                elif left-1==right or left==right-1:
                    ans+=1

            
        return ans
        