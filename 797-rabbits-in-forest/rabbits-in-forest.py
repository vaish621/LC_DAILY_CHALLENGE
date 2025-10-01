class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c=collections.Counter(answers)

        ans=0

        for k,v in c.items():
            
                gsize=(k+1)
                tot=v//gsize
                if v%gsize!=0:
                    tot+=1
                ans+=tot*gsize

        
        return ans
        