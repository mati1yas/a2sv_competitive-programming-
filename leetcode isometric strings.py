from collections import Counter 
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ds=dict (Counter(s))
        dt=dict(Counter(t))
        
        sl=[ int(ds[x]) for x in ds.keys()]
        tl=[ int(dt[x]) for x in dt.keys()]   
        
        n=max(len(sl),len(tl)) 
        d=dict(zip(s,t))
       
        if len(sl)!=len(tl):
            r=False        
        else:
            for i in range(n):
                
                if sl[i]!=tl[i]:
                    r= False
                    break 
                elif i == n-1 :
                    for j in range(len(s)):
                        if d[s[j]]!=t[j] :
                            return False
                            break
                            
                        elif j==len(s)-1:
                            return True 
                            
                    
            
        return r
        
