class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        mod=10**9+7
        array=[]

        b=bin(n)[2:]
        b=b[::-1]
        st=0

        for i in b:
            if i=="1":
                p=pow(2,st)%mod
                array.append(p)
            st+=1
        
        
        
        
        prefix=[1]*len(array)
        prefix[0]=array[0]

        for i in range(1,len(array)):
            prefix[i]=(prefix[i-1]*array[i])%mod

        # print(array)
        # print(prefix)

        ans=[]

        for st,en in queries:
            
            fi=prefix[en]%mod
            if st-1>=0:
                fi=prefix[en]*(pow(prefix[st-1],mod-2,mod))%mod
            ans.append(fi)
        
        return ans
        