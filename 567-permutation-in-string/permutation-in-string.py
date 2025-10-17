class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        st1=[0]*26
        st2=[0]*26

        for i in s1:
            st1[ord(i)-ord('a')]+=1
        
        st=0
        en=0

        while en<len(s2):
            st2[ord(s2[en])-ord('a')]+=1

            if en-st+1==len(s1):
                if st2==st1:
                    return True
                else:
                    st2[ord(s2[st])-ord('a')]-=1
                    st+=1
            
            en+=1
        
        return False
        