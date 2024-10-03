def bellman_ford(graph, src):
    dst={vertex:float('inf') for vertex in graph}
    dst[src]=0

    for _ in range(len(graph) - 1): # run n-1 iter
        for v in graph:
            for nbr, wt in graph[v]:
                if dst[v]+wt<dst[nbr]:
                    dst[nbr]=dst[v]+wt

    

    #check for negative cycle
    for v in graph:
        for nbr, wt in graph[v]:
            if dst[v]+wt<dst[nbr]:
                return -1 #graph contains negative cycle
             
    return dst

graph = {
    'A': [('C', 6), ('D', 6)],
    'B': [('A', 3)],
    'C': [('D', 1)],
    'D': [('B', 1)],
    'E': [('B', 4), ('D', 2)]
}
distances=bellman_ford(graph, 'A')
for v,d in distances.items():
    print(f"Min dst from 'A' to {v}: {d}")