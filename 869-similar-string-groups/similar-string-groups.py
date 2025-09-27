class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:

        adj=defaultdict(list)

        for i in range(len(strs)):
            for j in range(i+1,len(strs)):
                ch=(strs[i])
                ch1=(strs[j])
                k=0
                k1=0

                co=0

                while k<len(ch) and k1<len(ch1):
                    if ch[k]!=ch1[k]:
                        co+=1
                    k+=1
                    k1+=1
                
                if co<=2:
                    adj[i].append(j)
                    adj[j].append(i)
        

        visit=set()

        def dfs(i,par):
            if i in visit:
                return
            visit.add(i)

            for j in adj[i]:
                if j==par:
                    continue
                dfs(j,i)

        
        ans=0
        for i in range(len(strs)):
            if i not in visit:
                dfs(i,-1)
                ans+=1
                
        
        return ans

        