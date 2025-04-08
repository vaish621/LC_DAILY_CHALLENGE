class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        ans=0

        i=0
        while(i<(len(nums)-2) and len(set(nums))!=len(nums)):
            ans+=1
            nums=nums[(i+3):len(nums)]
            #print(nums)
            i=0
            

        if(len(set(nums))!=len(nums)):
            ans+=1

        return ans
            
        