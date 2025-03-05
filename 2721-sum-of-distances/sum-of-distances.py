class Solution:
    def distance(self, nums: List[int]) -> List[int]:

        d1={}

        for i in range(len(nums)):
            if nums[i] not in d1:
                d1[nums[i]]=[]
            d1[nums[i]].append(i)
        
        ans=[0]*len(nums)

        for v in d1.values():
            s=sum(v)
            p=0

            for j,ind in enumerate(v):
                le=j*ind-p
                re=(s-p-ind)-(len(v)-j-1)*ind
                ans[ind]=le+re
                p+=ind
        return ans


        