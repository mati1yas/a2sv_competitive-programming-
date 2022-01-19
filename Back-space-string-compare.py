class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ns=[]
        nt=[]
        for i in s:
            if i=='#':
                if len(ns)==0:
                    continue
                else:
                    ns.pop()
            else:
                ns.append(i)
        
        for i in t:
            if i=='#':
                if len(nt)==0:
                    continue
                else:
                    nt.pop()
            else:
                nt.append(i)
            
        if nt==ns:
            return True
        else:
            return False
                
                
                
