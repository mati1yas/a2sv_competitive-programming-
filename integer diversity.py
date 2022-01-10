from collections import Counter 
def negate():
    
    n=int(input())
     
    for i in range(n):
        size=int(input())
        l=[]
        l=list(map(int,input().split()))
        
        d=dict(Counter(l))
        
        c=0
        for i in d.keys():
           if d[i]>=2 and i!=0:
               c+=1
        sl=list(set(l))
        if len(sl)==1 and sl[0]==0:
            leng=1
        else:
            leng=len(sl)
        
        tot=leng+c
        print(tot)
        l.clear()
negate()
