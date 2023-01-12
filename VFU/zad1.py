#Apply slicing to the following string '0123456789' to extract the substring '456789'.
# sub_string = s[4:]
# print(sub_string)
string = "0123456789"
sub_string = string[4:8]
print(sub_string)
#
# sub_string = s[::3]
# print(sub_string)
#
# sub_string = s[:3]
# print(sub_string)
#
# lst=[3,4,6,1,2]
# lst[1:2]=[7,8]
# print(lst)

# d = {"john":40, "peter":45}
#
# del d["john"]
#
# print(d)

d = {"john":40, "peter":45}
print(list(d.keys()))
# d = {"john":40, "peter":45}
# print(d["john"])
# a=[[]]*3
# a[1].append(7)
# print(a)
t = (1, 2, 4, 3, 8, 9)
print([t[i] for i in range(0, len(t), 2)])

lst=[3,4,6,1,2]
lst[1:2]=[7,8]
print(lst)
