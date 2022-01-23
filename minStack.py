def __init__(self):
        self.minStack=[]
        self.minimum=[]
        

    def push(self, val: int) -> None:
        self.minStack.append(val)
        if len(self.minimum)>0 and self.minimum[-1]>=val:
            
            self.minimum.append(val)
        elif len(self.minimum)==0 :
            self.minimum.append(val)
        

    def pop(self) -> None:
        a=self.minStack.pop()
        if a==self.minimum[-1]:
            self.minimum.pop()
        

    def top(self) -> int:
        return self.minStack[-1]
        

    def getMin(self) -> int:
        if len(self.minimum)>0:
            return self.minimum[-1]
        else:
            return 0
        
