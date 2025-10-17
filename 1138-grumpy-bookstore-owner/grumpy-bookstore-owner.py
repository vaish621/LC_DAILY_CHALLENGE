class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        su=0

        for i in range(len(customers)):
            if grumpy[i]==0:
                su+=customers[i]
        

        st=0
        en=0
        ans=0
        zsum=0

        

        while en<len(grumpy):
            if grumpy[en]==1:
                zsum+=customers[en]
            
            if en-st+1==minutes:
                ans=max(ans,zsum+su)
                if grumpy[st]==1:
                    zsum-=customers[st]
                st+=1
            en+=1
        

        return ans


        
        
        