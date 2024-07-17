"""
Heap Sort Algorithm Implementation in Python

This module contains the implementation of the heap sort algorithm.
"""

def heapify(arr, n, i):
    """
    Function to build a max heap from a subtree with node i at the root.
    :param arr: List of integers to heapify
    :param n: Size of the heap
    :param i: Index of the root element of the subtree
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    """
    Main function to sort an array of given size using heap sort.
    :param arr: List of integers to sort
    """
    n = len(arr)

    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr

# Example usage
if __name__ == "__main__":
    example_array = [12, 11, 13, 5, 6, 7]
    print("Original array:", example_array)
    sorted_array = heap_sort(example_array)
    print("Sorted array:", sorted_array)