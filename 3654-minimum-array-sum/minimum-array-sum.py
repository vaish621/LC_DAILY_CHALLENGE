from functools import lru_cache
class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:

        @lru_cache(None)
        def rec(i,op1,op2):
            if i==len(nums):
                return 0
            
            skip=nums[i]+rec(i+1,op1,op2)

            if op1>0:
                val=math.ceil(nums[i]/2)
                skip=min(skip,val+rec(i+1,op1-1,op2))
            
            if op2>0 and nums[i]-k>=0:
                val=nums[i]-k
                skip=min(skip,val+rec(i+1,op1,op2-1))
            
            if op1>0 and op2>0:
                val=math.ceil(nums[i]/2)
                if val-k>=0:
                    skip=min(skip,val-k+rec(i+1,op1-1,op2-1))
                if nums[i]-k>=0:
                    val=nums[i]-k
                    tp=math.ceil(val/2)
                    skip=min(skip,tp+rec(i+1,op1-1,op2-1))
            
            return skip

            
            

            
        return (rec(0,op1,op2))


        