class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:


        ans=0

        while(target>1):
            if maxDoubles>0 and target%2==0:
                target=target//2
                maxDoubles-=1
            elif maxDoubles>0:
                target-=1
            else:
                ans+=target-1
                break
            ans+=1
        return ans
        