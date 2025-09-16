# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        i=0
        def dfs(l):
            nonlocal i
            if i>=len(preorder):
                return None
            
            val=preorder[i]
            if val>l:
                return None
            
            ne=TreeNode(preorder[i])
            i+=1
            
            ne.left=dfs(val)
            ne.right=dfs(l)
            return ne
        
        return dfs(float("inf"))

        
        