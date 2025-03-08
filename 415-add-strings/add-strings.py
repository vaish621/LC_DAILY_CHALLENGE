class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1=num1[::-1]
        num2=num2[::-1]

        st=''

        if len(num2)<len(num1):
            num1,num2=num2,num1
        
        ca=0
        for i in range(len(num1)):
            t=ca+int(num1[i])+int(num2[i])
            if t>9:
                re=t%10
                q=t//10
                st+=str(re)
                ca=q
            else:
                st+=str(t)
                ca=0
        
        i+=1

        #(ca)
        while i<len(num2):
            t=int(num2[i])+ca
            if t>9:
                re=t%10
                q=t//10
                st+=str(re)
                ca=q
            else:
                st+=str(t)
                ca=0
            i+=1
        
        if ca>0:
            st+=str(ca)
        
        return st[::-1]


        

        