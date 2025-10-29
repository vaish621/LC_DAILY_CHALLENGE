class Solution:
    def smallestNumber(self, n: int) -> int:

        

        p=0
        check=pow(2,p)

        while check<=n:
            p+=1
            check=pow(2,p)
        
        
        ans=pow(2,p)-1
        return ans
        