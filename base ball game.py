class Solution:
    def calPoints(self, ops: List[str]) -> int:
        # ops.reverse()
        print(ops)
        a=0
        b=0
        c=0
        record=[]
        for i in range(len(ops)):
            
            if ops[i]=='D':
                a=int(record.pop())
                b=2*a
                record.append(a)
                record.append(b)
                              
            elif ops[i]=='C':
                record.pop()  
                
            elif ops[i]=='+':
                a=int(record.pop())
                b=int(record.pop())
                c=a+b
                
                record.append(b)
                record.append(a)
                record.append(c)
                
            else:
                record.append(int(ops[i]))
                
        return sum(record)
 

