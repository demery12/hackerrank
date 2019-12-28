#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    count_dict = {}
    count_pairs_dict = {}
    number_triplets = 0
    for item in arr[::-1]:
        triple_pair = (item * r, item * r * r)
        if triple_pair in count_pairs_dict:
            number_triplets += count_pairs_dict[triple_pair]
        if item * r in count_dict:
            pair = (item, item * r)
            if pair not in count_pairs_dict:
                count_pairs_dict[pair] = 0
            count_pairs_dict[pair] += count_dict[item * r]
        if item not in count_dict:
            count_dict[item] = 0
        count_dict[item] += 1
    return number_triplets
if True:
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))
    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
