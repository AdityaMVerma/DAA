def fractional_knapsack(capacity, weights, profits):
    n = len(weights)
    value_per_weight = [(profits[i] / weights[i], weights[i], profits[i], i) for i in range(n)]
    value_per_weight.sort(reverse=True)  # Sort items by value-to-weight ratio in descending order

    total_value = 0
    selected_items = []
    remaining_capacity = capacity

    for ratio, weight, profit, index in value_per_weight:
        if remaining_capacity >= weight:
            selected_items.append((index, 1))  # Take the whole item
            total_value += profit
            remaining_capacity -= weight
        else:
            fraction = remaining_capacity / weight
            selected_items.append((index, fraction))
            total_value += profit * fraction
            break  # Knapsack is full

    return total_value, selected_items


# Given data
knapsack_capacity = 20
weights = [3, 5, 5, 8, 4]
profits = [10, 20, 21, 30, 16]

total_value, selected_items = fractional_knapsack(knapsack_capacity, weights, profits)

print("Selected items:")
for item, fraction in selected_items:
    print(f"x{item + 1}: {fraction:.2f} fraction")
print("Total value:", total_value)
