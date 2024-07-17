def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the index of the target value.
    If the target is not found, return -1.

    :param arr: List[int], the sorted array to search
    :param target: int, the target value to search for
    :return: int, the index of the target value in the array
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage
if __name__ == "__main__":
    example_array = [1, 3, 5, 7, 9, 11, 13, 15]
    target_value = 9
    result = binary_search(example_array, target_value)
    print(f"Index of {target_value}: {result}")