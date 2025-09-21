# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        


        def dfs(root):
            if root is None:
                return ""
            
            l=dfs(root.left)
            r=dfs(root.right)

            if root.left is None and root.right is None:
                return str(root.val)
            elif root.left is None:
                return str(root.val)+"()"+"("+r+")"
            elif root.right is None:
                return str(root.val)+"("+l+")"
            else:
                return str(root.val)+"("+l+")"+"("+r+")"
        
        return dfs(root)