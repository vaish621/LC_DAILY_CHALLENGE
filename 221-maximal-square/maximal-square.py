from functools import lru_cache
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ans=0


        @lru_cache(None)
        def rec(i,j):
            nonlocal ans
            if i==len(matrix) or j==len(matrix[0]) or matrix[i][j]=="0":
                return 0
            
            size=1+min(rec(i+1,j),rec(i,j+1),rec(i+1,j+1))
            ans=max(ans,size)

            return size
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]=="1":
                    rec(i,j)
            
        return ans*ans

        