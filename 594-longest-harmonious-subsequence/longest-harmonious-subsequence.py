class Solution:
    def findLHS(self, nums: List[int]) -> int:
        ck=collections.Counter(nums)

        ans=0

        for j in ck:
            if j+1 in ck:
                ans=max(ans,ck[j]+ck[j+1])
        
        return (ans)
        