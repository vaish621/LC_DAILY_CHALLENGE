class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:

        st=0
        en=0
        ans=0
        count=[0,0]

        while en<len(s):
            if s[en]=='1':
                count[1]+=1
            else:
                count[0]+=1
            
            while st<en and (count[0]>k and count[1]>k):
                
                if s[st]=='1':
                    count[1]-=1
                else:
                    count[0]-=1
                st+=1
            ans+=en-st+1
            en+=1
        

        
        
        return ans
        