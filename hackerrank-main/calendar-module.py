import calendar


m = list(map(int, input().split()))


print(calendar.day_name[calendar.weekday(m[2], m[0], m[1])].upper())

