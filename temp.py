def quick_sort(arr):
    """
    Sorts an array of integers using the quick sort algorithm.

    Args:
        arr (List[int]): The array to be sorted.

    Returns:
        List[int]: The sorted array.

    """
    if len(arr) < 2:
        # Base case: an array with 0 or 1 element is already sorted
        return arr
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]
    # Recursively sort the sub-arrays less and greater
    return quick_sort(less) + [pivot] + quick_sort(greater)

if __name__ == '__main__':
    arr = [5, 3, 6, 2, 10]
    print(quick_sort(arr))

