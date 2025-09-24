class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:


        count={}

        visit=set()
        visit.add(0)
        ans=[0]*len(labels)

        adj=defaultdict(list)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(i):
            d=defaultdict(int)

            d[labels[i]]=1
            
            for j in adj[i]:
                if j not in visit:
                    visit.add(j)
                    child=dfs(j)
                    for k,v in child.items():
                        d[k]+=v

            #print(i,d)
            ans[i]=d[labels[i]]
            return d
        
        dfs(0)
        return ans


        