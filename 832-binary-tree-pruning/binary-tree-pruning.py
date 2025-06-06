# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        res=[]

        def rec(root):
            nonlocal res

            if root is None:
                return None
            
            root.left=rec(root.left)
            root.right=rec(root.right)

            if root.val==0:
                if root.left==None and root.right==None:
                    res.append(root)
                else:
                    return root
            else:
                return root
        
        rec(root)

        if root.val==0 and root.left==None and root.right==None:
            return None
        
        return root
        