class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:

        expr=[
            [arr1[i]+arr2[i]+i for i in range(len(arr1))],
            [arr1[i]-arr2[i]+i for i in range(len(arr1))],
            [arr1[i]+arr2[i]-i for i in range(len(arr1))],
            [arr1[i]-arr2[i]-i for i in range(len(arr1))]
        ]

        ma=float('-inf')

        for i in expr:
            ma=max(ma,max(i)-min(i))
        return ma
        