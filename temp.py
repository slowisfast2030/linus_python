import random

def quick_sort(arr, T=10):
    """
    Sorts an array of integers using the quick sort algorithm.

    Args:
        arr (List[int]): The array to be sorted.
        T (int): Threshold for when to switch to insertion sort.

    Returns:
        List[int]: The sorted array.
    """
    if len(arr) < 2:
        # Base case: an array with 0 or 1 element is already sorted
        return arr
    elif len(arr) <= T:
        # Use insertion sort for small arrays
        return insertion_sort(arr)
    else:
        # Choose a random pivot element
        pivot_idx = random.randint(0, len(arr) - 1)
        pivot = arr[pivot_idx]
        # Partition the array around the pivot element
        less, equal, greater = partition(arr, pivot)
        # Recursively sort the sub-arrays less and greater
        return quick_sort(less, T=T) + equal + quick_sort(greater, T=T)

def insertion_sort(arr):
    """
    Sorts an array of integers using the insertion sort algorithm.

    Args:
        arr (List[int]): The array to be sorted.

    Returns:
        List[int]: The sorted array.
    """
    for i in range(1, len(arr)):
        current_value = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current_value:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = current_value
    return arr

def partition(arr, pivot):
    """
    Partitions an array around a pivot element.

    Args:
        arr (List[int]): The array to be partitioned.
        pivot (int): The pivot element.

    Returns:
        Tuple[List[int], List[int], List[int]]: A tuple containing three arrays -
            the elements less than the pivot, the elements equal to the pivot,
            and the elements greater than the pivot.
    """
    less, equal, greater = [], [], []
    for elem in arr:
        if elem < pivot:
            less.append(elem)
        elif elem == pivot:
            equal.append(elem)
        else:
            greater.append(elem)
    return less, equal, greater

if __name__ == "__main__":
    # Test the quick sort algorithm
    arr = [random.randint(0, 100) for _ in range(20)]
    print("Unsorted array:")
    print(arr)
    print("Sorted array:")
    print(quick_sort(arr, T=10))

