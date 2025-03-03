class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        h=[]

        for i in nums:
            heapq.heappush(h,i)
        ans=[]
        while len(h)>0:
            t=heapq.heappop(h)
            ans.append(t)
        return ans

        