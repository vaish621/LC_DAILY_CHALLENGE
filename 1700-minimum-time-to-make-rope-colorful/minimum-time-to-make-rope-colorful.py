class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        time=0

        i=0
        while i<len(colors):
            su=neededTime[i]
            ma=neededTime[i]
            ch=colors[i]
            j=i+1
            while j<len(colors) and ch==colors[j]:
                ma=max(ma,neededTime[j])
                su+=neededTime[j]
                j+=1
            i=j
            time+=su-ma
        
        return time
            
