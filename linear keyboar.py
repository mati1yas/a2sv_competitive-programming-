def distance():
    n=int(input())
    for i in range(n):
        s=str(input())
        c=str(input())
        d=dict(zip(s,[*range(1,len(s)+1,1)]))
       
        dist=0
        for i in range(len(c)-1):
            dist+=abs(d[c[i]]-d[c[i+1]])
        print(dist)
distance() 
