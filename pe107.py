from useful_functions import *

# check connectivity using BFS
# if all vertices are reachable from the initial
def is_connected(graph):
    num_vertices = len(graph)
    visited = {}
    for i in range(len(graph)):
        visited[i] = False
    queue = [0]
    while(len(queue) > 0):
        u = queue.pop(0)
        visited[u] = True
        for v in range(num_vertices):
            if(not visited[v] and graph[u][v] < float('inf')):
                queue.append(v)
    return(False not in visited.values())

def get_graph():
    graph = []
    with open(f"files/pe107_network.txt", 'r') as f:
        for line in f.readlines():
            graph.append([float(x) for x in line.replace('-','inf').split(',')])
    return graph


if __name__ == "__main__":
    inf = float('inf')
    graph = get_graph()
    # graph = [[inf, 16, 12, 21, inf, inf, inf],
    #          [16, inf, inf, 17, 20, inf, inf],
    #          [12, inf, inf, 28, inf, 31, inf],
    #          [21, 17, 28, inf, 18, 19, 23],
    #          [inf, 20, inf, 18, inf, inf, 11],
    #          [inf, inf, 31, 19, inf, inf, 27],
    #          [inf, inf, inf, 23, 11, 27, inf]]
    edges = {}
    for i in range(len(graph)-1):
        for j in range(i+1, len(graph)):
            if(graph[i][j]) < inf:
                edges[(i,j)] = graph[i][j]
    # sort
    edges = {k:v for k,v in sorted(edges.items(), key=lambda x: x[1])[::-1]}

    # Kruskal's Algorithm
    saved = 0
    for k in edges.keys():
        i,j = k
        weight = edges[k]
        graph[i][j] = inf
        graph[j][i] = inf
        # remove edge if still connected
        if(is_connected(graph)):
            saved += weight
        # otherwise add it back
        else:
            graph[i][j] = weight
            graph[j][i] = weight
    print(saved)