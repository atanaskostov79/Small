n = 5
s = "2 3 6 6 5"

x = s.split()
x = list(dict.fromkeys(x))
x.sort()
print(x)
print(x[-2:])

# n = int(input())
# arr = map(int, input().split())
# print(list(arr))