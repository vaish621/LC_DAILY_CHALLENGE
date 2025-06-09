# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        ans=0
        def rec(root,mi,ma):
            nonlocal ans
            if root is None:
                return None
            
            mi=min(mi,root.val)
            ma=max(ma,root.val)

            ans=max(ans,abs(mi-ma))

            rec(root.left,mi,ma)
            rec(root.right,mi,ma)
        
        rec(root,10000007,-10000007)
        return ans
        