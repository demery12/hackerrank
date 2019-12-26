#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    count_dict = count_chars(s)
    count_of_counts = count_chars(count_dict.values())
    count_of_counts_list = list(count_of_counts.values())
    counts_list = list(count_of_counts.keys())
    bleh = [(k,count_of_counts[k]) for k in count_of_counts]
    if len(count_of_counts_list) == 1 or (
            len(count_of_counts_list)==2 and 1 in count_of_counts_list and (abs(counts_list[0]-counts_list[1]) == 1 or (1,1) in bleh)):
        return 'YES'
    return 'NO'

def count_chars(s):
    count_dict = {}
    for char in s:
        if char not in count_dict:
            count_dict[char] = 0
        count_dict[char] += 1
    return count_dict

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

