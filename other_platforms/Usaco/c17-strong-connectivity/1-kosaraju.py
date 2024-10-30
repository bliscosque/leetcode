from collections import defaultdict

def dfs(graph, node, visited, stack):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, stack)
    stack.append(node)

def reverse_graph(graph):
    reversed_graph = defaultdict(list)
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            reversed_graph[neighbor].append(node)
    return reversed_graph

def kosaraju(graph):
    visited = set()
    stack = []
    for node in graph:
        if node not in visited:
            dfs(graph, node, visited, stack)

    reversed_graph = reverse_graph(graph)
    visited = set()
    sccs = []

    while stack:
        node = stack.pop()
        if node not in visited:
            scc = []
            dfs(reversed_graph, node, visited, scc)
            sccs.append(scc)

    return sccs

# Exemplo de uso
graph = {
    1: [2],
    2: [1, 5],
    3: [2, 7],
    4: [],
    5: [4],
    6: [3, 5],
    7: [6]
}

print(kosaraju(graph))