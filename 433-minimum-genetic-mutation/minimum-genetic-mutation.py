class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:


        q=deque()

        q.append(startGene)

        change=['A','C','G','T']

        time=0
        visit=set()
        visit.add(startGene)

        while q:

            for i in range(len(q)):

                t=q.popleft()
                #print(t)

                if t==endGene:
                    return time
                dp=t
                
                for j in range(len(dp)):
                    for ch in change:
                        if dp[j]!=ch:
                            if j==len(dp)-1:
                                k=dp[0:j]+ch
                            else:
                                k=dp[0:j]+ch+dp[j+1:]
                            
                            if k in bank and k not in visit:
                                visit.add(k)
                                q.append(k)
            time+=1
                        

        return -1

        