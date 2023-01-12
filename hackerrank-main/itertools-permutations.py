from itertools import permutations

if __name__ == '__main__':

    n = input().split()

    l = list(permutations(n[0], int(n[1])))
    l.sort()
    for i in l:
        for t in i:
            print(t, end="")
        print()