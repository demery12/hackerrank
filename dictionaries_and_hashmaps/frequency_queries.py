#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    count_of_num = {}
    count_of_frequency = {1:0}
    to_return = []
    for query in queries:
        operation = query[0]
        data = query[1]
        if operation == 1:
            if data not in count_of_num or count_of_num[data]==0:
                count_of_num[data] = 1
                count_of_frequency[1] += 1
            else:
                count_of_frequency[count_of_num[data]] -= 1
                count_of_num[data] += 1
                if count_of_num[data] not in count_of_frequency:
                    count_of_frequency[count_of_num[data]] = 0
                count_of_frequency[count_of_num[data]] += 1
                
        if operation == 2:
            if data in count_of_num and count_of_num[data] > 0:
                count_of_frequency[count_of_num[data]] -= 1
                count_of_num[data] -= 1
                if count_of_num[data] > 0:
                    count_of_frequency[count_of_num[data]] += 1
        if operation == 3:
            if data in count_of_frequency and count_of_frequency[data]>0:
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
