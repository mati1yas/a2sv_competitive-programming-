# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c=0
        
        d=0
        curr=head
        while(head):
            c+=1
            head=head.next
        mid=c//2
        
        head=curr
        while(d<mid):
        
            head=head.next
            d+=1
            
        return head
