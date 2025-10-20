class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        c=collections.Counter(nums)
        
        pair=len(nums)//2

        for k,v in c.items():
            if v%2==0:
                if pair-(v//2)>=0:
                    pair-=(v//2)
                else:
                    return False
            else:
                return False
        
        return True

        