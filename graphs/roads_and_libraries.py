#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
    # if the cost of a lib is less than the cost of a road
    # we build a lib in every city and don't worry about roads
    if c_lib<=c_road:
        return n * c_lib

    cities_as_adjacency_list = {city : [] for city in range(1,n+1)}
    for city_pair in cities:
        cities_as_adjacency_list[city_pair[0]].append(city_pair[1])
        cities_as_adjacency_list[city_pair[1]].append(city_pair[0])

    no_library = {i for i in range(1,n+1)}
    cost = 0
    while(len(no_library)>0):
        city = no_library.pop()
        cost += c_lib
        to_visit_stack = get_needy_neighbors(no_library, cities_as_adjacency_list[city])
        while(len(to_visit_stack)>0):
            cur_city = to_visit_stack.pop()
            if cur_city in no_library:
                cost += c_road
                no_library.remove(cur_city)
                to_visit_stack.extend(
                    get_needy_neighbors(no_library, cities_as_adjacency_list[cur_city]))
    return cost    

def get_needy_neighbors(no_library, neighbors):
        to_visit_stack = []
        for neighbor in neighbors:
            if (neighbor in no_library):
                to_visit_stack.append(neighbor)
        return to_visit_stack

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()

