class Solution:
    def findMin(self, nums: List[int]) -> int:

        l=0

        r=len(nums)-1

        ans=float("inf")

        while l<r:
            mid=(l+r)//2
            ans=min(ans,nums[mid])

            if nums[0]<=nums[mid]:
                if nums[0]>nums[-1]:
                    l=mid+1
                else:
                    r=mid-1
            else:
                if nums[0]<=nums[-1]:
                    l=mid+1
                else:
                    r=mid-1
        
        return min(nums[l],ans)
                
        