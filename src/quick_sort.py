"""
Quick Sort Algorithm Implementation in Python

This module contains the implementation of the quick sort algorithm.
"""

def partition(arr, low, high):
    """
    Function to place the pivot element at its correct position in sorted array, and places all smaller to left of pivot and all greater elements to right of pivot.
    :param arr: List of integers to sort
    :param low: Starting index
    :param high: Ending index
    :return: index of pivot
    """
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quick_sort(arr, low, high):
    """
    The main function that implements QuickSort
    :param arr: List of integers to sort
    :param low: Starting index
    :param high: Ending index
    """
    if len(arr) == 1:
        return arr
    if low < high:
        # pi is partitioning index, arr[p] is now at right place
        pi = partition(arr, low, high)

        # Separately sort elements before partition and after partition
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)

# Example usage
if __name__ == "__main__":
    example_array = [10, 7, 8, 9, 1, 5]
    n = len(example_array)
    print("Original array:", example_array)
    quick_sort(example_array, 0, n-1)
    print("Sorted array is:", example_array)