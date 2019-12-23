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
    graph_as_adjacency_list = make_adjacency_list(graph_nodes, graph_from, graph_to)

    # for each color of val, run dfs looking for another color val
    current_best_path_length = graph_nodes + 5
    for index, color in enumerate(ids):
        index += 1
        if val == color:
            new_length = dfs(graph_as_adjacency_list, val, index, ids, current_best_path_length)
            if new_length:
                current_best_path_length = new_length
    if current_best_path_length < graph_nodes + 5:
        return current_best_path_length
    else:
        return -1
                
def get_path_length_from_discovered_by_dict(discovered_by_dict, start_node, end_node):
    cur = end_node
    path_length = 0
    while cur != start_node and path_length < len(discovered_by_dict):
        path_length += 1
        cur = discovered_by_dict[cur]
    return path_length

def dfs(graph_as_adjacency_list, searching_for_val, start_index, ids, current_best_path_length):
    to_search_stack = graph_as_adjacency_list[start_index]
    discovered_by_dict = {i : start_index for i in graph_as_adjacency_list[start_index]}
    searched = [start_index]
    while(len(to_search_stack)>0):
        cur = to_search_stack.pop()
        if ids[cur-1] == searching_for_val:
            distance = get_path_length_from_discovered_by_dict(discovered_by_dict, start_index, cur)
            if distance < current_best_path_length:
                current_best_path_length = distance
                return current_best_path_length
        searched.append(cur)
        neighbors = graph_as_adjacency_list[cur]
        for neighbor in neighbors:
            if neighbor not in searched:
                to_search_stack.append(neighbor)
                discovered_by_dict[neighbor] = cur
    return False                    
def make_adjacency_list(graph_nodes, graph_from, graph_to):
    graph_as_adjacency_list = {node : [] for node in range(1, graph_nodes+1)}
    for g_from, g_to in zip(graph_from, graph_to):
        graph_as_adjacency_list[g_from].append(g_to)
        graph_as_adjacency_list[g_to].append(g_from)
    return graph_as_adjacency_list
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
