from itertools import combinations_with_replacement

if __name__ == '__main__':
    n = input().split()

    for j in combinations_with_replacement(sorted(n[0]), int(n[1])):
        print("".join(j))
