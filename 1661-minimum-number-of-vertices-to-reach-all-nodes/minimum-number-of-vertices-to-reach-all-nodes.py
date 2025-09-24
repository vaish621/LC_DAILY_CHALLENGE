class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        nodes=[0]*n

        for u,v in edges:
            nodes[v]+=1
        
        ans=[]
        for i in range(n):
            if nodes[i]==0:
                ans.append(i)
        
        return ans
        