class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:


        prereq={i:[] for i in range(numCourses)}


        for crs,pre in prerequisites:
            prereq[crs].append(pre)
        

        output=[]
        cycle=set()
        

        def dfs(crs):

            if crs in cycle:
                return False
            
            if crs in output:
                return True
            
            cycle.add(crs)

            for j in prereq[crs]:
                if not dfs(j):
                    return False
            
            cycle.remove(crs)
            output.append(crs)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return output
            