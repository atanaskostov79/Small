# def asdf(i,j):
#     if(i==0):
#         return j
#     else:
#         return asdf(i-1,i+j)
#
#
# print(asdf(5,2))
#
# asdf(5,4)
# asdf(4,7)
# asdf(5,3)
# asdf(5,2)
#
#
# def f(x):
#     def f1(a, b):
#         print("hello")
#         if b==0:
#             print("NO")
#             return
#         return f(a, b)
#     return f1
#
# @f
# def f(a, b):
#      return a%b
#
# f(4,0)
#
#
# def a(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return a(n - 1) + a(n - 2)
#

# for i in range(0, 4):
#     print(a(i), end=" ")
#
#
def odds(start=1):
    ''' return all odd numbers from start upwards'''
    if int(start) % 2 == 0: start = int(start) + 1
    while True:
        yield start
        start += 2

for n in odds(2):
    if n > 10:
        break
    else:
        print(n)
        file = open("odds.txt", "a")
        n = file.write(str(n) + "\r\n")
        file.close()


def mk(x):
    def mk1():
        print("Decorated")
        x()
    return mk1


def mk2():
    print("Ordinary")


p = mk(mk2)
p()


# class objects:
#     def __init__(self):
#         self.colour = None
#         self._shape = "Circle"
#
#
#     def display(self, s):
#         self._shape = s
#
#
# obj = objects()
# print(obj._objects_shape)

def f(p, q):
    return p % q


f(0, 2)
# f(2, 0)