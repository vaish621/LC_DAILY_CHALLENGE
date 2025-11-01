class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:

        idx=0
        queries.sort()

        available=[]
        running=[]

        for i in range(len(nums)):
            
            while idx<len(queries) and queries[idx][0]<=i:
                heapq.heappush(available,-queries[idx][1])
                idx+=1
            
            while running and running[0]<i:
                heapq.heappop(running)

            
            while len(running)<nums[i]:
                if not available:
                    return -1
                
                r=-heapq.heappop(available)
                if r<i:
                    return -1
                heapq.heappush(running,r)
            
            
        
        while idx<len(queries):
            heapq.heappush(available,-queries[idx][1])
            idx+=1
        
        return len(available)

        