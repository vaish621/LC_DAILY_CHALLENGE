class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        m=0
        if(x>y):
            m=x
        else:
            m=y
        
        l=[]


        i=0
        ans=0

        while(i<len(s)):
            if(len(l)>0 and l[-1]=='a' and m==x and s[i]=='b'):
                ans+=x
                l.pop()
            elif(len(l)>0 and l[-1]=='b' and m==y and s[i]=='a'):
                ans+=y
                l.pop()
            else:
                l.append(s[i])
            i+=1
        
        i=0
        l1=[]

        while(i<len(l)):
            if(len(l1)>0 and l1[-1]=='a' and m!=x and l[i]=='b'):
                ans+=x
                l1.pop()
            elif(len(l1)>0 and l1[-1]=='b' and m!=y and l[i]=='a'):
                ans+=y
                l1.pop()
            else:
                l1.append(l[i])
            i+=1
        
        return ans

       
        

        

        