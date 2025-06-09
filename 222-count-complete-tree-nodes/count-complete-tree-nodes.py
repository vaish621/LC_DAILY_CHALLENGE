# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        ans=0

        def rec(root):
            nonlocal ans
            if root is None:
                return None
            
            ans+=1
            rec(root.left)
            rec(root.right)
        
        rec(root)
        return ans