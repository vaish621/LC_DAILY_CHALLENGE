# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:

        d=deque([root])

        ast=False

        while d:
            n=d.popleft()

            if n==None:
                ast=True
            else:
                if ast:
                    return False
                d.append(n.left)
                d.append(n.right)
        return True
        