class Solution:
    def maxDiff(self, num: int) -> int:

        dp1=""
        while num>0:
            dp1+=str(num%10)
            num=num//10
        
        dp1=dp1[::-1]
        num=dp1
        
        if num.count(num[0])==len(num):

            a=['9']*len(num)
            b=['1']*len(num)

            return int("".join(a))-int("".join(b))
        
        else:
            if num[0]=='1':
                b=[]
                for j in range(len(num)):
                    if num[j]=='1':
                        b.append('9')
                    else:
                        b.append(num[j])
                
                i=0
                while i<len(num) and (num[i]=='1' or num[i]=='0'):
                    i+=1
            
                if i==len(num):
                    return int("".join(b))-int(num)
                
                num=num.replace(num[i],'0')

                return int("".join(b))-int(num)
            else:
                b=[]

                st=0

                if num[0]=='9':
                    st=0
                    while st<len(num) and num[st]=='9':
                        st+=1
                    
                if st<len(num):
                    for i in range(len(num)):
                        if num[i]==num[st]:
                            b.append('9')
                        else:
                            b.append(num[i])
                    
                    num=num.replace(num[0],'1')

                    return int("".join(b))-int(num)
                else:
                    large=int(num)
                    num=num.replace(num[0],'1')
                    return large-int(num)

                