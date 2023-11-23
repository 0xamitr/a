from collections import deque

# Representation of the state: (left_bank, right_bank, boat_position)
# Each bank is represented as a tuple (missionaries, cannibals)
INITIAL_STATE = ((3, 3), (0, 0), 'left')
GOAL_STATE = ((0, 0), (3, 3), 'right')

def is_valid(state):
    left_bank, right_bank, boat_position = state

    # Check if the number of cannibals is greater than the number of missionaries on any bank
    if left_bank[0] < left_bank[1] and left_bank[0] > 0:
        return False
    if right_bank[0] < right_bank[1] and right_bank[0] > 0:
        return False

    return True

def generate_next_states(state):
    next_states = []
    left_bank, right_bank, boat_position = state

    if boat_position == 'left':
        for m in range(3 + 1):
            for c in range(3 + 1):
                if 1 <= m + c <= 2:
                    new_left_bank = (left_bank[0] - m, left_bank[1] - c)
                    new_right_bank = (right_bank[0] + m, right_bank[1] + c)
                    new_boat_position = 'right'
                    new_state = (new_left_bank, new_right_bank, new_boat_position)
                    if is_valid(new_state):
                        next_states.append(new_state)
    else:
        for m in range(3 + 1):
            for c in range(3 + 1):
                if 1 <= m + c <= 2:
                    new_left_bank = (left_bank[0] + m, left_bank[1] + c)
                    new_right_bank = (right_bank[0] - m, right_bank[1] - c)
                    new_boat_position = 'left'
                    new_state = (new_left_bank, new_right_bank, new_boat_position)
                    if is_valid(new_state):
                        next_states.append(new_state)

    return next_states

def missionaries_cannibals():
    queue = deque([(INITIAL_STATE, [])])
    visited = set()

    while queue:
        current_state, actions = queue.popleft()
        if current_state == GOAL_STATE:
            return actions

        visited.add(current_state)
        next_states = generate_next_states(current_state)

        for next_state in next_states:
            if next_state not in visited:
                queue.append((next_state, actions + [next_state]))

    return None

def print_solution(solution):
    if solution:
        print("Solution Found:")
        for state in solution:
            print(state)
    else:
        print("No solution found.")

solution = missionaries_cannibals()
print_solution(solution)
