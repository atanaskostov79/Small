x = 1
y = 1
z = 1
n = 2

li = []

for nx in range(x+1):
    for ny in range(y+1):
        for nz in range(z+1):
            if (nx + ny + nz) != n:
                li.append([nx, ny, nz])

print(li)

