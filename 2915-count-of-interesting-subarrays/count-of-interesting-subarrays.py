class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:

        num=[]

        for i in nums:
            if i%modulo==k:
                num.append(1)
            else:
                num.append(0)
        
        su=0
        d=defaultdict(int)
        d[0]=1
        ans=0

        for i in range(len(num)):
            su+=num[i]
            r1=su%modulo
            r2=(r1-k+modulo)%modulo

            ans+=d[r2]
            d[r1]+=1
        
        return ans

        