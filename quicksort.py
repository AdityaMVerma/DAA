#quicksort
import timeit
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)

        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)


# Example usage
starttime = timeit.default_timer()
input_list = [12,23,65,45]
quicksort(input_list, 0, len(input_list) - 1)
print(input_list)
endtime = timeit.default_timer()
print(endtime - starttime)
