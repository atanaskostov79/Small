li = list(input().split())
n = int(li[0])
m = int(li[1])

string = ''
for ni in range(1, n + 1):
    if ni % 2 == 0:
        continue
    else:
        string = ".|." * ni
    if len(string) == m:
        string = "WELCOME"
    print(string.center(m, '-'))

for ni in range(n - 1, 0, -1):
    if ni % 2 == 0:
        continue
    else:
        string = ".|." * ni

    print(string.center(m, '-'))
