class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ma=0

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                t=(nums[i]-nums[j])
                for k in range(j+1,len(nums)):
                    f=t*nums[k]
                    ma=max(ma,f)
        
        return ma
        