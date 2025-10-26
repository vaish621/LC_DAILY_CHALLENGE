class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        ma=[]
        mi=[]
        co=0

        for i in nums:
            if i<0:
                heapq.heappush(ma,i)
                heapq.heappush(mi,-i)
            else:
                heapq.heappush(ma,-i)
                heapq.heappush(mi,i)
        
        ans=0
        fl=0
        while co<len(nums):
            if fl==0:
                ad=-heapq.heappop(ma)
                ans+=ad*ad
                fl=1
            else:
                ad=heapq.heappop(mi)
                ans-=ad*ad
                fl=0
            co+=1
        
        return ans
            
        