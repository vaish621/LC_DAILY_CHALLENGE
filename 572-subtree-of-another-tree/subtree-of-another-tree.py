# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def check(n1,n2):
            #print(n1,n2)
            if n1 is None and n2 is None:
                return True

            if n1 is None or n2 is  None:
                return False
            
            #print(n1.val,n2.val)
            
            if n1.val!=n2.val:
                return False
            
            return check(n1.left,n2.left) and check(n1.right,n2.right)
        
        ans=False
        
        def find(root,subRoot):
            nonlocal ans
            if root is None:
                return 
            

            if root.val==subRoot.val:
                print(root.val)
                if check(root,subRoot):
                    
                    ans=True
            
            find(root.left,subRoot)
            find(root.right,subRoot)
        
        find(root,subRoot)
        return ans
