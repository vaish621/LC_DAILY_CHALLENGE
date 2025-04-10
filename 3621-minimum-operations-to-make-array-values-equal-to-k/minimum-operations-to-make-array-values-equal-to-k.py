class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ma=max(nums)
        t=len(set(nums))
        no=t-1
        m=min(nums)
        if m<k:
            return -1
        else:
            if m==k:
                return no
            else:
                return no+1