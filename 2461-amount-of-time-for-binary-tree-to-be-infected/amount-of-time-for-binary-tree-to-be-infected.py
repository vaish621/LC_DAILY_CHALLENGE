# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:

        graph=defaultdict(list)

        def dfs(root,par):
            if root is None:
                return
            
            if par is not None:
                graph[root.val].append(par.val)
                graph[par.val].append(root.val)
            
            dfs(root.left,root)
            dfs(root.right,root)
        
        q=deque()

        dfs(root,None)

        q.append(start)
        visit=set()

        visit.add(start)
        time=0

        while q:
            #print("e")
            for i in range(len(q)):
                n=q.popleft()
                #print(n)
                for j in graph[n]:
                    if j not in visit:
                        visit.add(j)
                        q.append(j)
            time+=1
        
        return time-1

        