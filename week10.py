import math

print("Sanath S Shetty")
print("1BM23CS297")

# --- Global Variables ---
# We define the tree globally so the helper function can access it
tree = [] 
# A list to store string descriptions of pruned nodes [cite: 24]
pruned_nodes_list = [] 

# --- Helper Function ---
def get_node_by_path(path_indices):
    """
    A helper function to get a description of a node
    at a given path (list of indices) for readable output.
    """
    node = tree # Access global tree
    try:
        for index in path_indices:
            node = node[index]
        
        if isinstance(node, int):
            # It's a leaf node
            return f"Leaf node ({node})"
        else:
            # It's a branch node. Check if its children are all leaves.
            if all(isinstance(n, int) for n in node):
                 return f"Branch node (children: {node})"
            else:
                 return f"Branch node (children: {len(node)})"
    except (IndexError, TypeError):
        return "Path Error"

# --- Alpha-Beta Pruning Functions ---

def max_value(node, alpha, beta, path_indices=[]):
    """
    Implements the MAX-VALUE function from the pseudocode.
    Returns:
        (int): The utility value for this node.
        (list): The optimal path (list of indices) from this node.
    """
    
    # if TERMINAL-TEST(state) then return UTILITY(state) 
    if isinstance(node, int):
        return node, [] # (value, no path from here)

    # v <- -∞ (Implied initialization for MAX)
    v = -math.inf
    best_path = []
    
    # for each a in ACTIONS(state) do [cite: 66]
    for i, child in enumerate(node):
        
        # v <- ΜΑΧ(v, ΜIN-VALUE(RESULT(s,a), a, β)) [cite: 67]
        # We recursively call min_value for the child
        child_v, child_path = min_value(child, alpha, beta, path_indices + [i])
        
        # If this child's value is better, update v and the best path
        if child_v > v:
            v = child_v
            best_path = [i] + child_path # Prepend this child's index
        
        # if v >= β then return v [cite: 68]
        # This is the pruning condition for a MAX node
        if v >= beta:
            # Prune remaining siblings
            for j in range(i + 1, len(node)):
                pruned_path = path_indices + [j]
                pruned_nodes_list.append(f"Path {pruned_path} (Node: {get_node_by_path(pruned_path)})")
            
            print(f"PRUNING (MAX): At path {path_indices}, v={v} >= beta={beta}. Pruning remaining children.")
            return v, best_path # Return current best
        
        # α <- ΜΑΧ(α, v) [cite: 69]
        alpha = max(alpha, v)
    
    # return v [cite: 70]
    return v, best_path

def min_value(node, alpha, beta, path_indices=[]):
    """
    Implements the MIN-VALUE function from the pseudocode.
    Returns:
        (int): The utility value for this node.
        (list): The optimal path (list of indices) from this node.
    """
    
    # if TERMINAL-TEST(state) then return UTILITY(state) [cite: 72]
    if isinstance(node, int):
        return node, []

    # v <- +∞ [cite: 73]
    v = math.inf
    best_path = []
    
    # for each a in ACTIONS(state) do [cite: 74]
    for i, child in enumerate(node):
        
        # v <- ΜΙΝ(v, ΜAX-VALUE(RESULT(s,a), α, β)) [cite: 75]
        # We recursively call max_value for the child
        child_v, child_path = max_value(child, alpha, beta, path_indices + [i])
        
        # If this child's value is better, update v and the best path
        if child_v < v:
            v = child_v
            best_path = [i] + child_path # Prepend this child's index
        
        # if v <= α then return v [cite: 76]
        # This is the pruning condition for a MIN node
        if v <= alpha:
            # Prune remaining siblings
            for j in range(i + 1, len(node)):
                pruned_path = path_indices + [j]
                pruned_nodes_list.append(f"Path {pruned_path} (Node: {get_node_by_path(pruned_path)})")
                
            print(f"PRUNING (MIN): At path {path_indices}, v={v} <= alpha={alpha}. Pruning remaining children.")
            return v, best_path # Return current best
        
        # β <- MIN(β, v) [cite: 77]
        beta = min(beta, v)
        
    # return v [cite: 78]
    return v, best_path

# --- Main Execution ---

if __name__ == "__main__":
    
    # Define the tree structure from the problem diagram 
    # The leaves are the terminal utility values [cite: 25, 27, 28, 29, 30, 31, 32, 33]
    tree = [  # Root (MAX) [cite: 35]
        [  # MIN node 1 [cite: 36]
            [10, 9],  # MAX node 1.1 [cite: 37]
            [14, 18]  # MAX node 1.2 [cite: 37]
        ],
        [  # MIN node 2 [cite: 36]
            [5, 4],   # MAX node 2.1 [cite: 37]
            [50, 3]   # MAX node 2.2 [cite: 37]
        ]
    ]

    print("Starting Alpha-Beta Search...")
    
    # Initial call to search the tree [cite: 63]
    # We start with max_value because the root is a MAX node [cite: 35]
    # Initial alpha = -infinity, beta = +infinity
    root_value, optimal_path_indices = max_value(tree, -math.inf, math.inf, path_indices=[])
    
    print("\n--- Search Complete ---")

    # --- 1. Find value of root node [cite: 23] ---
    print(f"\n## Value of the Root Node")
    print(f"The final optimal value for the root node is: {root_value}")

    # --- 2. Identify the path to root node [cite: 23] ---
    print(f"\n## Optimal Path")
    print("The path to achieve this value is:")
    path_str = "Root"
    current_node = tree
    print(f"  {path_str} (Value: {root_value})")
    for index in optimal_path_indices:
        current_node = current_node[index]
        if isinstance(current_node, int):
            path_str += f" -> [Leaf {current_node}]"
        else:
            path_str += f" -> [Node at index {index}]"
        print(f"  {path_str}")

    # --- 3. Identify the paths which are Pruned [cite: 24] ---
    print(f"\n## Pruned Paths")
    if pruned_nodes_list:
        print("The following paths were pruned (not explored):")
        for p in pruned_nodes_list:
            print(f"- {p}")
    else:
        print("No paths were pruned.")