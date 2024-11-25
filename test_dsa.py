from binary_search import binary_search
from selection_sort import selection_sort

def test_binary_search():
    arr = [1, 2, 3, 4, 5]
    val = 4

    assert binary_search(arr, val) == 3


def test_selection_sort():
    int_arr = [1, 2, 5, 10, 22, 5, 6, 12, 11, 13, 20, 21, 0, 3]
    assert selection_sort(int_arr, "asc") == [0, 1, 2, 3, 5 ,5, 6, 10, 11, 12, 13, 20, 21, 22]
    assert selection_sort(int_arr, "desc") == [22, 21, 20, 13, 12, 11, 10, 6, 5, 5, 3, 2, 1, 0]

    char_arr = ["a", "c", "f", "z", "q", "b"]
    assert selection_sort(char_arr, "asc") == ["a", "b", "c", "f", "q", "z"]
    assert selection_sort(char_arr, "desc") == ["z", "q", "f", "c", "b", "a"]
