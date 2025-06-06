# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        
        res=[]
        def rec(root):
            nonlocal res
            if root is None:
                return None
            
            root.left=rec(root.left)
            root.right=rec(root.right)

            if root.val in to_delete:
                if root.left:
                    res.append(root.left)
                if root.right:
                    res.append(root.right)
                
                return None
            else:
                return root

            

            
        
        rec(root)

        if root.val not in to_delete:
            res.append(root)


        return (res)
        