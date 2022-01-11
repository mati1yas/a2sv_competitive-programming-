n,m=input().split()

arr=list(map(int,input().split()))
A=set(map(int,input().split()))
B=set(map(int,input().split()))
h=0
for i in arr:
    if i in A:
        h+=1
    elif i in B:
        h-=1
print(h)
