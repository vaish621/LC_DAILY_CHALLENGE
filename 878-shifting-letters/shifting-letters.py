class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:

        en=0
        
        t=[0]*len(s)

        

        for j in shifts:
            t[0]=t[0]+j
            en+=1
            if en<len(t):
                t[en]=t[en]-j
        
        for j in range(1,len(t)):
            t[j]=t[j]+t[j-1]

        
        ans=''
        for k in range(len(t)):
            su=ord(s[k])-ord('a')
            f=(su+t[k])%26
            ans+=chr(ord('a')+f)
            #print(ans)
        
        return ans
            
        
        
