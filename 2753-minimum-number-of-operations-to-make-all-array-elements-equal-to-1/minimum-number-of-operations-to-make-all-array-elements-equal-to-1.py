class Solution:
    def minOperations(self, nums: List[int]) -> int:

        count1=0

        for i in nums:
            if i==1:
                count1+=1
        
        if count1>0:
            return len(nums)-count1
        
        ans=float("inf")
        
        for i in range(len(nums)):
            st=nums[i]
            for j in range(i+1,len(nums)):
                st=math.gcd(st,nums[j])
                if st==1:
                    ans=min(ans,j-i)
                    break
        
        if ans==float("inf"):
            return -1
        
        return ans+(len(nums)-1)
        


        

        
            
            