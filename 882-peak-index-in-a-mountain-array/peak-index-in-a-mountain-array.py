class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        i=0

        while i<len(arr):

            while i+1<len(arr) and arr[i]<arr[i+1]:
                i+=1
            
            return i

            while i+1<len(arr) and arr[i]>arr[i+1]:
                i+=1
            
            return i
        
        
































        