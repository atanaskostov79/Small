n = int(input())
for _ in range(n):
    number1, number2 = input().split()
    try:
        print( int(int(number1) / int(number2)))
    except ZeroDivisionError as e:
         print ("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print(f"Error Code: {e}")
