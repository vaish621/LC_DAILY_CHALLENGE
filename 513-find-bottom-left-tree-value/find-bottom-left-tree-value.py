# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        q=deque()

        q.append([root,0])
        prev=-1
        ans=0

        while q:
            le=len(q)

            for i in range(le):
                n,l=q.popleft()
                if prev!=l:
                    ans=n.val
                    prev=l

                if n.left:
                    q.append([n.left,l+1])
                if n.right:
                    q.append([n.right,l+1])
        
        return ans
            

        