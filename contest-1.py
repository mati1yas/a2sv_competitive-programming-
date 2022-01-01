# QUESTION NUMBER ONE111111111111111
  # A
n=4
for i in range(n):

    for k in range(n+1-i):
         print(" ",end="")

    for j in range(i+num):
         print("*",end="")
    print()
    num+=1
  # B
  for i in range(5):
    for j in range(i):
        print("*",end="")

    print()
# QUESTION NUMBER TWO 222222222222222
i=1
k=1
l=1
i=1

for i in range(5):

    for j in range(i+1):
         print("* ",end="")
    for k in range(5-i-1):
         print("  ",end="")
    for l in range(5-i-1):
         print("  ",end="")

    for n in range(i+1):
         print("* ",end="")
# QUESTION NUMBER THREE3333333333333333
def triangle(n):
    for i in range(2):
        for k in range(n):
            print("#"*(n-1)+" " , end=" ")
        print()
triangle(4)
# QUESTION NUMBER FOUR444444444444444
  # A

n=3
print("PYRAMID")
for i in range(n):
    for j in range(n+1-i):
        print(" ",end="")
    for k in range(1,i+1):
        print(k,end="")
    for l in range(i+1,0,-1):
        print(l,end="")
    print()
  # B
n=3
print("DIAMOND")
for i in range(n):
    for j in range(n-1-i):
        print(" ",end="")
    for k in range(1,i+1):
        print(k,end="")
    for l in range(i+1,0,-1):
        print(l,end="")
    print()

for i in range(1,n):
    for j in range(i):
        print(" ",end="")
    for k in range(1,n-i,1):
        print(k,end="")
    for l in range(n-i,0,-1):
        print(l,end="")
    print()
#  C

n=5

for i in range(n+2):
    if i%2==0:
        for j in range(n):
            print("## ",end="")
    else:
        for j in range(n-1):
            print(" ##",end="")
    print()
# QUESTION NUMBER FIVE (WORKING IT )


# QUESTION NUBMER SIX (666666666666
l=[1,9,0,9,0]
z=[]
for i in l:
    if i==0:
        l.remove(i)
        z.append(i)

s=l+z
print(s)
# QUESTION NUMBER SEVEN 777777



  
