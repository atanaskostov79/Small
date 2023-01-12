from itertools import product
import math
print( math.ceil( 31/115 * 100))
x = input().split()
y = input().split()
x = list(map(int, x))
y = list(map(int, y))
out = list(product(x,y))

for i in out:
    print(i, end=" ")