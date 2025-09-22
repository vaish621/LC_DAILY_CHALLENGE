# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        q=deque()

        q.append(root)

        adj={}

        le=0

        while q:
            c=0

            for i in range(len(q)):
                t=q.popleft()
                c+=t.val
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
            
            adj[le]=c
            le+=1
        
        root.val=0

        q=deque()

        q.append(root)

        le=1

        while q:
            for i in range(len(q)):
                t=q.popleft()
                sib=0
                if t.left:
                    q.append(t.left)
                    sib+=t.left.val
                if t.right:
                    q.append(t.right)
                    sib+=t.right.val
                if t.left:
                    t.left.val=adj[le]-sib
                if t.right:
                    t.right.val=adj[le]-sib
            le+=1
        
        return root

        