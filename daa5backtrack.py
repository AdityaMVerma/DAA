def knapsack_backtracking(values, weights, capacity):
    n = len(values)

    def backtrack(index, current_weight, current_value):
        nonlocal max_value
        if index == n or current_weight == capacity:
            max_value = max(max_value, current_value)
            return

        # Check if adding the current item exceeds the capacity
        if current_weight + weights[index] <= capacity:
            # Include the current item
            backtrack(index + 1, current_weight + weights[index], current_value + values[index])

        # Exclude the current item
        backtrack(index + 1, current_weight, current_value)

    max_value = 0
    backtrack(0, 0, 0)
    return max_value

# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

result = knapsack_backtracking(values, weights, capacity)
print("Maximum value:", result)
