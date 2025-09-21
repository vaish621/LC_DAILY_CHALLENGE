# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        check={}
        ans=[]

        def dfs(root):
            if root is None:
                return "N"

            s = f"{root.val},{dfs(root.left)},{dfs(root.right)}"

            
            if s not in check:
                check[s]=1
            else:
                check[s]+=1
            
            #print(s)
            if check[s]==2:
                ans.append(root)
           

            
            return s
        
        dfs(root)
        return ans
        