from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def remove_edge(self, u, v):
        self.graph[u].remove(v)
        self.graph[v].remove(u)
    
    def find_start_vertex(self):
        # Encontrar vértices de grau ímpar
        odd_vertices = [v for v in self.graph if len(self.graph[v]) % 2 != 0]
        
        if len(odd_vertices) == 0:
            # Se todos os vértices têm grau par, podemos começar de qualquer um
            return min(self.graph.keys())
        elif len(odd_vertices) == 2:
            # Se há dois vértices de grau ímpar, começamos em um deles
            return odd_vertices[0]
        else:
            # Se há mais de dois vértices de grau ímpar, não existe caminho euleriano
            return None
    
    def hierholzer(self):
        start_vertex = self.find_start_vertex()
        if start_vertex is None:
            return None
            
        # Criar uma cópia do grafo para não modificar o original
        current_graph = defaultdict(list)
        for v in self.graph:
            current_graph[v] = self.graph[v].copy()
        
        def find_next_path(vertex):
            path = [vertex]
            current_v = vertex
            
            while True:
                if not current_graph[current_v]:
                    return path
                
                next_v = current_graph[current_v][0]
                current_graph[current_v].remove(next_v)
                current_graph[next_v].remove(current_v)
                
                current_v = next_v
                path.append(current_v)
        
        final_path = []
        stack = [start_vertex]
        
        while stack:
            current_vertex = stack[-1]
            
            if current_graph[current_vertex]:
                new_path = find_next_path(current_vertex)
                stack.extend(new_path[1:])
            else:
                final_path.append(stack.pop())
        
        return final_path[::-1]

# Criar e preencher o grafo do exemplo
g = Graph(8)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(2, 5)
g.add_edge(2, 6)
g.add_edge(3, 4)
g.add_edge(3, 6)
g.add_edge(4, 7)
g.add_edge(5, 6)
g.add_edge(6, 7)

# Encontrar um caminho euleriano
path = g.hierholzer()

print("Caminho Euleriano encontrado:")
if path:
    print(" -> ".join(map(str, path)))
else:
    print("Não existe caminho euleriano neste grafo")