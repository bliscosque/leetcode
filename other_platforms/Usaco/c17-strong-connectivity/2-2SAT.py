from collections import defaultdict

class TwoSAT:
    def __init__(self, n):
        self.n = n  # Número de variáveis
        self.adj = defaultdict(list)  # Grafo de implicações
        self.adj_inv = defaultdict(list)  # Grafo transposto
        self.visited = [False] * (2 * n)
        self.scc = [-1] * (2 * n)
        self.stack = []
        
    def add_clause(self, u, v):
        """Adiciona cláusula (u ∨ v) ao grafo de implicações."""
        # para cala clausula, adicionamos "Nao A -> B" e "Nao B -> A"
        self.adj[u ^ 1].append(v)  # ¬u implica v
        self.adj[v ^ 1].append(u)  # ¬v implica u
        self.adj_inv[v].append(u ^ 1)
        self.adj_inv[u].append(v ^ 1)
        
    def dfs1(self, v):
        self.visited[v] = True
        for neighbor in self.adj[v]:
            if not self.visited[neighbor]:
                self.dfs1(neighbor)
        self.stack.append(v)
        
    def dfs2(self, v, label):
        self.scc[v] = label
        for neighbor in self.adj_inv[v]:
            if self.scc[neighbor] == -1:
                self.dfs2(neighbor, label)
                
    def solve(self):
        # Os passos 1 e 2 são do algoritmo de Kosaraju

        # Passo 1: Executa DFS para ordem topológica
        for i in range(2 * self.n):
            if not self.visited[i]:
                self.dfs1(i)
        
        # Passo 2: Processa grafo transposto por ordem reversa
        label = 0
        while self.stack:
            v = self.stack.pop()
            if self.scc[v] == -1:
                self.dfs2(v, label)
                label += 1
                
        # Verifica se cada variável está em componente diferente de sua negação
        assignment = [False] * self.n
        for i in range(self.n):
            if self.scc[2 * i] == self.scc[2 * i + 1]:
                return None  # Não é satisfazível
            assignment[i] = self.scc[2 * i] < self.scc[2 * i + 1]
            
        return assignment


def main():
    # Número de variáveis na expressão
    n = 4
    solver = TwoSAT(n)
    
    # Adiciona as cláusulas da expressão L1 = (x2 ∨ ¬x1)∧(¬x1 ∨ ¬x2)∧(x1 ∨ x3)∧(¬x2 ∨ ¬x3)∧(x1 ∨ x4)
    # Cada variável xi é mapeada para um índice par (2i), e sua negação para o índice ímpar (2i+1)
    # Traduzindo as cláusulas para índices:
    # x1 -> 0, ¬x1 -> 1, x2 -> 2, ¬x2 -> 3, x3 -> 4, ¬x3 -> 5, x4 -> 6, ¬x4 -> 7

    solver.add_clause(2, 1)   # (x2 ∨ ¬x1)
    solver.add_clause(1, 3)   # (¬x1 ∨ ¬x2)
    solver.add_clause(0, 4)   # (x1 ∨ x3)
    solver.add_clause(3, 5)   # (¬x2 ∨ ¬x3)
    solver.add_clause(0, 6)   # (x1 ∨ x4)

    result = solver.solve()
    
    if result is None:
        print("A expressão não é satisfazível.")
    else:
        print("A expressão é satisfazível. Atribuição:", result)


if __name__ == "__main__":
    main()
