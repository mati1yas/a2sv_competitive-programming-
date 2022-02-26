class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        s=''
        
        c = 0
       
        
        for i in num:           
            if  len(stack)==0 :                
                stack.append(i)
                               
            elif i >=stack[-1] :                
                stack.append(i)
                               
            else:
                while stack and stack[-1] > i and c < k :
                    stack.pop()
                    c += 1
                
                stack.append(i)   
        
        s = "".join(stack[0:len(num)-k]).lstrip("0")
        
        
        return "0" if  s== "" else s
