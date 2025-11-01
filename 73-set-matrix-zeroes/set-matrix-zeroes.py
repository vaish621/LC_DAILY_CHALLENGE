class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        mod=10**7+9

        def marking(i,j):

            #row
            for k in range(len(matrix[0])):
                if matrix[i][k]!=0:
                    matrix[i][k]=mod
            
            #col

            for k in range(len(matrix)):
                if matrix[k][j]!=0:
                    matrix[k][j]=mod
        

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    marking(i,j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==mod:
                    matrix[i][j]=0
        
        