#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
max_arr = {}
def maxSubsetSum(arr):
    max_at_postion  = [arr[0], max(arr[0], arr[1])]
    for i in range(2,len(arr)):
        num = arr[i]
        max_at_postion.append(max(max_at_postion[i-1], max_at_postion[i-2] + num, max_at_postion[i-2], num))
    if max_at_postion[-1]<0:
        return 0
    return max_at_postion[-1]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

