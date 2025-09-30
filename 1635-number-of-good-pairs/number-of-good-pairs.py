class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        c=collections.Counter(nums)
        ans=0

        for k,v in c.items():
            if v>1:
                ans+=(((v)*(v-1))//2)
        
        return ans

        