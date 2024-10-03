# def.: max distance between any 2 nodes

def diameter_two_dfs(tree):
    def dfs(node, parent, depth):
        max_depth, farthest_node=depth,node
        for child in tree[node]:
            if child!=parent:
                child_depth,child_farthest=dfs(child,node,depth+1)
                if child_depth>max_depth:
                    max_depth,farthest_node=child_depth,child_farthest
        return max_depth,farthest_node
    
    _,far_node=dfs(1,-1,0) #calculate the far node from any node
    max_depth,_=dfs(far_node,-1,0) # the depth from this node to the far_node will have max depth
    return max_depth

def diameter_dp_dfs(tree):
    def dfs(node,parent):
        nonlocal diameter
        max_length1, max_length2=0,0
        for child in tree[node]:
            if child!=parent:
                to_leaf=dfs(child,node) # max length from curr node until a leaf
                if to_leaf>max_length1:
                    max_length2,max_length1=max_length1,to_leaf
                elif to_leaf>max_length2:
                    max_length2=to_leaf
        diameter=max(diameter,max_length1+max_length2) # max length from path wich higher point as current node
        return max_length1+1
    
    diameter=0
    dfs(1,-1) # assume that 1 is the root
    return diameter

    

tree = {1: [2, 3, 4], 2: [1, 5, 6], 3: [1], 4: [1, 7], 5: [2], 6: [2], 7: [4]}

print("Diameter (Two DFS):", diameter_two_dfs(tree))
print("Diameter (DP):", diameter_dp_dfs(tree))