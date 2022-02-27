class Solution:
    def compress(self, chars: List[str]) -> int:
        p2=0
        p1=0
        c=0
        arr = []
        
        
        for p1 in range( len(chars)):
            
            if chars[p2] != chars[p1]:
            
                arr.append(str(chars[p2]))
                if c != 1:
                    c=str(c)
                    for cp in range(len(c)):
                        arr.append(c[cp])
                    
                c=0
                p2=p1
            c+=1
            
            
        arr.append(str(chars[p1]))
               
        if c!=1:
            c=str(c)
            for cp in range(len(c)):
                arr.append(c[cp])
                
        for i in range(len(arr)):
            chars.insert(i,arr[i])
           
        return len(arr)
        
        
