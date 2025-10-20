class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        adj=defaultdict(list)

        for u,v in prerequisites:
            adj[u].append(v)
            
        

        def dfs(i,par,des,visit):
            if i==des:
                return True
            
            if adj[i]==[]:
                return False
            
            visit.add(i)
            for j in adj[i]:
                if j==par:
                    continue
                if j not in visit:
                    if dfs(j,i,des,visit):
                        return True
            
            return False
        
        ans=[]
        for u,v in queries:
            visit=set()
            ans.append(dfs(u,-1,v,visit))
        return ans
                


        