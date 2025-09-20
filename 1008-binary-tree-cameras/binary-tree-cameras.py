# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        ans=0
        def dfs(root):
            nonlocal ans
            if root is None:
                return 2
            
            l=dfs(root.left)
            r=dfs(root.right)

            if l==0 or r==0:
                ans+=1
                return 1
            
            elif l==1 or r==1:
                return 2
            else:
                return 0
        
        if dfs(root)==0:
            ans+=1
        return ans