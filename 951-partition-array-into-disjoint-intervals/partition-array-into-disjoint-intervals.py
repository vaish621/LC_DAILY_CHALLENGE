class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:

    

        pre=[float('inf')]*len(nums)

        pre[len(pre)-1]=nums[len(nums)-1]

        i=len(nums)-2

        while i>=0:
            pre[i]=min(nums[i],pre[i+1])
            i-=1
        
        ma=nums[0]
        i=0

        while i<len(nums)-1:
           
            ma=max(ma,nums[i])
        
            if ma<=pre[i+1]:
                return i+1
            
            i+=1


        return -1

        