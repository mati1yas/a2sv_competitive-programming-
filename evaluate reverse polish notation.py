import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack=[]
        for i in range(len(tokens)):
            if tokens[i]=='*':
                a=int(stack.pop())
                b=int(stack.pop())
                stack.append(b*a)
            elif tokens[i]=='/':
                a=int(stack.pop())
                b=int(stack.pop())
                if (a<0 or b<0) and b%a==0:
                    stack.append(math.floor(b//a))
                
                elif  (a<0 and b<0) and b%a!=0:
                    stack.append(b//a)
                elif (a<0 or b<0) and b%a!=0:
                    stack.append(1+b//a)
                else:
                    stack.append(b//a)
            elif tokens[i]=='+':
                a=int(stack.pop())
                b=int(stack.pop())
                stack.append(b+a)
            elif tokens[i]=='-':
                a=int(stack.pop())
                b=int(stack.pop())
                stack.append(b-a)
            else:
                stack.append(tokens[i])
            
        return stack[-1]
        
