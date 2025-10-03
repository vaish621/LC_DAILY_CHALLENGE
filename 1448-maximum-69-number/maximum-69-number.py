class Solution:
    def maximum69Number (self, num: int) -> int:
        num=str(num)
        for i in range(len(num)):
            if num[i]=="6":
                ans=num[0:i]+"9"+num[i+1:]
                return int(ans)
        
        return int(num)
        