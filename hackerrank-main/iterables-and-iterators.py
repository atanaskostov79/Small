from itertools import *
n = input()
st = input().split()
k = input()
ind = list()
com = list(combinations(range(1,int(n)+1),int(k)))
for i,g in enumerate(st):
    if g == 'a':
         ind.append(i+1)
count = 0
res = float(len(set([y for x in ind for y in com if x in y ])))/len(com)
print (f"{res:.4f}")
