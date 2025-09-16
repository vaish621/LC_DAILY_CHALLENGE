# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if root is None:
            return TreeNode(val)

        def dfs(root,prev):
            if root is None:
                if prev is not None:
                    if val<prev.val:
                        prev.left=TreeNode(val)
                    else:
                        prev.right=TreeNode(val)
                return
            
            if val<root.val:
                dfs(root.left,root)
            else:
                dfs(root.right,root)
        dfs(root,None)

        return root
        