class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxi=[0]*len(nums)
        maxi[-1]=nums[-1]

        for i in range(len(nums)-2,-1,-1):
            maxi[i]=max(nums[i],maxi[i+1])
        
        minind=-1
        maxind=-1
        mi=float("inf")
        ma=float("-inf")
        ans=0

        for i in range(len(nums)):
            if nums[i]>ma:
                ma=nums[i]
                maxind=i
            
            if nums[i]<mi:
                mi=nums[i]
                minind=i
            
            if minind<maxind:
                mi=float("inf")
                minind=-1
            elif minind!=-1 and maxind!=-1 and maxind<minind:
                if i+1<len(nums):
                    ans=max(ans,(ma-mi)*maxi[i+1])
        
        return ans


        