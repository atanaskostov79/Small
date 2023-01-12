def count_substring(string, sub_string):
    counter = 0
    c = 0

    for i in range(len(string) - len(sub_string) + 1):
        for j in range(len(sub_string)):
            if string[i + j] == sub_string[j]:
                if c < len(sub_string):
                    c = c + 1
                    if c == len(sub_string):
                        counter += 1
                        c = 0
                        break
                    continue
            else:
                break
    return counter


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)