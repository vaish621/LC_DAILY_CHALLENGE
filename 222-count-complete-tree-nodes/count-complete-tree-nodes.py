# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0
        ans=0

        def dfs(root):
            nonlocal ans
            if root is None:
                return None
            
            le=dfs(root.left)
            re=dfs(root.right)


            # if le:
            #     print(le.val)
            # if re:
            #     print(re.val)

            if le and re:
                ans+=2
            elif le and not re:
                ans+=1
            
            return root


        dfs(root)

        return ans+1 if ans>0 else 1

        


        