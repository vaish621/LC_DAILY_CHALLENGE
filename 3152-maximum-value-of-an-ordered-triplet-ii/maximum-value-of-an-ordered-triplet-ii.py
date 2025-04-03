class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:

        ma_a=float('-inf')
        ma_ab=float('-inf')
        ma_abc=0

        for i in nums:
            ma_abc=max(ma_abc,ma_ab*i)
            ma_ab=max(ma_ab,ma_a-i)
            ma_a=max(ma_a,i)
        
        return ma_abc

        