import re

pattern = r"^([456][0-9]{3})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})$"
second_pattern = r"([0-9]).?\1{3,}"
second_pattern = r"(\d)\1{3,}"
n = int(input())
for n in range(n):
    s = input()
    mach = re.search(pattern, s)
    # print(mach)
    if mach:
        processed = "".join(mach.group(0).split('-'))
        final = re.search(second_pattern, processed)
        if final:
            print("Invalid")
        else:
            print("Valid")
    else:
        print("Invalid")
