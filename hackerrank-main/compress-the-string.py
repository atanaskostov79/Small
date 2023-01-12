from itertools import *

n = input()

for i,j in groupby(map(int,list(n))):
    print(tuple([len(list(j)), i]) ,end = " ")