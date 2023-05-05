def bubble_sort(lst):
    """
    Sorts the given list using the bubble sort algorithm.

    Args:
        lst: List[int] - The list of integers to be sorted.

    Returns:
        List[int]: The sorted list of integers.
    """
    n = len(lst)
    # Flag to check if any swaps were made in the previous iteration.
    # If no swaps were made, the list is already sorted and the algorithm can exit early.
    flag = True
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                # Swap the elements
                lst[j], lst[j+1] = lst[j+1], lst[j]
                # Mark that a swap has been made in this iteration
                flag = False
        # If no swaps were made in the current iteration, the list is already sorted.
        if flag:
            break
    return lst

if __name__ == "__main__":
    lst = [5, 4, 3, 2, 1]
    print(bubble_sort(lst))

