class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:

        for i in range(k-1):
            colors.append(colors[i])
        
        ans=0
        st=0
        en=1

        while en<len(colors):
            if colors[en]==colors[en-1]:
                st=en
                en+=1
                continue
            en+=1

            if en-st<k:
                continue
            
            ans+=1
            st+=1
        
        return ans