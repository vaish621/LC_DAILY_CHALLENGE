class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums=set(nums)
        ans=0
        for i in nums:
            if i-1 not in nums:
                ch=i
                le=0
                while ch in nums:
                    le+=1
                    ch+=1
                ans=max(ans,le)
        return ans
