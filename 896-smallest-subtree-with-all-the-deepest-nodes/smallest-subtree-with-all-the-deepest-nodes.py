# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:


        def dfs(root):
            if root is None:
                return None,0
            
            lnode,lh=dfs(root.left)
            rnode,rh=dfs(root.right)

            if lh==rh:
                return root,lh+1
            elif lh>rh:
                return lnode,lh+1
            else:
                return rnode,rh+1
        
        return dfs(root)[0]

        