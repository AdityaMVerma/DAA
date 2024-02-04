def subset_sum(nums, target):
    def backtrack(start, target, path):
        if target == 0:
            result.append(path[:])
            return
        for i in range(start, len(nums)):
            if nums[i] > target:
                continue
            path.append(nums[i])
            backtrack(i + 1, target - nums[i], path)
            path.pop()

    result = []
    backtrack(0, target, [])
    return result

# Example usage:
S = {1, 2, 5, 6, 8}
target_sum = 9

subsets = subset_sum(list(S), target_sum)

if subsets:
    print("Subset(s) with sum", target_sum, "found:")
    for subset in subsets:
        print(subset)
else:
    print("No solution found.")
