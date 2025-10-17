class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        count=nums.count(1)

        if count==0:
            return 0

        for i in range(len(nums)):
            nums.append(nums[i])
        
        st=0
        en=0
        ans=float("inf")
        cur=0

        while en<len(nums):
           
            if nums[en]==1:
                cur+=1
            
            #print(en,st)
            if en-st+1==count:
                ans=min(ans,count-cur)
                if nums[st]==1:
                    cur-=1
                st+=1
            
            en+=1
        
        return ans


        