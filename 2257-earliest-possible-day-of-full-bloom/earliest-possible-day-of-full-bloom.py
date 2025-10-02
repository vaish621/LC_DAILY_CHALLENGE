class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:

        s=sorted(zip(growTime,plantTime),reverse=True)

        ans=0

        prev=0

        #print(s)

        for u,v in s:
            prev+=v
            bloom=prev+u
            ans=max(ans,bloom)
        
        return ans
        
        