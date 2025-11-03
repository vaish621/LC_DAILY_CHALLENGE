from functools import lru_cache
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:

        EPS=1e-6

        
        def rec(nums):
            if len(nums)==1:
                return abs(nums[0]-24)<EPS
            
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    ne=[]

                    for k in range(len(nums)):
                        if k!=i and k!=j:
                            ne.append(nums[k])
                    
                    a,b=nums[i],nums[j]
                    add=[a-b,b-a,a*b,a+b]

                    if abs(a)>EPS:
                        add.append(b/a)
                    if abs(b)>EPS:
                        add.append(a/b)
                    
                    for val in add:
                        if rec(ne+[val]):
                            return True
            
            return False
        

        return rec(cards)
        