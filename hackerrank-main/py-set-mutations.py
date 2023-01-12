n = int(input())
s = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    command = input().split()

    if command[0] == "intersection_update":
        tc = set(map(int, input().split()))
        s.intersection_update(tc)
        print(s)
    elif command[0] == "update":
        tc = set(map(int, input().split()))
        s.update(tc)
        print(s)
    elif command[0] == "symmetric_difference_update":
        tc = set(map(int, input().split()))
        s.symmetric_difference_update(tc)
        print(s)
    elif command[0] == "difference_update":
        tc = set(map(int, input().split()))
        s.difference_update(tc)
        print(s)
    else:
        assert False
print(sum(s))
