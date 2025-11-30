class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        tot=sum(nums)

        cut=tot%p

        if cut==0:
            return 0
        
        sh=float("inf")
        seen={0:-1}
        pre=0

        for i,num in enumerate(nums):
            pre=(pre+num)%p
            target=(pre-cut)%p

            if target in seen:
                sh=min(sh,i-seen[target])

            seen[pre]=i
        
        if sh==len(nums) or sh==float("inf"):
            return -1
        
        return sh

