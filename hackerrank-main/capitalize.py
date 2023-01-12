import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    arr = s.split(" ")

    for i, a in enumerate(arr):
        if len(a) > 0:
            if 97 <= ord(a[0]) <= 122:
                arr[i] = a.title()
    str = " ".join(arr)
    print(str)
    return str


if __name__ == '__main__':
    fptr = open('test.txt', 'w')

    # s = input()
    s = "chris alan"
    s = "1 w 2 r 3g"
    # s = "132 456 Wq  m e"
    # s = "hello   world  lol"
    # s = "q w e r t y u i o p a s d f g h j  k l z x c v b n m Q W E R T Y U I O P A S D F G H J  K L Z X C V B N M"
    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
