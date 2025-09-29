class Solution:
    def maxScore(self, nums: List[int]) -> int:

        nums.sort()
        h=[]
        ap=[]

        i=0

        while i<len(nums) and nums[i]<=0:
            heapq.heappush(h,-nums[i])
            i+=1
        
        while i<len(nums):
            ap.append(nums[i])
            i+=1
        
        while h:
            ap.append(-heapq.heappop(h))

        prefix=[0]*len(ap)
        prefix[0]=ap[0]

        if ap[0]>0:
            co=1
        else:
            co=0

        i=1

        while i<len(nums):
            prefix[i]=prefix[i-1]+ap[i]
            if prefix[i]>0:
                co+=1
            i+=1
        
        return co
        