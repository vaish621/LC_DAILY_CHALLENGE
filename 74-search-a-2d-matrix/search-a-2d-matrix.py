import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for j in matrix:
            t=bisect.bisect_left(j,target)
            if t-1>=0 and j[t-1]==target:
                return True
            elif t>=0 and t<len(j) and j[t]==target:
                return True
            elif t+1<len(j) and j[t+1]==target:
                return True
        
        return False

        