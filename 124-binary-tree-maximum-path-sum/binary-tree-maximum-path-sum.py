# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def rec(root):
            if root is None:
                return 0

           
            return root.val+rec(root.left)+rec(root.right)
        
        ans=rec(root)
        ma=root.val

        def rec1(root):
            nonlocal ma
            if root is None:
                return 0
            l=max(0,rec1(root.left))
            r=max(0,rec1(root.right))
            ma=max(ma,root.val+l+r)
            return root.val+max(l,r)
        
        # print(ans)
        ma=max(ma,root.val)
        rec1(root)
        return ma