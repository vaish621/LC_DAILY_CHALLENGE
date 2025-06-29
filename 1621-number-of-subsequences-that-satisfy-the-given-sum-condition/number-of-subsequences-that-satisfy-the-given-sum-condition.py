class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:

        nums.sort()
        l=0
        r=len(nums)-1
        ans=0

        while l<=r:
            if nums[l]+nums[r]>target:
                r-=1
            else:
                ans+=pow(2,r-l)
                l+=1
        
        ans=ans%(pow(10,9)+7)

        return (ans)