#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    num_counts = {}
    to_return = []
    for query in queries:
        operation = query[0]
        data = query[1]
        if operation == 1:
            # built_list.append(data)
            if data not in num_counts:
                num_counts[data] = 0
            num_counts[data] += 1
        if operation == 2:
            if data in num_counts and num_counts[data] > 0:
                num_counts[data] -= 1
        if operation == 3:
            if data in num_counts.values():
                to_return.append(1)
            else:
                to_return.append(0)
    return to_return



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()

