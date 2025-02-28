class Solution:
    def isPalindrome(self, x: int) -> bool:
        o=x
        if x<0:
            return False
        num=0

        while(x!=0):
            t=x%10
            num=num*10+t
            x=x//10
        
        if num==o:
            return True
        else:
            return False
        