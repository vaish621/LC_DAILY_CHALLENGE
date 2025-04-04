# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(root):
            if root is None:
                return (0,None)
            
            le,lel=dfs(root.left)
            re,rel=dfs(root.right)

            if le>re:
                return (le+1,lel)
            elif re>le:
                return (re+1,rel)
            else:
                return (le+1,root)
        
        return dfs(root)[1]
        