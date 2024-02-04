def unsorted_binary_search(arr, low, high, key):
    if low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[low] <= key < arr[mid]:
            return unsorted_binary_search(arr, low, mid - 1, key)
        else:
            return unsorted_binary_search(arr, mid + 1, high, key)
    else:
        return -1

if __name__ == "__main__":
    # Generate an unsorted list of at least 5000 elements
    import random
    unsorted_list = random.sample(range(1, 10000), 5000)
    unsorted_list.sort()  # Sorting the list for comparison

    key = int(input("Enter the key to search: "))

    result = unsorted_binary_search(unsorted_list, 0, len(unsorted_list) - 1, key)

    if result != -1:
        print(f"Key {key} found at index {result}.")
    else:
        print(f"Key {key} not found in the list.")
