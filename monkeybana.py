def monkey_banana(rows, cols, bananas):
    table = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for banana in bananas:
        row, col, value = banana
        table[row - 1][col - 1] = value
    
    # Dynamic programming to find the maximum number of bananas the monkey can collect
    for i in range(rows - 1, -1, -1):
        for j in range(cols):
            from_above = table[i + 1][j] if i + 1 < rows else 0
            from_right = table[i][j - 1] if j - 1 >= 0 else 0
            table[i][j] += max(from_above, from_right)
    
    return table[0][cols // 2]  # Max bananas collected at the starting position

# Example usage:
rows = 4
cols = 3
bananas = [(1, 1, 1), (2, 2, 2), (3, 3, 3)]  # Format: (row, column, banana_value)

max_bananas = monkey_banana(rows, cols, bananas)
print("Maximum bananas the monkey can collect:", max_bananas)
