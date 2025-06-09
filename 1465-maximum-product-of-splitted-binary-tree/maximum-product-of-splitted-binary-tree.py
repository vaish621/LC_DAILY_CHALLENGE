# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        def rec(root):
            if root is None:
                return 0
            
            l=rec(root.left)
            r=rec(root.right)

            return root.val+l+r

        ans=rec(root)
        ma=0

        def rec1(root):
            nonlocal ma
            if root is None:
                return 0
            
            l=rec1(root.left)
            r=rec1(root.right)
            sb=root.val+l+r
            t=ans-sb
            #print(t,sb)
            ma=max(ma,t*sb)

            return  sb
        
        
        rec1(root)
        MOD = 10**9 + 7
        return ma%(MOD)



                
        