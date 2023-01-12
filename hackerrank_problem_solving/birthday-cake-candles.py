#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    maximum = result =0
    for c in candles:
        if c < maximum:
            continue
        elif c == maximum:
            result +=1
        elif c > maximum:
            result = 1
            maximum = c
    return result
if __name__ == '__main__':
    fptr = open("candle", 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()