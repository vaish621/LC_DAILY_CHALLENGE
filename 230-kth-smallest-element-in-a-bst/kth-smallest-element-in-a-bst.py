# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        h=[]

        def dfs(root):
            #nonlocal h
            if root is None:
                return
            
            heapq.heappush(h,root.val)
            l=dfs(root.left)
            r=dfs(root.right)
        
        dfs(root)
        ans=-1
        while h and k>0:
            ans=heapq.heappop(h)
            k-=1
        return ans


        