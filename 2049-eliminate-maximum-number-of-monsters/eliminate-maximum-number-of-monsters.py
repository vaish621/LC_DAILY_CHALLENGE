class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:

        diff=[]

        for u,v in zip(dist,speed):
            diff.append((u+v-1)//v)
        
        diff.sort()
        
        ans=0
        
        for i,t in enumerate(diff):
            if t<=i:
                return i
        
        return len(diff)