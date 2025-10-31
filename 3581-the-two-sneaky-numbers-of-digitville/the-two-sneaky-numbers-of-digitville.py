class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        c=collections.Counter(nums)
        ans=[]

        for k,v in c.items():
            if v==2:
                ans.append(k)
        
        return ans
        