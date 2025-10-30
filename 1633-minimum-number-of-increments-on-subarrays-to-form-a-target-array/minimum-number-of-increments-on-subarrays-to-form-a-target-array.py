class Solution:
    def minNumberOperations(self, target: List[int]) -> int:

        prev=0
        ans=0
        
        for i in range(len(target)):
            cur=target[i]
            if cur>prev:
                ans+=cur-prev
            prev=target[i]
        
        return ans
        