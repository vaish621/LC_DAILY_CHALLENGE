# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        check=[]

        def inorder(root):
            if root is None:
                return 
            
            inorder(root.left)
            check.append(root.val)
            inorder(root.right)
        
        inorder(root)
        
        def create(l,r):
            if l>r:
                return None
            
            m=(l+r)//2
            ne=TreeNode(check[m])

            ne.left=create(l,m-1)
            ne.right=create(m+1,r)

            return ne
        
        return create(0,len(check)-1)

        