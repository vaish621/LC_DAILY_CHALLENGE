from functools import lru_cache
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:


        @lru_cache(None)
        def rec(i,j):
            if i==len(matrix) or j==len(matrix[0]) or matrix[i][j]==0:
                return 0
            
            size=1+min(rec(i+1,j),rec(i,j+1),rec(i+1,j+1))

            return size
        
        res=0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]:
                    res+=rec(i,j)
        
        return res
        