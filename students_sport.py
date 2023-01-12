arr = []
arr_s = []
arr_n = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    arr.append([name, score])
    arr_n.append(score)
arr_n = list(dict.fromkeys(arr_n))
arr_n.sort()
score = arr_n[1]
for ars in arr:
    if ars[1] == score:
        arr_s.append(ars[0])

arr_s.sort()
for s in arr_s:
    print(s)

