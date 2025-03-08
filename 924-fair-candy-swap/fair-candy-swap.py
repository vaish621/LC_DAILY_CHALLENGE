class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:

        t=(sum(aliceSizes)-sum(bobSizes))//2

        aliceSizes=set(aliceSizes)

        for i in set(bobSizes):
            if t+i in aliceSizes:
                return [t+i,i]
        