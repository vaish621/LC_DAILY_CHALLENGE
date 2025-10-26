class Solution:
    def removeZeros(self, n: int) -> int:
        res=0
        do=1
        while(n>0):
            t=n%10
            if t!=0:
                res+=do*t
                do*=10
            n//=10
        
        return res

        