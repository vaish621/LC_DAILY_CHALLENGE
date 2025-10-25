class Solution:
    def totalMoney(self, n: int) -> int:

        weeks=n//7
        days=n%7
        ans=28*weeks+7*weeks*(weeks-1)//2+days*(weeks+1)+days*(days-1)//2
        return ans

