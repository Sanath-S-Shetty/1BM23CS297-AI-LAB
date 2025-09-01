from collections import deque

# Function to display puzzle state
def print_state(state):
    for i in range(0, 9, 3):
        print(" ".join(state[i:i+3]))
    print()

# Generate neighbors
def get_neighbors(state):
    neighbors = []
    index = state.index("0")  # blank position
    row, col = divmod(index, 3)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            state_list = list(state)
            # swap blank
            state_list[index], state_list[new_index] = state_list[new_index], state_list[index]
            neighbors.append("".join(state_list))
    return neighbors

# BFS solver
def bfs(start, goal):
    visited = set()
    queue = deque([(start, [])])  # (state, path)
    visited.add(start)
    state_count = 1

    while queue:
        state, path = queue.popleft()

        if state == goal:
            print("\n Goal reached!")
            print(" Number of states explored:", state_count)
            print("  Number of moves:", len(path))
            print("\nSolution path:")
            for s in path + [state]:
                print_state(s)
            return path

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [state]))
                state_count += 1

    print("No solution found.")
    return None

# --------------------------
# MAIN PROGRAM
# --------------------------
print("Enter the INITIAL 8-puzzle board configuration (use 0 for blank):")
initial_board = []
for i in range(3):
    row = input(f"Row {i+1} (3 numbers space-separated): ").split()
    initial_board.extend(row)

print("\nEnter the GOAL 8-puzzle board configuration (use 0 for blank):")
goal_board = []
for i in range(3):
    row = input(f"Row {i+1} (3 numbers space-separated): ").split()
    goal_board.extend(row)

start_state = "".join(initial_board)

goal_state = "".join(goal_board)

print("\nInitial State:")
print_state(start_state)

print("Goal State:")
print_state(goal_state)

bfs(start_state, goal_state)
print("Sanath S Shetty")
print("1BM23CS297")
