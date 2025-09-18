class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        nums=set(nums)
        ans=-1

        for i in nums:
            if i>1:
                if (i-1) not in nums:
                    ans=i-1
                    break
        
        st=1

        if ans==-1:
            m=max(nums)
            if m<0:
                return 1
            else:
                ans=m+1

        while st<ans:
            if st not in nums:
                return st
            st+=1
        
        return ans

        