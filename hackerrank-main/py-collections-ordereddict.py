n = int(input())
dictionary = {}
for _ in range(n):
    l = input().split()

    key = [" ".join(l[:-1])]
    val = l[-1]
    if key in dictionary:
        dictionary[key] += dictionary[key]
    else:
        dictionary[key] = val

    print(dictionary)