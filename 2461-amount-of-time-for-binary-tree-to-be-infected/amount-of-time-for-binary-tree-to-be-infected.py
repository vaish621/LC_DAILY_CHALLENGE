# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:

        if root is None:
            return 0

        graph=defaultdict(list)

        def dfs(root,par):
            if root is None:
                return
            
            if par:
                graph[par.val].append(root.val)
                graph[root.val].append(par.val)
            
            dfs(root.left,root)
            dfs(root.right,root)
        

        dfs(root,None)

        q=deque()

        q.append(start)
        visit=set()

        visit.add(start)
        time=0

        while q:
            for i in range(len(q)):
                t=q.popleft()
                for j in graph[t]:
                    if j not in visit:
                        visit.add(j)
                        q.append(j)
            time+=1
        
        return time-1

        