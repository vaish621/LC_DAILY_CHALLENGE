class Solution:
    def minOperations(self, nums: List[int]) -> int:

        isflipped=[False]*len(nums)

        flipcount=0
        ans=0

        for i in range(len(nums)):
            if i>=3 and isflipped[i-3]:
                flipcount-=1
            
            if flipcount%2==nums[i]:
                if i+3>len(nums):
                    return -1
                flipcount+=1
                ans+=1
                isflipped[i]=True
        
        return ans
        