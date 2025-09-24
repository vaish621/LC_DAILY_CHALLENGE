class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        
        ans=0

        adj=defaultdict(list)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)


        visit=set()

        def dfs(i,count):

            for j in adj[i]:
                count[1]+=1
                if j not in visit:
                    count[0]+=1
                    visit.add(j)
                    dfs(j,count)
        ans=0
        for i in range(n):
            if i not in visit:
                count=[1,0]
                visit.add(i)
                dfs(i,count)
                v=count[0]
                check=(v*(v-1))//2
                if check==count[1]//2:
                    ans+=1

                
        
        return ans