class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s=sum(nums)

        if s%k==0:
            return 0
        
        div=s//k

        rem=s-(k*div)

        return rem
        