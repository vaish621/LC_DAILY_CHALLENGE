class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:

        prev=0
        ans=0

        for i in range(len(bank)):
            cur=0
            for j in bank[i]:
                if j=='1':
                    cur+=1
            
            ans+=prev*cur

            if cur!=0:
                prev=cur
        
        return ans

        