class Solution(object):
    def minimumK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l=1
        h=sum(nums)
        ans=0

        while l<=h:
            mid=(l+h)//2
            co=0
            
            for i in nums:
                if i%mid==0:
                    t=(i//mid)
                    if t==0:
                        co+=1
                    else:
                        co+=t
                else:
                    t=i//mid
                    co+=(t+1)
                    
            
            print(mid,co)
            if co>mid*mid:
                l=mid+1
            else:
                ans=mid
                h=mid-1
        
        return (ans)
        

        