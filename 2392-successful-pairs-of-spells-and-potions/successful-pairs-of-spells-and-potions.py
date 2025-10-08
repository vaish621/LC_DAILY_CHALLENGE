import bisect
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        ans=[]
        potions.sort()

        for s in spells:
            div=success//s
            if success%s!=0:
                div+=1
            t=bisect.bisect_left(potions,div)
            if t<len(potions):
                ans.append(len(potions)-t)
            else:
                ans.append(0)
        
        return ans
            
        