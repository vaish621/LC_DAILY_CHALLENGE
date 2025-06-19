
class Solution:
    def minimizeMax(self,nums:List[int],p:int)->int:
        nums.sort()
        l=0
        r=nums[-1]-nums[0]
        while l<r:
            m=(l+r)//2
            c=0
            i=0
            while i<len(nums)-1:
                if nums[i+1]-nums[i]<=m:
                    c+=1
                    i+=2
                else:
                    i+=1
                    
            if c>=p:
                r=m
            else:
                l=m+1
        return l
