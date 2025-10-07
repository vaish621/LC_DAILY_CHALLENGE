class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:

        l=1
        r=max(candies)
        ans=0

        while l<=r:
            mid=(l+r)//2
            co=0

            for i in candies:
                if i>=mid:
                    co+=i//mid
            
            #print(mid,co)


            if co>=k:
                ans=mid
                l=mid+1
            else:
                r=mid-1
        
        return ans
        