class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        self.ans=0

        def rec(i,cu):
            if i>=len(nums):
                self.ans+=cu
                return
            
            rec(i+1,cu^nums[i])
            rec(i+1,cu)
        
        rec(0,0)
        return self.ans
                
        