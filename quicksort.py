def quicksort(arr: list) -> list:
    """
    quicksort is a sorting algorithm faster than selection sort and uses the
    concept of divide and conquer.
    """

    # Base case where the length of the array is 0 or 1, we do not need to sort it
    # and we can just return the array
    if len(arr) < 2:
        return arr

    # Else if the array length is greater than 1, we get a pivot element and sort
    # the array based on that.
    else:
        # Use the first element as the pivot
        pivot = arr[0]
        # Create new arrays for values that are less than and greater than the pivot
        less = [i for i in arr[1:] if i < pivot]
        greater = [i for i in arr[1:] if i > pivot ]

    # Recursive case where we get the sorted of less and greater array
    # and add the resulting array with the pivot.
    return quicksort(less) + [pivot] + quicksort(greater)
