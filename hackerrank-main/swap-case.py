def swap_case(s):
    s = list(s)  # Convert to list because string is immutable
    for i in range(len(s)):
        if 65 <= ord(s[i]) <= 90:
            s[i] = chr(ord(s[i]) + 32)
        elif 97 <= ord(s[i]) <= 122:
            s[i] = chr(ord(s[i]) - 32)
    return "".join(s)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
