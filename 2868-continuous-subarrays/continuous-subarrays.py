class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:

        st=0
        en=0
        ans=0

        d=defaultdict(int)

        while en<len(nums):
            d[nums[en]]+=1
            ma=max(d.keys())
            mi=min(d.keys())

            while st<=en and abs(ma-mi)>2:
                d[nums[st]]-=1
                if d[nums[st]]==0:
                    del d[nums[st]]
                ma=max(d.keys())
                mi=min(d.keys())
                st+=1
            
            ans+=en-st+1
            en+=1
        
        return ans
            

        