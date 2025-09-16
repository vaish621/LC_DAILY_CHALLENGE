# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        traversal=[]

        while head:
            traversal.append(head.val)
            head=head.next


        def bst(left,right):
            if left > right:
                return None
            
            mid=(left+right)//2
            ne=TreeNode(traversal[mid])

            ne.left=bst(left,mid-1)
            ne.right=bst(mid+1,right)

            return ne
        
        return bst(0,len(traversal)-1)
        