class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        
        prev=-1
        ma=1
        ans=0

        


        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                ma+=1
            else:
                
                ans=max(ans,ma//2)
                if prev!=-1:
                    ans=max(ans,min(prev,ma))
                prev=ma
                ma=1
        
        if prev==-1:
            prev=1
        
        ans=max(ans,ma//2)
        
        ans=max(ans,min(ma,prev))

        return ans