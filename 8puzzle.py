import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, move=None, depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = self.calculate_cost()

    def calculate_cost(self):
        # Manhattan distance heuristic
        cost = 0
        goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    goal_row, goal_col = divmod(self.state[i][j] - 1, 3)
                    cost += abs(i - goal_row) + abs(j - goal_col)

        return cost + self.depth

    def get_children(self):
        children = []
        zero_row, zero_col = self.get_blank_position()

        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dr, dc in moves:
            new_row, new_col = zero_row + dr, zero_col + dc

            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state = [row[:] for row in self.state]
                new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], 0
                children.append(PuzzleNode(new_state, self, (new_row, new_col), self.depth + 1))

        return children

    def get_blank_position(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

    def __lt__(self, other):
        return self.cost < other.cost

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]

def solve_8_puzzle(initial_state):
    initial_node = PuzzleNode(initial_state)
    heap = [initial_node]
    heapq.heapify(heap)
    visited = set()

    while heap:
        current_node = heapq.heappop(heap)

        if current_node.state == [[0, 1, 2], [3, 4, 5], [6, 7, 8]]:
            return reconstruct_path(current_node)

        visited.add(tuple(map(tuple, current_node.state)))

        for child in current_node.get_children():
            if tuple(map(tuple, child.state)) not in visited:
                heapq.heappush(heap, child)

    return None

# Example usage:
initial_state = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
solution = solve_8_puzzle(initial_state)

if solution:
    print("Solution found!")
    for step in solution:
        print("Step:")
        for row in step:
            print(row)
        print("-----")
else:
    print("No solution exists.")
