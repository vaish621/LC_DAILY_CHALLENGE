# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ma=0

        d={}

        it=0

        le=0
        temp=head
        while(temp!=None):
            temp=temp.next
            le+=1

        temp=head
        while(temp!=None):
            if it not in d:
                d[le-it-1]=temp.val
            else:
                ma=max(ma,d[it]+temp.val)
            it+=1
            temp=temp.next
        return (ma)
        