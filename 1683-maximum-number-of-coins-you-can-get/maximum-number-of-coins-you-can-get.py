class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)

        it=0
        ans=0
        m=0
        print(piles)

        while it<len(piles)//3:
            ans+=piles[m+1]
            it+=1
            m+=2
        
        return ans

        