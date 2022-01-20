from itertools import permutations

string,num=input().split()
p=list(permutations(sorted(string),int(num)))
for i in p:
    print(''.join(i))
