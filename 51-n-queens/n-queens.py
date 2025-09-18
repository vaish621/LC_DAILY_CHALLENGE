class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        board=[['.']*n for _ in range(n)]

        o=n
        ans=[]

        def issafe(r,c):
            

            for i in range(c):
                if board[r][i]=='Q':
                    return False
            
            for i in range(r):
                if board[i][c]=='Q':
                    return False
            
            i,j=r,c

            while i>=0 and j>=0:
                if board[i][j]=='Q':
                    return False
                i-=1
                j-=1
            
            i,j=r,c

            while i>=0 and j<n:
                if board[i][j]=='Q':
                    return False
                i-=1
                j+=1
            
            return True
        

        def rec(o,r):
            if o==0:
                ans.append(["".join(row) for row in board])
                return
            
            for j in range(n):
                if issafe(r,j):
                    board[r][j]='Q'
                    rec(o-1,r+1)
                    board[r][j]='.'
        
        rec(o,0)
        return ans
            

        

