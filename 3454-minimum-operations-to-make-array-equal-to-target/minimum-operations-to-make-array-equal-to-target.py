class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:

        diff=[]

        for i in range(len(target)):
            diff.append(target[i]-nums[i])
        
        ans=0
        prev=0

        for i in range(len(diff)):
            cur=diff[i]
            if (prev<0 and cur>0) or (prev>0 and cur<0):
                ans+=abs(cur)
            elif abs(cur)>abs(prev):
                ans+=abs(cur)-abs(prev)
            
            prev=diff[i]
        
        return ans
        