class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:

        rev=defaultdict(int)
        ans=float("inf")

        for i in range(len(nums)):
            if nums[i] in rev:
                ans=min(ans,i-rev[nums[i]])
                rev[nums[i]]=i
            else:
                form=0
                org=nums[i]

                while org>0:
                    rem=org%10
                    form=form*10+rem
                    org//=10
                
                rev[form]=i
        
            #print(rev)
        
        if ans==float("inf"):
            return -1
        
        return ans