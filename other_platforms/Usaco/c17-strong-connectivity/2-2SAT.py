from collections import defaultdict

def to_graph(expression):
    graph = defaultdict(list)
    for clause in expression.split('^'):
        literals = [int(x.strip('~')) for x in clause.strip('()').split('v')]
        if len(literals) != 2:
            raise ValueError("Invalid 2-SAT clause: must have exactly two literals")
        x1, x2 = literals
        if x1 < 0:
            graph[-x1].append(-x2)
        else:
            graph[x1].append(x2)
        if x2 < 0:
            graph[-x2].append(-x1)
        else:
            graph[x2].append(x1)
    return graph

def dfs(graph, node, visited, stack):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, stack)
    stack.append(node)

def kosaraju(graph):
    n = max(max(abs(node) for node in graph), 0)
    visited = set()
    stack = []
    for node in range(1, n+1):
        if node not in visited:
            dfs(graph, node, visited, stack)

    scc = []
    visited = set()
    while stack:
        node = stack.pop()
        if node not in visited:
            component = []
            dfs(graph, node, visited, component)
            scc.append(component)
    return scc

def solve_2sat(expression):
    graph = to_graph(expression)
    scc = kosaraju(graph)
    for component in scc:
        if any(abs(x) in component for x in component):
            return False
    return True

expression = "(x2 v ~x1) ^ (~x1 v ~x2) ^ (x1 v x3) ^ (~x2 v ~x3) ^ (x1 v x4)"
if solve_2sat(expression):
    print("The 2-SAT expression is satisfiable.")
else:
    print("The 2-SAT expression is not satisfiable.")