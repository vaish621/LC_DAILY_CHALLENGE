class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        fre=0
        num=0

        for i in nums:
            if fre==0:
                fre=1
                num=i
            elif i==num:
                fre+=1
            else:
                fre-=1
                if fre==0:
                    fre=1
                    num=i
        
        if nums.count(num) * 2 <= len(nums):
            return -1 
        
        pre=[0]*len(nums)

        for i in range(len(nums)):
            if nums[i]==num:
                pre[i]=pre[i-1]+1
            else:
                pre[i]=pre[i-1]
        
        
        i=0

        while i<len(nums)-1:
            le=pre[i]
            re=pre[-1]-pre[i]
            if le*2>(i+1) and re*2>(len(nums)-i-1):
                return i
            i+=1
        return -1
        