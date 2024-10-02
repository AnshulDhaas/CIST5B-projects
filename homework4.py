import time
import matplotlib.pyplot as plt

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def print_list(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

if __name__ == "__main__":
    # Best-case scenario (already sorted array)
    arr_best_case = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Best-case scenario:")
    print("Given array is")
    print_list(arr_best_case)
    merge_sort(arr_best_case)
    print("Sorted array is")
    print_list(arr_best_case)
    print()

    # Worst-case scenario for merge sort (reverse sorted array)
    arr_worst_case = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("Worst-case scenario:")
    print("Given array is")
    print_list(arr_worst_case)
    merge_sort(arr_worst_case)
    print("Sorted array is")
    print_list(arr_worst_case)
    print()

    # Random array
    arr_random = [12, 11, 13, 5, 6, 7]
    print("Random array:")
    print("Given array is")
    print_list(arr_random)
    merge_sort(arr_random)
    print("Sorted array is")
    print_list(arr_random)
    
    # Timing Merge Sort and Plotting
    sizes = [100, 1000, 10000, 100000]
    times = []

    for size in sizes:
        arr = list(range(size, 0, -1))  # Worst-case scenario: reverse sorted array
        print(f"Sorting array of size {size}")
        start_time = time.time()
        merge_sort(arr)
        end_time = time.time()
        time_taken = end_time - start_time
        print(f"Time taken: {time_taken:.6f} seconds")
        times.append(time_taken)

    # Plotting the graph
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, marker='o', linestyle='-', color='b')
    plt.title('Merge Sort Time Complexity (Worst Case)')
    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.show()
