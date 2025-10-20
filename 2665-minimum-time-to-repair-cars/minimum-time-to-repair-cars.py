class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        ma=max(ranks)
        l=1
        r=ma*cars*cars

        def ispossible(mid):
            count=0
            for i in ranks:
                count+=math.floor(math.sqrt(mid//i))
            return count
        
        ans=0
        while l<=r:
            mid=(l+r)//2

            check=ispossible(mid)
            #print(check,mid)
            if check>=cars:
                ans=mid
                r=mid-1
            else:
                l=mid+1
        
        return ans


        