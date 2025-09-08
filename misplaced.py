

import heapq

print("Sanath S Shetty")
print("1BM23CS297")

def print_state(state):
    """Prints the 8-puzzle state in a 3x3 grid."""
    for i in range(0, 9, 3):
        print(" ".join(str(x) for x in state[i:i+3]))
    print()

def misplaced_tiles(current_state, goal_state):
    """Calculates the number of misplaced tiles heuristic."""
    misplaced = 0
    for i in range(9):
        if current_state[i] != 0 and current_state[i] != goal_state[i]:
            misplaced += 1
    return misplaced

def find_zero(state):
    """Finds the index of the blank tile (0)."""
    return state.index(0)

def get_neighbors(state):
    """Generates possible next states (neighbors) from the current state."""
    neighbors = []
    zero_index = find_zero(state)
    row, col = divmod(zero_index, 3)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_state_list = list(state)
            new_state_list[zero_index], new_state_list[new_index] = new_state_list[new_index], new_state_list[zero_index]
            neighbors.append(tuple(new_state_list))
    return neighbors

def astar_misplaced(start_state, goal_state):
    """Solves the 8-puzzle using A* with the misplaced tiles heuristic."""
    open_set = []
    heapq.heappush(open_set, (misplaced_tiles(start_state, goal_state), 0, start_state, [])) # (f_cost, g_cost, state, path)
    visited = set()
    visited.add(start_state)
    state_count = 0

    while open_set:
        f_cost, g_cost, current_state, path = heapq.heappop(open_set)
        state_count += 1

        if current_state == goal_state:
            print("\nGoal reached!")
            print("Number of states explored:", state_count)
            print("depth:", g_cost)
            print("\nSolution path:")
            for s in path + [current_state]:
                print_state(s)
            return path

        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                visited.add(neighbor)
                new_g_cost = g_cost + 1
                new_f_cost = new_g_cost + misplaced_tiles(neighbor, goal_state)
                heapq.heappush(open_set, (new_f_cost, new_g_cost, neighbor, path + [current_state]))

    print("No solution found.")
    return None

# --- Main Execution ---
print("Enter the INITIAL 8-puzzle board configuration (use 0 for blank):")
initial_board = []
for i in range(3):
    row = input(f"Row {i+1} (3 numbers space-separated): ").split()
    initial_board.extend(map(int, row))

print("\nEnter the GOAL 8-puzzle board configuration (use 0 for blank):")
goal_board = []
for i in range(3):
    row = input(f"Row {i+1} (3 numbers space-separated): ").split()
    goal_board.extend(map(int, row))

start_state = tuple(initial_board)
goal_state = tuple(goal_board)

print("\nInitial State:")
print_state(start_state)

print("Goal State:")
print_state(goal_state)

astar_misplaced(start_state, goal_state)