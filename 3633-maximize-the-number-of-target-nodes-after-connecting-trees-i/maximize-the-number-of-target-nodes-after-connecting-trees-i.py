class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:

        adj1=defaultdict(list)

        for u,v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)
        
        adj2=defaultdict(list)

        for u,v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)
        

        res1=[1]*(len(edges1)+1)
        res2=[1]*(len(edges2)+1)


        def dfs(st,i,par,k1,adj,fl):
            for j in adj[i]:
                if j==par:
                    continue
                if k1>0:
                    if fl==1:
                        res1[st]+=1
                    else:
                        res2[st]+=1
                    dfs(st,j,i,k1-1,adj,fl)

        

        for i in range(len(res2)):
            dfs(i,i,-1,k-1,adj2,2)

        count=max(res2)
        for i in range(len(res1)):
            (dfs(i,i,-1,k,adj1,1))
        
        if k==0:
            return res1
            
        for i in range(len(res1)):
            res1[i]+=count
        
        return res1
        

        