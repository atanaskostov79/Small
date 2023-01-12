# str1 = "0123456789"
# str2 = str1[4:]
# print(str2)
#
# d = {"john":40, "peter":45}
# print(list(d.keys()))
#
# d = {"john":40, "peter":45}
# print(d["john"])
#
# t=(1,2,4,3)
# print(t[1:3])
#
# t1 = (1, 2, 4, 3)
# t2 = (1, 2, 3, 4)
# print(t1 == t2)


class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 1

    def __eq__(self, other):
        return self.x * self.y == other.x * other.y


obj1 = A(5, 2)
obj2 = A(2, 5)
print(obj1 == obj2)


print("Hello {0!r} and {0!s}".format('foo', 'bin'))

print("Hello {name1} and {name2}".format(name1='foo', name2='bin'))
print('The sum of {0:b} and {1:x} is {2:o}'.format(2, 10, 12))

a = foo(2)
b = foo(3)
print(a < b)
