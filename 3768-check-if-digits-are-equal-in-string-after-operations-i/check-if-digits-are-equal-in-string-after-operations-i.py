class Solution:
    def hasSameDigits(self, s: str) -> bool:

        while len(s)>2:
            ne=""
            for i in range(len(s)-1):
                cal=(int(s[i])+int(s[i+1]))%10
                ne+=str(cal)
            s=ne
        
        if s[0]==s[1]:
            return True
        return False
        