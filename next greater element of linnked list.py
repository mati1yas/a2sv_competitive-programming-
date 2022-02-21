# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        lp=head 
        arr=[]
        while lp:
            arr.append(lp.val)
            lp=lp.next
        res=[0]*len(arr)
        stack=[]
        for index,item in enumerate(arr):
            while stack and item>stack[-1][0]:
                stackt,stackin=stack.pop()
                print(stackt,stackin)
                res[stackin]=(item)
            stack.append([item,index])
        return res
            
            
