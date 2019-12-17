def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    # Make an adjacency list
    graph_as_adjacency_list = {node : [] for node in range(1, graph_nodes+1)}
    for g_from, g_to in zip(graph_from, graph_to):
        graph_as_adjacency_list[g_from].append(g_to)
        graph_as_adjacency_list[g_to].append(g_from)

    # for each color of val, run dfs looking for another color val
    solution_nodes = None
    path_length = graph_nodes + 5
    for index, color in enumerate(ids):
        if val == color and index+1 not in solution:
            #dfs(index+1)
            

    # take the min, or return 0

def dfs(val):
    pass

