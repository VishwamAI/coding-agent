"""
Quick Sort Algorithm Implementation in Python

This module contains the implementation of the quick sort algorithm using the first element as the pivot.
"""

def quick_sort(arr):
    """
    Quick sort function that sorts an array in ascending order.
    :param arr: List of elements to be sorted.
    :return: List of elements sorted in ascending order.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + equal + quick_sort(greater)

# Example usage
if __name__ == "__main__":
    example_array = [10, 7, 8, 9, 1, 5]
    print("Original array:", example_array)
    sorted_array = quick_sort(example_array)
    print("Sorted array:", sorted_array)