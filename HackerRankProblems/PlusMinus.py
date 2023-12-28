#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    zero,pos,neg = 0,0,0
    for i in arr:
        if i == 0:
            zero += 1
        elif i < 0:
            neg +=1
        else:
            pos += 1
    p = f"{(pos / len(arr)):.6f}"
    n = f"{(neg / len(arr)):.6f}"
    z = f"{(zero / len(arr)):.6f}"
    print(p)
    print(n)
    print(z)
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)