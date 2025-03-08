class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        i=0
        ans=0

        while i<len(blocks):
            if blocks[i]=='W':
                while(i<len(blocks) and blocks[i]=='W'):
                    i+=1
            else:
                c=0
                while(i<len(blocks) and blocks[i]=='B'):
                    c+=1
                    i+=1
                ans=max(ans,c)
        
        if ans>=k:
            return 0
        
        st=0
        en=0

        w=0
        b=0
        ans=float('inf')
        while en<len(blocks):
            if blocks[en]=='W':
                w+=1
            
            if blocks[en]=='B':
                b+=1
            
            if w+b==k:
                ans=min(ans,w)
                if blocks[st]=='W':
                    w-=1
                else:
                    b-=1
                st+=1
            en+=1
        
        return (ans)



        