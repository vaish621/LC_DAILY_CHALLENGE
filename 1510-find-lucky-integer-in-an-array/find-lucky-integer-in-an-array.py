class Solution:
    def findLucky(self, arr: List[int]) -> int:

        ck=collections.Counter(arr)

        ma=-1

        for j in ck:
            if j==ck[j]:
                ma=max(ma,j)
        
        #print(ma)

        return ma
        