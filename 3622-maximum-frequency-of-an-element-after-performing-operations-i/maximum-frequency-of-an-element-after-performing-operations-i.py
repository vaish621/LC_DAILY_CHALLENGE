class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        c=collections.Counter(nums)
        ans=max(c.values())

        for i in range(nums[0],nums[-1]+1):
            l=bisect.bisect_left(nums,i-k)
            r=bisect.bisect_right(nums,i+k)-1
            if i in c:
                t=min(r-l+1,c[i]+numOperations)
            else:
                t=min(r-l+1,numOperations)
            ans=max(ans,t)
        
        return ans
        