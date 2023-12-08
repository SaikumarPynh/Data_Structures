#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(a):
    arr = sorted(a)
    msum = 0
    Msum = 0
    for i in range(len(arr)-1):
        msum += arr[i]
    for i in range(1,len(arr)):
        Msum += arr[i]
    print(msum,Msum)
        
    # Write your code here

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
