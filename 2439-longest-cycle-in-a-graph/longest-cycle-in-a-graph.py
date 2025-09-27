class Solution:
    def longestCycle(self, edges: List[int]) -> int:

        visit=set()

        recursion=set()

        count=[1]*len(edges)

        ans=-1

        def dfs(i):
            #print(i,count)
            nonlocal ans
            if i in visit or i==-1:
                return
            
            visit.add(i)
            recursion.add(i)
            v=edges[i]

            if v!=-1 and v not in visit:
                count[v]=count[i]+1
                dfs(v)
            else:
                if v in visit and v in recursion:
                    ans=max(ans,count[i]-count[v]+1)
            
            recursion.remove(i)
        
        res=-1
        for i in range(len(edges)):
            dfs(i)
            res=max(res,ans)
        
        return res