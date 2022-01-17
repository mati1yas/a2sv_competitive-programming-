class Solution:
    def isValid(self, s: str) -> bool:
        
        stack=[]
        dic={')':'(','}':'{',']':'['}
        opening="({["
        closing=")}]"
        output=False
        if len(s)%2!=0:
            output=False
        for i in s:
           
            if len(stack)==0 and i in opening:
                
                stack.append(i)
                continue
            if len(stack)!=0 and i in opening:
                stack.append(i)
                
            if len(stack)==0 and i in closing:
                output=False
                break
            if len(stack)!=0 and i in closing :
                
                if stack.pop()!=dic[i] :
                    output=False
                    break
                else:
                    output=True
        
        if len(stack)!=0:
            output=False
            
                
        return output   
                
                
