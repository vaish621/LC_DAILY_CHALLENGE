# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:



        def build(ino,post):
            if len(post)<1:
                return None
            
            ne=TreeNode(post[-1])



            index=ino.index(post[-1])
            


            lepost=post[0:index]
            repost=post[index:len(post)-1]

            inleft=ino[0:index]
            inright=ino[index+1:]

            ne.left=build(inleft,lepost)
            ne.right=build(inright,repost)

            return ne
        
        return build(inorder,postorder)
        

        