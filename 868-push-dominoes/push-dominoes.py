class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        d={}
        index=[]
        ans=['.']*len(dominoes)

        for i in range(len(dominoes)):
            if dominoes[i]!='.':
                d[i]=dominoes[i]
                index.append(i)
        
        done=set()
        
        for i in range(len(index)-1):
            if d[index[i]]=='R' and d[index[i+1]]=='L':
                check=index[i+1]-index[i]-1
                ans[index[i]]='R'
                ans[index[i+1]]='L'
                div=check//2
                it=0
                ind=index[i]+1
                while ind<len(dominoes) and it<div:
                    ans[ind]='R'
                    ind+=1
                    it+=1
                it=0
                ind=index[i+1]-1
                while ind>=0 and it<div:
                    ans[ind]='L'
                    ind-=1
                    it+=1
                done.add(index[i])
                done.add(index[i+1])
        
        
        for k,v in d.items():
            if k not in done:
                if v=='R':
                    ans[k]='R'
                    ind=k+1
                    while ind<len(ans) and ans[ind]=='.':
                        ans[ind]='R'
                        ind+=1
                else:
                    ans[k]='L'
                    ind=k-1
                    while ind>=0 and ans[ind]=='.':
                        ans[ind]='L'
                        ind-=1
        
        #print(ans)
        ans="".join(ans)
        return ans
            
            
            