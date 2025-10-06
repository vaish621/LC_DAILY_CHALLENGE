"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        if root is None:
            return []

        ans=[[root.val]]

        q=deque()

        q.append(root)


        while q:
            f=[]
            for i in range(len(q)):
                t=q.popleft()
                if t.children:
                    for j in range(len(t.children)):
                        f.append(t.children[j].val)
                        q.append(t.children[j])
            if f:
                ans.append(f)
        
        return ans

        