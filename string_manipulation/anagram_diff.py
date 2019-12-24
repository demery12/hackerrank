#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    a_dict = get_dict_of_char_counts(a) # {a:5, b:3}
    b_dict = get_dict_of_char_counts(b)
    count = 0
    for char in a_dict:
        count_a = a_dict[char]
        if char in b_dict and count_a > b_dict[char]:
            count += count_a - b_dict[char]
        elif char not in b_dict:
            count += count_a
    for char in b_dict:
        count_b = b_dict[char]
        if char in a_dict and count_b > a_dict[char]:
            count += b_dict[char] - a_dict[char]
        elif char not in a_dict:
            count += count_b
    return count

def get_dict_of_char_counts(string):
    char_dict = {}
    for char in string:
        if char not in char_dict:
            char_dict[char] = 0
        char_dict[char] += 1
    return char_dict

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()

