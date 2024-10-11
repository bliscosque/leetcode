class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.max_length_down = 0
        self.max_length = 0

def calculate_max_lengths_down(node): # max length that goes down from node (max from children+1)
    if not node.children:
        return 0
    
    child_lengths = [calculate_max_lengths_down(child) for child in node.children]
    node.max_length_down = max(child_lengths) + 1 
    return node.max_length_down

def calculate_max_lengths(node, length_from_parent=0):
    # Calculate max length considering path from parent
    node.max_length = max(node.max_length_down, length_from_parent)
    
    if len(node.children) == 0:
        return
    
    if len(node.children) == 1: # node has only one child... calculate just this 
        calculate_max_lengths(node.children[0], node.max_length + 1)
    else:
        # Find the two longest paths down, if node has more than 2 childs
        first_max, second_max = sorted([child.max_length_down for child in node.children], reverse=True)[:2]
        
        for child in node.children:
            if child.max_length_down == first_max:
                child_length_from_parent = max(second_max + 2, length_from_parent + 1)
            else:
                child_length_from_parent = max(first_max + 2, length_from_parent + 1)
            calculate_max_lengths(child, child_length_from_parent)

def print_max_lengths(node, level=0):
    print("  " * level + f"Node {node.value}: {node.max_length}")
    for child in node.children:
        print_max_lengths(child, level + 1)

# Criando a árvore do exemplo
root = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

root.children = [node2, node3, node4]
node2.children = [node5, node6]

# Calculando os comprimentos máximos
calculate_max_lengths_down(root)
calculate_max_lengths(root)

# Imprimindo os resultados
print("Comprimentos máximos dos caminhos para cada nó:")
print_max_lengths(root)

# Calculando o diâmetro da árvore
diameter = max(node.max_length for node in [root, node2, node3, node4, node5, node6])
print(f"\nDiâmetro da árvore: {diameter}")