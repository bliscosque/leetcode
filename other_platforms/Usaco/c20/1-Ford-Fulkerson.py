from collections import deque

def bfs(graph, source, sink, parent):
    visited = [False] * (len(graph) + 1)
    queue = deque([(source, float('inf'))])
    visited[source] = True

    while queue:
        node, min_flow = queue.popleft()
        if node == sink:
            return min_flow, parent
        for neighbor, capacity in enumerate(graph[node]):
            if not visited[neighbor] and capacity > 0:
                visited[neighbor] = True
                parent[neighbor] = node
                queue.append((neighbor, min(min_flow, capacity)))
    return 0, parent

def ford_fulkerson(graph, source, sink):
    parent = [-1] * (len(graph) + 1)
    max_flow = 0

    while True:
        flow, parent = bfs(graph, source, sink, parent)
        if flow == 0:
            break
        max_flow += flow

        # Update graph with new flow found
        node = sink
        while node != source:
            prev_node = parent[node]
            graph[prev_node][node] -= flow
            graph[node][prev_node] += flow
            node = prev_node

    return max_flow

graph = [
    [0, 5, 0, 4, 0, 0],
    [0, 0, 6, 0, 0, 0],
    [0, 0, 0, 0, 8, 5],
    [0, 3, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0],
]

source = 0
sink = 5

max_flow = ford_fulkerson(graph, source, sink)
print(f"Fluxo máximo: {max_flow}")