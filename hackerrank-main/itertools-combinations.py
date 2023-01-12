from itertools import combinations

if __name__ == '__main__':
    n = input().split()

for i in range(1, int(n[1]) + 1):
    for j in combinations(sorted(n[0]), i):
        print("".join(j))
