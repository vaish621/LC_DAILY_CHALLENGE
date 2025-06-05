# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def rec(root):

            if root is None:
                return None

            if root==p or root==q:
                return root
            
            l=rec(root.left)
            r=rec(root.right)

            if l!=None and r!=None:
                return root
            elif l==None:
                return r
            else:
                return l
        
        return rec(root)

        