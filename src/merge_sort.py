def merge_sort(arr):
    """
    Merge Sort function that sorts an array in ascending order.
    :param arr: List of elements to be sorted.
    :return: List of elements sorted in ascending order.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    """
    Helper function to merge two sorted arrays.
    :param left: Left sorted subarray.
    :param right: Right sorted subarray.
    :return: Merged sorted array.
    """
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Example usage
if __name__ == "__main__":
    example_array = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", example_array)
    sorted_array = merge_sort(example_array)
    print("Sorted array:", sorted_array)