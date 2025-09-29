"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        adj=defaultdict(list)


        for i in employees:
            if len(i.subordinates)>0:
                for k in i.subordinates:
                    adj[i.id].append(k)
        
        strength={}

        for i in employees:
            strength[i.id]=i.importance
        
        #print(adj)
        
        visit=set()
        ans=0

        def dfs(i):
            nonlocal ans
            visit.add(i)
            ans+=strength[i]

            if i in adj:
                for j in adj[i]:
                    if j not in visit:
                        dfs(j)

        dfs(id)

        return ans

        


        