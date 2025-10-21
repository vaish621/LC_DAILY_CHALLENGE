class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:

        c=collections.Counter(tops)
        topmax=0
        topval=0

        for k,v in c.items():
            if v>topmax:
                topmax=v
                topval=k
        
        botmax=0
        botval=0

        b=collections.Counter(bottoms)
        for k,v in b.items():
            if v>botmax:
                botmax=v
                botval=k

        sw=0
        
        for i in range(len(tops)):
            if tops[i]!=topval:
                if bottoms[i]==topval:
                    sw+=1
                else:
                    
                    break
        
        ans=float("inf")
        #print(i)

        if i==len(tops)-1:
            ans=min(sw,ans)
        
        sw=0

        for i in range(len(bottoms)):
            if bottoms[i]!=botval:
                if tops[i]==botval:
                    sw+=1
                else:
                    break
        
        #print(i)
        if i==len(bottoms)-1:
            ans=min(ans,sw)
        
        return ans if ans!=float("inf") else -1


        


        