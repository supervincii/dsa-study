def binary_search(sorted_list: list, item: int) -> int | None:
    """
    binary_search function executes a binary search algorithm where we find
    the 'item' index by splitting the 'sorted_list' in half. If the middle value is
    equal to the item value, we return the index of that item. If however the
    middle value is greater than the 'item', we discard the top half and do
    binary search on the lower half. The opposite happens if the middle value is
    less than the 'item'.
    """
    high = len(sorted_list) - 1
    low = 0

    while (low < high):
        middle = (low + high) // 2
        guess = sorted_list[middle]

        if (item == guess):
            return middle
        elif (item > guess):
            low = middle + 1
        elif (item < guess):
            high = middle - 1

    return None
