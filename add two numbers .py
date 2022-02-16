# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        p1,p2=l1,l2
        rem = 0;
        res = n = ListNode(0);
        while p1 or p2 or rem:
            if p1:
                rem += p1.val
                p1 = p1.next;
            if p2:
                rem += p2.val;
                p2 = p2.next;
            rem, val = divmod(rem, 10)
            n.next = n = ListNode(val);
        return res.next;
