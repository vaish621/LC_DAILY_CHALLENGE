import heapq
from typing import List

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:

        ma = []  
        mn=[]

        pr = [-1] * len(nums) 
        sr = [-1] * len(nums) 

        n = len(nums)
        third = n // 3
        en = n - third

        su = 0
        for j in range(0, 2 * third):  
            su += nums[j]
            heapq.heappush(ma, -nums[j])

            if len(ma) > third:
                t = -heapq.heappop(ma)
                su -= t

            if len(ma) == third:
                pr[j] = su  

        su = 0
        for j in range(n - 1, third - 1, -1): 
            su += nums[j]
            heapq.heappush(mn, nums[j])

            if len(mn) > third:
                t = heapq.heappop(mn)
                su -= t

            if len(mn) == third:
                sr[j] = su 

        ans = float('inf')

        
        for i in range(third - 1, 2 * third):
            if sr[i + 1] != -1:
                ans = min(ans, pr[i] - sr[i + 1])

        return ans
