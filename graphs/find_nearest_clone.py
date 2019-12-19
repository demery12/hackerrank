#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#
def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    # Make an adjacency list
    graph_as_adjacency_list = {node : [] for node in range(1, graph_nodes+1)}
    for g_from, g_to in zip(graph_from, graph_to):
        graph_as_adjacency_list[g_from].append(g_to)
        graph_as_adjacency_list[g_to].append(g_from)
    
    print(graph_as_adjacency_list)

    # for each color of val, run dfs looking for another color val
    solution_nodes = []
    path_length = graph_nodes + 5
    for index, color in enumerate(ids):
        print(index, color)
        index += 1
        if val == color and index not in solution_nodes:
            #dfs(index+1)
            to_search_stack = graph_as_adjacency_list[index]
            searched = [index]
            distance = 0
            while(len(to_search_stack)>0):
                cur = to_search_stack.pop()
                distance += 1
                if ids[cur-1] == val:
                    if distance < path_length:
                        solution_nodes = [cur, index]
                        path_length = distance
                    break
                searched.append(cur)
                neighbors = graph_as_adjacency_list[cur]
                for neighbor in neighbors:
                    if neighbor not in searched:
                        to_search_stack.append(neighbor)
    if solution_nodes:
        return path_length
    else:
        return -1
                


            

    # take the min, or return 0

def dfs(val):
    pass

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    fptr.write(str(ans) + '\n')

    fptr.close()
