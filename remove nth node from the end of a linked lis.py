# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        h = 0
        p1=head     
        p2= p1
        
        while p1:
            
            p1=p1.next
            h+=1
        
        x=h-n
        
        
        p1=head
        while x>1:           
            p1=p1.next           
            x-=1 
#         if ordered to delete the first from front
        if h==n:
            p1=p1.next
            return p1
#            if only one element            
        if p1.next==None:
            head=None
            return head
        p1.next= p1.next.next
        
        return p2
            
