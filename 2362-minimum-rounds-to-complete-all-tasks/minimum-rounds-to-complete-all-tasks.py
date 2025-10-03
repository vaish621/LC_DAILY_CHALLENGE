class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:

        c=collections.Counter(tasks)

        s=dict(sorted(c.items(),key=lambda x:x[1],reverse=True))
        tot=0

        for i in s.values():
            if i==1:
                return -1
            tot+=i//3

            if i%3!=0:
                tot+=1
        
        return tot
            
        