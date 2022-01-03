#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    temp=arr[n-1]
    for i in range(2,n+2):    
        
        if temp < arr[n-i]:
            arr[n-i+1]=arr[n-i]
            print(*arr)
        else:
            arr[n-i+1]=temp
            print(*arr)
            break
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
