class Solution:
    def smallestString(self, s: str) -> str:

        res=""

        i=0

        while i<len(s) and s[i]=="a":
            i+=1
        
        if i==len(s):
            return s[0:len(s)-1]+"z"
        else:
            ch=s[i]
            org=i

            res=""

            while i<len(s) and s[i]!="a":
                res+=chr(ord(s[i])-1)
                i+=1
            
            return s[0:org]+res+s[i:]

        