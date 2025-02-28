class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:

        su=0
        mi=0
        ma=0

        for i in differences:
            su+=i
            mi=min(mi,su)
            ma=max(ma,su)
        
        l=lower-mi
        u=upper-ma

        return max(0,u-l+1)
        