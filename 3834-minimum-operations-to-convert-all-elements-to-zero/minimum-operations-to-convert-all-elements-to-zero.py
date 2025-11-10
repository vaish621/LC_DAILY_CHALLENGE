class Solution:
    def minOperations(self, nums: List[int]) -> int:

        stack=[]
        ans=0

        for i in range(len(nums)):

            while stack and nums[i]<stack[-1]:
                stack.pop()
            
            if nums[i]==0:
                continue
            
            if len(stack)==0 or nums[i]>stack[-1]:
                stack.append(nums[i])
                ans+=1
        
        return ans
        