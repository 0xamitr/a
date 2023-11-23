from collections import deque

# Function to perform Breadth-First Search
def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    visited = set()
    queue = deque([(0, 0)])  # Starting with both jugs empty
    visited.add((0, 0))
    steps = []

    while queue:
        jug1, jug2 = queue.popleft()

        # Check if target is reached
        if jug1 == target or jug2 == target:
            steps.append((jug1, jug2))
            while jug1 != 0 or jug2 != 0:
                for step in steps[::-1]:
                    print(step)
                    if step[0] == jug1 and step[1] == jug2:
                        if step[0] != 0:
                            print("Pour {} liters from Jug 1".format(step[0]))
                        if step[1] != 0:
                            print("Pour {} liters from Jug 2".format(step[1]))
                        jug1 -= step[0]
                        jug2 -= step[1]
                        break

            return True

        # Pour from jug1 to jug2
        if jug1 > 0 and jug2 != jug2_capacity:
            temp = min(jug1, jug2_capacity - jug2)
            if (jug1 - temp, jug2 + temp) not in visited:
                visited.add((jug1 - temp, jug2 + temp))
                queue.append((jug1 - temp, jug2 + temp))
                steps.append((jug1 - temp, jug2 + temp))

        # Pour from jug2 to jug1
        if jug2 > 0 and jug1 != jug1_capacity:
            temp = min(jug2, jug1_capacity - jug1)
            if (jug1 + temp, jug2 - temp) not in visited:
                visited.add((jug1 + temp, jug2 - temp))
                queue.append((jug1 + temp, jug2 - temp))
                steps.append((jug1 + temp, jug2 - temp))

    return False

# Example usage:
jug1_capacity = 4
jug2_capacity = 3
target_amount = 2

result = water_jug_bfs(jug1_capacity, jug2_capacity, target_amount)
if not result:
    print("Target amount {} liters cannot be measured using the given jugs.".format(target_amount))
