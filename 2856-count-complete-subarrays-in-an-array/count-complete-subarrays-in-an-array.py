class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:

        st=0
        en=0
        ans=0
        le=len(set(nums))
        d=defaultdict(int)
        length=len(nums)


        while en<len(nums):
            d[nums[en]]+=1

            while st<=en and len(d)==le:
                d[nums[st]]-=1
                if d[nums[st]]==0:
                    del d[nums[st]]
                st+=1
            
            ans+=en-st+1
            en+=1
        
        fi=(length*(length+1))//2
        return fi-ans
        
        



        