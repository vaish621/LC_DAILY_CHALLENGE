# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        if depth==1:
            n=TreeNode(val)
            n.left= root
            return n
        else:
            cur=1
            def rec(root,cur):
                if root is None:
                    return None
                
                if cur==depth-1:
                    le=root.left
                    re=root.right

                    root.left=TreeNode(val)
                    root.right=TreeNode(val)

                    root.left.left=le
                    root.right.right=re

                    return root
                else:
                    root.left=rec(root.left,cur+1)
                    root.right=rec(root.right,cur+1)
                    return root

            return rec(root,1)
            
        