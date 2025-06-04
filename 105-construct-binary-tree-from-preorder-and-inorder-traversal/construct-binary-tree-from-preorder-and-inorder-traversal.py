# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        d={}

        for i in range(len(inorder)):
            d[inorder[i]]=i

        idx=0
        

        def rec(st,en):
            nonlocal idx
            if st>en:
                return None
            
            root=TreeNode(preorder[idx])
            i=d[preorder[idx]]
            idx+=1
            

            root.left=rec(st,i-1)
            root.right=rec(i+1,en)

            return root
        
        return rec(0,len(inorder)-1)
        