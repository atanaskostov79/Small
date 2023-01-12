def most_commons(s):
    list = []
    print(type(list))
    for i in range(len(s)):
        if not any(s[i] in x for x in list):
            list.append([s[i], 1])
        else:
            for l in range(len(list)):
                if list[l][0] == s[i]:
                    list[l][1] += 1


    list = sorted (list, key=lambda row: (row[1] * -1, row[0]))
    for i in range(3):
        print(f"{list[i][0]} {list[i][1]}")


if __name__ == '__main__':
    # n = input()
    n = "aabbbccde"
    # n = "google"
    # [['g', 2], ['o', 2], ['l', 1], ['e', 1]]
    # [['e', 1], ['l', 1], ['g', 2], ['o', 2]]
    most_commons(n)

    # asdfdsbg