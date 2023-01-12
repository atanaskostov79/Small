s = {1, 2, 3}

d = {1, 2, 3}
c = {3, 2, 1}
e =  {2, 1, 3}
print(s==c==d==e)

t = (1, 2, 4, 3)
print(t[1: 3])

print('The sum of {0:b} and {1:x} is {2:o}'.format(2, 10, 12))

def isPalindrome(s):
    if len(s) <= 1:  # Base case
        return True
    elif   s[0] != s[-1]:
        return False
    else:

        return isPalindrome(s[1:len(s) - 1])

print(isPalindrome("malayalam"))
s = {1, 2, 4, 3}
# s[3] = 45
print(s)
print(max(s))
print(len(s))
# print(s[3])

with open("example.txt", "w") as example:
    print("Hello", "World", end=".", sep="-", file=example)

f = open("example.txt", "r")

s = f.read()

s = s.replace("-",", " )
s = s.replace(".","!" )

print(s)

print('The sum of {0:b} and {1:x} is {2:o}'.format(2, 10, 12))
print('{:#}'.format(1112223334))