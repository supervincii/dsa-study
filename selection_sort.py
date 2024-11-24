def find_item(arr: list, order: str):
    """
    Finds the smallest value in the array and returns its index.
    """
    item = arr[0]
    item_index = 0

    for i in range(1, len(arr)):
        if (order == "desc" and arr[i] > item) or (order == "asc" and arr[i] < item):
            item = arr[i]
            item_index = i

    return item_index

def selection_sort(arr: list, order: str) -> list | None:
    """
    Sorts an array from smallest to largest. It calls the find_smallest function
    to get the smallest value and gets in index. It pops that value for the array
    and appends it to the new array. Then we run the loop again on the original
    array.
    """
    new_arr = []
    copied_arr = list(arr)

    for _ in range(len(copied_arr)):
        if order in ["asc", "desc"]:
            item = find_item(copied_arr, order)
            new_arr.append(copied_arr.pop(item))
        else:
            print("Order value is not valid")

    return new_arr
