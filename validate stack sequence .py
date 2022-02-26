class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        p2=0
        
        for i in pushed :           
            stack.append(i)
            
            while len(stack) != 0  and popped[p2] == stack[-1]:
                    stack.pop()
                    p2+=1
        return p2 == len(pushed)
        
