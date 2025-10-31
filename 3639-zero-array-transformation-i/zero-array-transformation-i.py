class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:

        beg=[0]*len(nums)

        for st,en in queries:
            beg[st]+=1
            if en+1<len(nums):
                beg[en+1]-=1
        
        for i in range(1,len(beg)):
            beg[i]+=beg[i-1]
        
        for i in range(len(beg)):
            if beg[i]<nums[i]:
                return False
        
        return True
        