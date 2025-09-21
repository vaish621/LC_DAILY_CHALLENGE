# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:

        ans=0
        def dfs(root):
            nonlocal ans
            if root is None:
                return 0,0
            
            lsum,lcount=dfs(root.left)
            rsum,rcount=dfs(root.right)

            tsum=root.val+lsum+rsum
            tcount=1+lcount+rcount

            if root.val==tsum//tcount:
                ans+=1
            
            return tsum,tcount
        
        dfs(root)
        return ans