# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        q=deque()
        ans=0

        q.append([root,0])

        while q:
            fi=q[0][1]
            la=q[-1][1]
            ans=max(ans,la-fi)

            for i in range(len(q)):
                t,le=q.popleft()

                if t.left:
                    q.append([t.left,2*le])
                if t.right:
                    q.append([t.right,2*le+1])
        
        return ans+1


        