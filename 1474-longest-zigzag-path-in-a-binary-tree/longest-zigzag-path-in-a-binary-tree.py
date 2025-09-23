# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:


        ans=0

        def dfs(root,cur):
            nonlocal ans
            if root is None:
                return
            
            if cur:
                if cur[-1]!='L':
                    dfs(root.left,cur+'L')
                else:
                    dfs(root.left,'L')
            else:
                dfs(root.left,cur+'L')
            if cur: 
                if cur[-1]!='R':
                    dfs(root.right,cur+'R')
                else:
                    dfs(root.right,'R')
            else:
                dfs(root.right,cur+'R')
            
            if cur:
                ans=max(ans,len(cur))
        
        dfs(root,'')
        return ans

        