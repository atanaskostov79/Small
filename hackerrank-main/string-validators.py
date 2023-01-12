if __name__ == '__main__':
    s = input()
    b = False
    for i in range(len(s)):
        if s[i].isalnum():
            b = True
            break
        else:
            b = False
    print(b)
    for i in range(len(s)):
        if s[i].isalpha():
            b = True
            break
        else:
            b = False
    print(b)
    for i in range(len(s)):
        if s[i].isdigit():
            b = True
            break
        else:
            b = False
    print(b)
    for i in range(len(s)):
        if s[i].islower():
            b = True
            break
        else:
            b = False
    print(b)
    b = False
    for i in range(len(s)):
        if s[i].isupper():
            b = True
            break
        else:
            b = False
    print(b)

    # print(s.isalnum())
    # print(s.isalpha())
    # print(s.isdigit())
    # print(s.islower())
    # print(s.isupper())