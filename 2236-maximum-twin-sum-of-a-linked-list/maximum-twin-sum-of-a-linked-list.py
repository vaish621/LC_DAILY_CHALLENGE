# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow=head
        fast=head
        

        ans=0

        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        
        prev=None
        while slow:
            node=slow.next
            slow.next=prev
            prev=slow
            slow=node

        while prev:
            ans=max(ans,head.val+prev.val)
            head=head.next
            prev=prev.next


        return (ans)