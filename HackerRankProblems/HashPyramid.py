#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    for i in range(1,n+1):
        for j in range(n-i,0,-1):
            print(end=" ")
        print(i * "#")
        
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
