import sys

def calculate_distance(points, order):
    total_distance = 0
    for i in range(len(order) - 1):
        city1, city2 = order[i], order[i + 1]
        total_distance += points[city1][city2]
    return total_distance

def traveling_salesman_brute_force(points):
    num_cities = len(points)
    cities = [i for i in range(num_cities)]
    min_distance = sys.maxsize
    min_path = None

    def permute(order, length):
        nonlocal min_distance, min_path
        if length == num_cities:
            distance = calculate_distance(points, order + (order[0],))
            if distance < min_distance:
                min_distance = distance
                min_path = order + (order[0],)
        else:
            for i in range(length, num_cities):
                order[length], order[i] = order[i], order[length]
                permute(order, length + 1)
                order[length], order[i] = order[i], order[length]  # Backtrack

    permute(cities, 0)
    return min_path, min_distance

# Example usage:
# Replace points with the distances between cities represented in a matrix format
points = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

shortest_path, shortest_distance = traveling_salesman_brute_force(points)
print("Shortest path:", shortest_path)
print("Shortest distance:", shortest_distance)
