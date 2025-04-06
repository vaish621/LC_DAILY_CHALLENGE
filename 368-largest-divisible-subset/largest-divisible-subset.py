from typing import List
from functools import lru_cache

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        self.le = 0
        self.ans = []

        @lru_cache(None)
        def rec(i, prev_val):
            if i == len(nums):
                return []

            taken = []
            if prev_val == -1 or nums[i] % prev_val == 0:
                taken = [nums[i]] + rec(i + 1, nums[i])
            
            not_taken = rec(i + 1, prev_val)

            return taken if len(taken) > len(not_taken) else not_taken

        self.ans = rec(0, -1)
        return self.ans
