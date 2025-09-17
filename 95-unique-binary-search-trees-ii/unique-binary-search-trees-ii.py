# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:



        def dfs(left,right):
            if left>right:
                return [None]
            
            res=[]

            for val in range(left,right+1):
                for leftree in dfs(left,val-1):
                    for rightree in dfs(val+1,right):
                        ne=TreeNode(val,leftree,rightree)
                        res.append(ne)
            
            return res
        
        return dfs(1,n)
        


        