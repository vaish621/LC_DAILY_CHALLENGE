class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        ma=1

        if arr[0]!=1:
            arr[0]=1

        for i in range(1,len(arr)):
            if arr[i]-arr[i-1]>1:
                
                arr[i]=arr[i-1]+1
                ma=max(ma,arr[i])
            ma=max(ma,arr[i])
        
        
        
        return ma
        